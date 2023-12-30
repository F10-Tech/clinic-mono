import { defineStore } from 'pinia';
import { usePatientsApi } from '../../api/patients';
import { useAgentStore } from './agent';
import { convertToDict, type baseType } from './_helpers';
import { apiUrl } from '../../main';
import type { Patient } from '../../models';

const agentStore = useAgentStore();
const { patientsApi: api } = usePatientsApi();
type SearchByType = 'name' | 'phone';

export const usePatientsStore = defineStore('patients', {
  state: (): baseType<Patient> => ({
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
        return false;
      }
      return true;
    },
    async fetchOne(id: string): Promise<Boolean> {
      try {
        const axios = await api.raw();
        const { data } = await axios.get(apiUrl + '/order/one/' + id);
        return data;
      } catch (error: any) {
        const message = error.response.data.message;
        return false;
      }
    },
    async create(
      one: Patient,
      img_1: File | null = null,
      img_2: File | null = null,
    ): Promise<Boolean> {
      try {
        const { data } = await api.post(one);
        if (data) {
          if (img_1) {
            const formData = new FormData();
            formData.append('img_1', img_1);
            await this.uploadImage(data.id, formData);
          }
          if (img_2) {
            const formData = new FormData();
            formData.append('img_2', img_2);
            await this.uploadImage(data.id, formData);
          }
        }
      } catch (error: any) {
        return false;
      }
      return true;
    },
    async patch(id: string, one: Partial<Patient>,
      img_1: File | null = null,
      img_2: File | null = null,): Promise<Boolean> {
      try {
        if (one) {
          const axios = await api.raw();
          const { data } = await axios.patch(apiUrl + '/patient/'+ id +'/update' , one, {
            headers: {
              // 'Content-Type': 'multipart/json',
              Authorization: `JWT ${agentStore.accessToken}`,
            },
          });
        }
        if (img_1) {
          console.log(img_1);
          const formData = new FormData();
          formData.append('img_1', img_1);
          await this.uploadImage(id, formData);
        }
        if (img_2) {
          const formData = new FormData();
          formData.append('img_2', img_2);
          await this.uploadImage(id, formData);
        }
        
        return true;
      } catch (error: any) {
        return false;
      }
    },
    async uploadImage(id: string, formData: FormData): Promise<Boolean> {
      try {
        const axios = await api.raw();
        const { data } = await axios.post(apiUrl + '/patient/' + id + '/uploadImage', formData, {
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
    async deletePatient(id: string): Promise<boolean> {
      try {
        await api.delete(id);
        return true;
      } catch (error: any) {
        const message = error.response.data.message;
        return false;
      }
    },
    localSearch(searchBy: SearchByType) {
      try {
        const results: Patient[] = [];
        const objects = Object.values(this.all);
        if (this.filterQuery != '') {
          for (const object of objects) {
            if (object[searchBy]!.toLowerCase().includes(this.filterQuery.toLowerCase())) {
              results.push(object);
            }
          }
          this.filteredIds = results.map((result) => result.id);
        }
      } catch (error: any) {
        const message = error.response.data.message;
      }
    },
    unsetFilter() {
      this.filterQuery = '';
      this.filteredIds = [];
    },
  },

  getters: {
    selected(state): Patient | undefined {
      return state.selectedId ? state.all[state.selectedId] : undefined;
    },

    edited(state): Patient | undefined {
      return state.editedId ? state.all[state.editedId] : undefined;
    },

    list(state): Patient[] {
      return state.order.map((id) => state.all[id]);
    },

    filteredList(state): Patient[] {
      if (state.filterQuery != '') return state.filteredIds.map((id) => state.all[id]);
      return this.list;
    },
  },

  persist: true,
});
