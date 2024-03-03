import { defineStore } from 'pinia';
import { useDoctorsApi } from '../../api/doctors';
import { useAgentStore } from './agent';
import { convertToDict, type baseType } from './_helpers';
import { apiUrl } from '../../main';
import type { Doctor } from '../../models';

const agentStore = useAgentStore();
const { doctorsApi: api } = useDoctorsApi();
type SearchByType = 'name';

export const useDoctorsStore = defineStore('doctor', {
  state: (): baseType<Doctor> => ({
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
      one: Doctor,
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
        const results: Doctor[] = [];
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
    selected(state): Doctor | undefined {
      return state.selectedId ? state.all[state.selectedId] : undefined;
    },

    edited(state): Doctor | undefined {
      return state.editedId ? state.all[state.editedId] : undefined;
    },

    list(state): Doctor[] {
      return state.order.map((id) => state.all[id]);
    },

    filteredList(state): Doctor[] {
      if (state.filterQuery != '') return state.filteredIds.map((id) => state.all[id]);
      return this.list;
    },
  },

  persist: true,
});
