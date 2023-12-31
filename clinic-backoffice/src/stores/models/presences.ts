import { defineStore } from 'pinia';
import { usePresencesApi } from '../../api/presences';
import { useAgentStore } from './agent';
import { convertToDict, type baseType } from './_helpers';
import { apiUrl } from '../../main';
import type { Presence } from '../../models';

const agentStore = useAgentStore();
const { presencesApi: api } = usePresencesApi();
type SearchByType = 'day';

export const usePresenceStore = defineStore('presence', {
  state: (): baseType<Presence> => ({
    all: {},
    order: [],
    filteredIds: [],
    filterQuery: '',
    selectedId: undefined,
    editedId: undefined,
  }),

  actions: {
    async fetchAll(query: String): Promise<Boolean> {
      try {
        const axios = await api.raw();
        // const { data } = await axios.get(apiUrl + '/order/one/' + id);
        const { data } = await axios.get(apiUrl + '/patient/presence/' + query );
        console.log(data);
        const { all, order } = convertToDict(data);
        this.all = all;
        this.order = order;
      } catch (error: any) {
        return false;
      }
      return true;
    },
    async create(one: Presence): Promise<Boolean> {
      try {
        const { data } = await api.post(one);
        return true;
      } catch (error: any) {
        return false;
      }
      return true;
    },
    async patch(id: string, one: Partial<Presence>): Promise<Boolean> {
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
    async delete(id: string): Promise<boolean> {
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
        const results: Presence[] = [];
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
    selected(state): Presence | undefined {
      return state.selectedId ? state.all[state.selectedId] : undefined;
    },

    edited(state): Presence | undefined {
      return state.editedId ? state.all[state.editedId] : undefined;
    },

    list(state): Presence[] {
      return state.order.map((id) => state.all[id]);
    },

    filteredList(state): Presence[] {
      if (state.filterQuery != '') return state.filteredIds.map((id) => state.all[id]);
      return this.list;
    },
  },

  persist: true,
});