<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useAgentStore, useServicesStore } from '@/stores';
import type { Service } from '@/models/service';
import SectionMain from '@/vendor/Section/SectionMain.vue';
import CardBox from '@/vendor/CardBox/CardBox.vue';
import FormField from '@/vendor/Form/FormField.vue';
import FormControl from '@/vendor/Form/FormControl.vue';
import BaseDivider from '@/vendor/Base/BaseDivider.vue';
import BaseButton from '@/vendor/Base/BaseButton.vue';
import BaseButtons from '@/vendor/Base/BaseButtons.vue';
import NotificationBar from '@/vendor/NotificationBar/NotificationBar.vue';
import DropZone from '@/components/Base/DropZone.vue';
import SectionTitleLineWithButton from '@/vendor/Section/SectionTitleLineWithButton.vue';

const agentStore = useAgentStore();
const store = useServicesStore();
const router = useRouter();

const image_light = ref(undefined);
const image_dark = ref(undefined);
const service = ref<Service>({} as unknown as Service);

const submit = async () => {
  const isCreated = await store.create(service.value, image_dark.value, image_light.value);
  if (isCreated) {
    formStatusSubmit();
    setTimeout(function () {
      BackHim();
      router.push('/services');
    }, agentStore.timeToKill);
  } else {
    formStatusCurrent.value = 2;
    setTimeout(function () {
      BackHim();
    }, agentStore.timeToKill);
  }
};
const BackHim = () => {
  formStatusCurrent.value = 0;
};

const formStatusWithHeader = ref(true);

const formStatusCurrent = ref(0);

const formStatusOptions = ['info', 'success', 'danger', 'warning'];

const formStatusSubmit = () => {
  formStatusCurrent.value = formStatusOptions[formStatusCurrent.value + 1]
    ? formStatusCurrent.value + 1
    : 0;
};
</script>

<template>
  <SectionMain>
    <SectionTitleLineWithButton title="Create Service" main />
    <CardBox form @submit.prevent="submit">
      <div class="flex">
        <FormField label="English Name" class="mr-3 w-2/5">
          <FormControl
            v-model="service.name_EN"
            type="text"
            placeholder="Name in English"
            :required="true"
          />
        </FormField>
        <FormField label="English Desciption" class="w-3/5">
          <FormControl
            v-model="service.description_EN"
            type="text"
            placeholder="Description in English"
            :required="true"
          />
        </FormField>
      </div>
      <div class="flex">
        <FormField label="French Name" class="mr-3 w-2/5">
          <FormControl v-model="service.name_FR" type="text" placeholder="Nom en français" />
        </FormField>
        <FormField label="French Desciption" class="w-3/5">
          <FormControl
            v-model="service.description_FR"
            type="text"
            placeholder="Description en French"
          />
        </FormField>
      </div>
      <div class="flex">
        <FormField label="Arabic Name" class="mr-3 w-2/5">
          <FormControl
            v-model="service.name_AR"
            type="text"
            placeholder="الاسم بالعربية"
            :style="{ direction: 'rtl' }"
          />
        </FormField>
        <FormField label="Arabic Desciption" class="w-3/5">
          <FormControl
            v-model="service.description_AR"
            type="text"
            placeholder="الوصف بالعربية"
            :style="{ direction: 'rtl' }"
          />
        </FormField>
      </div>

      <div class="flex justify-between">
        <DropZone v-model="image_light" class="w-[95%]" text="Drop light image here" />
        <DropZone v-model="image_dark" class="w-[95%]" text="Drop dark image here" />
      </div>

      <BaseDivider />

      <BaseButtons class="justify-end">
        <BaseButton type="submit" color="info" label="Submit" @click="submit" />
      </BaseButtons>
    </CardBox>
    <NotificationBar
      v-if="formStatusCurrent"
      :color="formStatusOptions[formStatusCurrent]"
      :is-placed-with-header="formStatusWithHeader"
      class="animate-fade-left w-96 right-10 top-20 fixed"
    >
      <span
        ><b class="capitalize">{{ formStatusOptions[formStatusCurrent] }}</b></span
      >
    </NotificationBar>
  </SectionMain>
</template>
