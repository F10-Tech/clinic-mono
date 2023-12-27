<script setup lang="ts">
import { ref, onBeforeMount } from 'vue';
import { mdiClipboardListOutline } from '@mdi/js';
import { LoopingRhombusesSpinner } from 'epic-spinners';

import { useServicesStore } from '@/stores';
import type { Service } from '@/models';
import SectionMain from '@/vendor/Section/SectionMain.vue';
import SectionTitleLineWithButton from '@/vendor/Section/SectionTitleLineWithButton.vue';
import BaseButton from '@/vendor/Base/BaseButton.vue';
import CardBoxService from '@/components/CardBox/CardBoxService.vue';

const store = useServicesStore();
const services = ref<Service[]>();

const isLoading = ref(false);

onBeforeMount(async () => {
  isLoading.value = true;
  if (await store.fetchAll()) {
    services.value = store.list;
  }
  isLoading.value = false;
});
</script>

<template>
  <div v-if="isLoading" class="flex justify-center items-center h-screen">
    <looping-rhombuses-spinner :animation-duration="1500" :rhombus-size="20" color="#fff" />
  </div>

  <div v-else>
    <SectionMain>
      <SectionTitleLineWithButton :icon="mdiClipboardListOutline" title="Services" main>
        <BaseButton
          label="Create Service"
          color="contrast"
          to="/services/new"
          class="font-medium"
        />
      </SectionTitleLineWithButton>
      <div class="grid grid-cols-1 gap-6 lg:grid-cols-3 mb-6">
        <CardBoxService v-for="service in services" :key="service.id" :service="service" />
      </div>
    </SectionMain>
  </div>
</template>
