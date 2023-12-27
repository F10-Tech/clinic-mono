<script setup lang="ts">
import { mdiPencil } from '@mdi/js';
import CardBox from '@/vendor/CardBox/CardBox.vue';
import BaseButton from '@/vendor/Base/BaseButton.vue';
import BaseImg from '@/components/Base/BaseImg.vue';

const props = defineProps({
  subService: {
    type: Object,
    required: true,
  },
});
</script>

<template>
  <CardBox>
    <div class="flex flex-col justify-between h-full">
      <div class="flex justify-evenly h-32 mb-2">
        <div class="flex w-[48%] mr-1 bg-[#000814] h-full rounded-xl">
          <BaseImg :src="subService.image_light" alt="" class="h-3/4 m-auto" />
        </div>
        <div class="flex w-[48%] ml-1 bg-[#edf2f4] h-full rounded-xl">
          <BaseImg :src="subService.image_dark" alt="" class="h-3/4 m-auto" />
        </div>
      </div>

      <div>
        <div class="flex justify-between mx-2">
          <h1 class="text-xl leading-tight font-semibold">
            {{ subService.name_EN }}
          </h1>
          <h1 class="text-xl leading-tight font-semibold">
            {{ subService.description_EN }}
          </h1>
        </div>
        <div class="flex justify-between mx-2">
          <h1 class="text-xl leading-tight font-semibold">
            {{ subService.name_FR }}
          </h1>
          <h1 class="text-xl leading-tight font-semibold">
            {{ subService.description_FR }}
          </h1>
        </div>
        <div class="flex justify-between mx-2">
          <h1 class="text-xl leading-tight font-semibold">
            {{ subService.name_AR }}
          </h1>
          <h1 class="text-xl leading-tight font-semibold">
            {{ subService.description_AR }}
          </h1>
        </div>
      </div>
      <div class="flex justify-center mt-4">
        <BaseButton
          label="Edit"
          :icon="mdiPencil"
          icon-w="w-4"
          icon-h="h-4"
          color="info"
          small
          :to="{ name: 'subservices.edit', params: { id: subService.id } }"
          class="w-full mx-2"
        />
      </div>
    </div>
  </CardBox>
</template>
