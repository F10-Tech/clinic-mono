import { defineStore } from 'pinia';
import { useServicesApi } from '../../api/services';
import { useAgentStore } from './agent';
import { convertToDict, type baseType } from './_helpers';
import { apiUrl } from '../../main';
import type { Service } from '../../models/service';

const { servicesApi: api } = useServicesApi();
const agentStore = useAgentStore();

export const useServicesStore = defineStore('services', {
  state: (): baseType<Service> => ({
    all: {},
    order: [],
    filteredIds: [],
    filterQuery: '',
    selectedId: undefined,
    editedId: undefined,
  }),

  actions: {
    async fetchAll(): Promise<Boolean> {
      try {
        const { data } = await api.all();
        const { all, order } = convertToDict(data);
        this.all = all;
        this.order = order;
      } catch (error: any) {
        const message = error.response.data.message;
        return false;
      }
      return true;
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

    async deleteService(id: string): Promise<boolean> {
      try {
        await api.delete(id);
        return true;
      } catch (error: any) {
        const message = error.response.data.message;
        return false;
      }
    },
    async create(
      one: Service,
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

    async patch(
      id: string,
      one: Partial<Service>,
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
        const { data } = await axios.post(apiUrl + '/service/' + id + '/uploadImage', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
            Authorization: `JWT ${agentStore.accessToken}`,
          },
        });
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
    selected(state): Service | undefined {
      return state.selectedId ? state.all[state.selectedId] : undefined;
    },

    edited(state): Service | undefined {
      return state.editedId ? state.all[state.editedId] : undefined;
    },

    list(state): Service[] {
      return state.order.map((id) => state.all[id]);
    },

    filteredList(state): Service[] {
      if (state.filterQuery != '') return state.filteredIds.map((id) => state.all[id]);

      return this.list;
    },
  },

  persist: true,
});
