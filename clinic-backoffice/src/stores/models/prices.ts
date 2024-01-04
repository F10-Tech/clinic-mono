import { defineStore } from 'pinia';
import { usePricesApi } from '../../api/prices';
import { useAgentStore } from './agent';
import { convertToDict, type baseType } from './_helpers';
import { apiUrl } from '../../main';
import type { Price } from '../../models';

const agentStore = useAgentStore();
const { pricesApi: api } = usePricesApi();

export const usePriceStore = defineStore('prices', {
  state: (): baseType<Price> => ({
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
    async fetchTotal(query: string): Promise<number> {
      try {
        const axiosInstance = await api.raw();
        const response = await axiosInstance.get(apiUrl + '/order/total/' + query);
        
        if (typeof response.data === 'number') {
          return response.data;
        } else {
          throw new Error('Data received is not a number');
        }
      } catch (error) {
        throw error;
      }
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
      one: Price,
    ): Promise<Boolean> {
      try {
        const { data } = await api.post(one);
      } catch (error: any) {
        return false;
      }
      return true;
    },
    async patch(id: string, one: Partial<Price>,
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
    async delete(id: string): Promise<boolean> {
      try {
        await api.delete(id);
        return true;
      } catch (error: any) {
        const message = error.response.data.message;
        return false;
      }
    },
    unsetFilter() {
      this.filterQuery = '';
      this.filteredIds = [];
    },
  },

  getters: {
    selected(state): Price | undefined {
      return state.selectedId ? state.all[state.selectedId] : undefined;
    },

    edited(state): Price | undefined {
      return state.editedId ? state.all[state.editedId] : undefined;
    },

    list(state): Price[] {
      return state.order.map((id) => state.all[id]);
    },

    filteredList(state): Price[] {
      if (state.filterQuery != '') return state.filteredIds.map((id) => state.all[id]);
      return this.list;
    },
  },

  persist: true,
});
