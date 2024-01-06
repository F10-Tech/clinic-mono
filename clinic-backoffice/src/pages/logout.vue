<script setup lang="ts">
import { onBeforeMount } from 'vue';
import { useRouter } from 'vue-router';

import {
  useAgentStore,

  useMainStore
} from '@/stores';

const mainStore = useMainStore();
const agentStore = useAgentStore();

const router = useRouter();

onBeforeMount(() => {
  agentStore.logout();
  mainStore.$reset();

  router.push({ name: 'login' });
});
</script>
