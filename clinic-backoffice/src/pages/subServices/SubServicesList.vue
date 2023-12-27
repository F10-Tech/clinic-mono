<script setup lang="ts">
import { ref, onBeforeMount } from 'vue';
import { useServicesStore, useSubServicesStore } from '@/stores';
import type { Service } from '@/models/service';
import { mdiClipboardTextMultipleOutline } from '@mdi/js';
import { LoopingRhombusesSpinner } from 'epic-spinners';
import SectionMain from '@/vendor/Section/SectionMain.vue';
import SectionTitleLineWithButton from '@/vendor/Section/SectionTitleLineWithButton.vue';
import BaseButton from '@/vendor/Base/BaseButton.vue';
import SubserviceServiceSection from '@/pages/subServices/_partials/SubserviceServiceSection.vue';

const ServiceStore = useServicesStore();
const store = useSubServicesStore();
const services = ref<Service[]>();
const isLoading = ref(false);

onBeforeMount(async () => {
  isLoading.value = true;
  if (await ServiceStore.fetchAll()) services.value = ServiceStore.list;

  await store.fetchAll();
  isLoading.value = false;
});
</script>

<template>
  <div v-if="isLoading" class="flex justify-center items-center h-screen">
    <looping-rhombuses-spinner :animation-duration="1500" :rhombus-size="20" color="#fff" />
  </div>

  <div v-else>
    <SectionMain>
      <SectionTitleLineWithButton :icon="mdiClipboardTextMultipleOutline" title="Subservices" main>
        <BaseButton
          label="Create Subservice"
          color="contrast"
          :to="{ name: 'subservices.new' }"
          class="font-medium"
        />
      </SectionTitleLineWithButton>

      <div v-for="service in services" :key="service.id" class="mb-4 select-none">
        <div class="border-l-8 rounded bg-[#f1f5f9] dark:bg-[#1e293b]">
          <h2 class="font-bold text-3xl capitalize my-2 ml-2">{{ service.name_EN }}</h2>
        </div>
        <SubserviceServiceSection :serviceId="service.id!" />
      </div>
    </SectionMain>
  </div>
</template>
