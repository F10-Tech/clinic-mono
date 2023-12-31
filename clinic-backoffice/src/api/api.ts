import axios from 'axios';
import { apiUrl } from '../main';
import { useAgentStore } from '../stores/models/agent';

const client = axios.create({ baseURL: apiUrl });
client.defaults.headers.common['Content-Type'] = 'application/json';

export function useApi() {
  const axios = async () => {
    const store = useAgentStore();
    const auth = `JWT ${store.accessToken}`;
    client.defaults.headers.common['Authorization'] = auth;

    return client;
  };

  return { axios };
}

export const abstractApi = (apiUrl: string, name: string) => {
  return () => {
    const { axios } = useApi();
    const url = apiUrl;

    const api = {
      all: async (filters = '') => {
        return (await axios()).get(url + filters);
      },

      one: async (id: string) => {
        const data = (await axios()).get(url + id);
        return (await data).data;
      },
      byservice: async (id: string) => {
        return (await axios()).get(url + id + '/subservice');
      },

      post: async (data: any) => {
        return (await axios()).post(url + 'create/', data);
      },

      patch: async (id: string, data: any) => {
        return (await axios()).patch(url + id + '/update', data);
      },

      put: async (id: number, data: any) => {
        return (await axios()).put(url + '/' + id, data);
      },

      delete: async (id: string) => {
        return (await axios()).delete(url + id + '/delete');
      },

      raw: async () => {
        return await axios();
      },

      getApiUrl: () => {
        return url;
      },
    };

    return { [name]: api };
  };
};
