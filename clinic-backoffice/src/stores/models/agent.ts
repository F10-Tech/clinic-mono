import { defineStore } from 'pinia';
import axios from 'axios';
import { apiUrl } from '../../main';

export const useAgentStore = defineStore('agent', {
  state: () => ({
    username: '',
    firstName: '',
    lastName: '',
    email: '',
    phone: '',
    accessToken: '',
    isLoggedIn: false,
    timeToKill: 2000,
  }),
  actions: {
    async login(username: string, password: string): Promise<Boolean> {
      let tokens: { access: string; refresh: string };
      try {
        const { data, status } = await axios.post(
          apiUrl + '/auth/jwt/create/',
          { username, password },
          { headers: { 'Content-Type': 'application/json' } },
        );

        if (status != 200) throw Error();
        tokens = data;
      } catch {
        throw Error('Incorrect phone or password');
      }
      this.accessToken = tokens.access;

      try {
        const { data, status } = await axios.get(apiUrl + '/auth/users/me/', {
          headers: {
            Authorization: `JWT ${this.accessToken}`,
          },
        });

        if (data.is_staff == true) {
          this.isLoggedIn = true;
          this.setUser(data);
        }
        if (status != 200) throw Error();
        tokens = data;
      } catch {
        throw Error('Error while fetching user data');
      }

      return true;
    },
    async logout(): Promise<Boolean> {
      this.$reset();
      this.isLoggedIn = false;
      return true;
    },
    // async fetchUser(): Promise<Boolean> {
    //     const store = useMainStore();
    //     const { agentsApi: api } = useAgentsApi();
    //     try {
    //         const { data } = await api.me();
    //         this.setUser({ ...data, ...data.profile });
    //     } catch {
    //         throw Error('Inactive user');
    //     }
    //     return true;
    // },
    setUser(payload: Omit<AgentType, 'accessToken'>) {
      if (payload.username) {
        this.username = payload.username;
      }
      if (payload.first_name) {
        this.firstName = payload.first_name;
      }
      if (payload.last_name) {
        this.lastName = payload.last_name;
      }
      if (payload.email) {
        this.email = payload.email;
      }
      if (payload.phone) {
        this.phone = payload.phone;
      }
    },
  },

  persist: true,
});
type AgentType = {
  email: string;
  first_name: string;
  last_name: string;
  phone: string;
  username: string;
  accessToken: string;
  isLoggedIn: boolean;
};
