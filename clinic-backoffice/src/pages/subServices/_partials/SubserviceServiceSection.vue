<script setup lang="ts">
import { LoopingRhombusesSpinner } from 'epic-spinners';
import { ref, onBeforeMount } from 'vue';
import { useStyleStore, useSubServicesStore } from '@/stores';
import type { Subservice } from '@/models/subservice';
import CardBox from '@/vendor/CardBox/CardBox.vue';
import CardBoxSubService from '@/components/CardBox/CardBoxSubService.vue';

const styleStore = useStyleStore();
const store = useSubServicesStore();
const subServices = ref<Subservice[]>([]);
let numOfProperties = ref(0);
const isLoading = ref(false); // Initially, set loading to false
const props = defineProps({
  serviceId: {
    type: String,
    required: true,
  },
});
onBeforeMount(async () => {
  isLoading.value = true;
  if (await store.fetchByService(props.serviceId)) {
    subServices.value = await store.fetchByService(props.serviceId);
  }
  isLoading.value = false;
});

defineEmits(['submit']);
</script>

<template>
  <CardBox class="h-full">
    <div v-if="isLoading" class="flex justify-center items-center min-h-[19.5rem]">
      <looping-rhombuses-spinner :animation-duration="1500" :rhombus-size="20" color="#fff" />
    </div>

    <div v-else-if="subServices.length > 0">
      <div
        :class="styleStore.darkMode ? 'aside-scrollbars-[slate]' : styleStore.asideScrollbarsStyle"
        class="flex overflow-x-auto overflow-y-hidden"
      >
        <div
          v-for="subService in subServices"
          :key="subService.id"
          class="w-80 mr-2 flex-none mb-2"
        >
          <CardBoxSubService :subService="subService" />
        </div>
      </div>
    </div>
    <div v-else class="flex justify-center items-center min-h-[19.5rem]">
      <p class="text-xl text-gray-400">No subservices found</p>
    </div>
  </CardBox>
</template>

<style>
.hide-scroll-bar {
  -ms-overflow-style: none;
  scrollbar-width: none;
}

.hide-scroll-bar::-webkit-scrollbar {
  display: none;
}
</style>
