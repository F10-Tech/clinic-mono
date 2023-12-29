import { defineStore } from 'pinia';

import { useSubServicesApi } from '../../api/subServices';
import { useAgentStore } from './agent';
import { convertToDict, type baseType } from './_helpers';
import { apiUrl } from '../../main';
import type { Subservice } from '../../models/subservice';

const agentStore = useAgentStore();

const { subServicesApi: api } = useSubServicesApi();

export const useSubServicesStore = defineStore('subServices', {
  state: (): baseType<Subservice> => ({
    all: {},
    order: [],
    filteredIds: [],
    filterQuery: '',
    selectedId: undefined,
    editedId: undefined,
    diseases: [],
  }),

  actions: {
    async fetchAll(): Promise<Boolean> {
      try {
        const axios = await api.raw();
        const { data } = await axios.get(apiUrl + '/service/subservice');
        const { all, order } = convertToDict(data);
        this.all = all;
        this.order = order;
      } catch (error: any) {
        const message = error.response.data.message;
        return false;
      }
      return true;
    },

    async create(
      one: Subservice,
      image_dark: File | null = null,
      image_light: File | null = null,
    ): Promise<Boolean> {
      try {
        const { data } = await api.post(one);
        if (data) {
          if (image_dark) {
            const formData = new FormData();
            formData.append('image_dark', image_dark);
            await this.uploadImage(data.id, formData);
          }
          if (image_light) {
            const formData = new FormData();
            formData.append('image_light', image_light);
            await this.uploadImage(data.id, formData);
          }
        }
      } catch (error: any) {
        return false;
      }
      return true;
    },

    async delete(id: string): Promise<Boolean> {
      try {
        await api.delete(id);
        return true;
      } catch (error: any) {
        const message = error.response.data.message;
        return false;
      }
    },

    async fetchByService(id: string): Promise<Subservice[]> {
      try {
        const axios = await api.raw();
        const { data } = await axios.get(apiUrl + '/service/' + id + '/subservice');
        const { all, order } = convertToDict(data);
        return data.map((subservice: Subservice) => subservice);
      } catch (error: any) {
        const message = error.response.data.message;
        return [];
      }
    },

    async fetchOne(id: string): Promise<Boolean> {
      try {
        const data = await api.one(id);
        return data;
      } catch (error: any) {
        const message = error.response.data.message;

        return false;
      }
    },
    async fetchSubservicesList(): Promise<Boolean> {
      try {
        const axios = await api.raw();
        const { data } = await axios.get(apiUrl + '/service/subservice/ids');
        const { all, order } = convertToDict(data);
        this.order = order;
        this.filteredIds = order.map((id) => all[id].id);
      } catch (error: any) {
        const message = error.response.data.message;
        return false;
      }
      return true;
    },

    async patch(
      id: string,
      one: Partial<Subservice>,
      image_dark: File | null = null,
      image_light: File | null = null,
    ): Promise<Boolean> {
      try {
        if (one) {
          const { data } = await api.patch(id, one);
        }
        if (image_dark) {
          const formData = new FormData();
          formData.append('image_dark', image_dark);
          await this.uploadImage(id, formData);
        }
        if (image_light) {
          const formData = new FormData();
          formData.append('image_light', image_light);
          await this.uploadImage(id, formData);
        }
      } catch (error: any) {
        return false;
      }
      return true;
    },
    async uploadImage(id: string, formData: FormData): Promise<Boolean> {
      try {
        const axios = await api.raw();
        const { data } = await axios.post(
          apiUrl + '/service/subservice/' + id + '/uploadImage',
          formData,
          {
            headers: {
              'Content-Type': 'multipart/form-data',
              Authorization: `JWT ${agentStore.accessToken}`,
            },
          },
        );
        if (data) {
          return true;
        }
        return false;
      } catch (error: any) {
        const message = error.response.data.message;
        return false;
      }
    },
  },

  getters: {
    selected(state): Subservice | undefined {
      return state.selectedId ? state.all[state.selectedId] : undefined;
    },

    edited(state): Subservice | undefined {
      return state.editedId ? state.all[state.editedId] : undefined;
    },

    list(state): Subservice[] {
      return state.order.map((id) => state.all[id]);
    },

    filteredList(state): Subservice[] {
      if (state.filterQuery != '') return state.filteredIds.map((id) => state.all[id]);

      return this.list;
    },
  },

  persist: true,
});
