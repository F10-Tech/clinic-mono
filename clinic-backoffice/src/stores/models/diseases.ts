import { defineStore } from 'pinia';
import { useDiseasesApi } from '../../api/diseases';
import { useAgentStore } from './agent';
import { convertToDict, type baseType } from './_helpers';
import { apiUrl } from '../../main';
import type { Disease } from '../../models';

const agentStore = useAgentStore();
const { diseasesApi: api } = useDiseasesApi();
type SearchByType = 'name';

export const useDiseasesStore = defineStore('disease', {
  state: (): baseType<Disease> => ({
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
    async create(
      one: Disease,
    ): Promise<Boolean> {
      try {
        const { data } = await api.post(one);
        return true;
      } catch (error: any) {
        return false;
      }
      return true;
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
        const results: Disease[] = [];
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
    selected(state): Disease | undefined {
      return state.selectedId ? state.all[state.selectedId] : undefined;
    },

    edited(state): Disease | undefined {
      return state.editedId ? state.all[state.editedId] : undefined;
    },

    list(state): Disease[] {
      return state.order.map((id) => state.all[id]);
    },

    filteredList(state): Disease[] {
      if (state.filterQuery != '') return state.filteredIds.map((id) => state.all[id]);
      return this.list;
    },
  },

  persist: true,
});
