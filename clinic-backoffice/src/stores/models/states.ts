import { defineStore } from 'pinia';
import { useStatesApi } from '../../api/states';
import { useAgentStore } from './agent';
import { convertToDict, type baseType } from './_helpers';
import { apiUrl } from '../../main';
import type { State } from '../../models';

const agentStore = useAgentStore();
const { statesApi: api } = useStatesApi();
type SearchByType = 'name';

export const useStateStore = defineStore('state', {
  state: (): baseType<State> => ({
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
    // async fetchOne(id: string): Promise<Boolean> {
    //   try {
    //     const axios = await api.raw();
    //     const { data } = await axios.get(apiUrl + '/order/one/' + id);
    //     return data;
    //   } catch (error: any) {
    //     const message = error.response.data.message;
    //     return false;
    //   }
    // },
    async create(one: Partial<State>): Promise<Boolean> {
      try {
        const axios = await api.raw();
        const { data } = await axios.post(apiUrl + '/order/', one, {
          headers: {
            'Content-Type': 'multipart/form-data',
            Authorization: `JWT ${agentStore.accessToken}`,
          },
        });
      } catch (error: any) {
        return false;
      }
      return true;
    },
    async patch(id: string, one: Partial<State>): Promise<Boolean> {
      try {
        const axios = await api.raw();
        const { data } = await axios.put(apiUrl + '/order/' + id + '/', one, {
          headers: {
            'Content-Type': 'multipart/form-data',
            Authorization: `JWT ${agentStore.accessToken}`,
          },
        });
        return true;
      } catch (error: any) {
        return false;
      }
    },
    async deleteOrder(id: string): Promise<boolean> {
      try {
        const axios = await api.raw();
        await axios.delete(apiUrl + '/order/' + id + '/', {
          headers: {
            'Content-Type': 'multipart/form-data',
            Authorization: `JWT ${agentStore.accessToken}`,
          },
        });
        return true;
      } catch (error: any) {
        const message = error.response.data.message;
        return false;
      }
    },
    localSearch(searchBy: SearchByType) {
      try {
        const results: State[] = [];
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
    selected(state): State | undefined {
      return state.selectedId ? state.all[state.selectedId] : undefined;
    },

    edited(state): State | undefined {
      return state.editedId ? state.all[state.editedId] : undefined;
    },

    list(state): State[] {
      return state.order.map((id) => state.all[id]);
    },

    filteredList(state): State[] {
      if (state.filterQuery != '') return state.filteredIds.map((id) => state.all[id]);
      return this.list;
    },
  },

  persist: true,
});