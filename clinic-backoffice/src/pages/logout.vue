<script setup lang="ts">
import { onBeforeMount } from 'vue';
import { useRouter } from 'vue-router';

import {
  useAgentStore,
  useOrderStore,
  useServicesStore,
  useSubServicesStore,
  useMainStore,
} from '@/stores';

const mainStore = useMainStore();
const agentStore = useAgentStore();
const orderstore = useOrderStore();
const servicestore = useServicesStore();
const subservicestore = useSubServicesStore();

const router = useRouter();

onBeforeMount(() => {
  agentStore.logout();
  mainStore.$reset();
  orderstore.$reset();
  servicestore.$reset();
  subservicestore.$reset();

  router.push({ name: 'login' });
});
</script>
