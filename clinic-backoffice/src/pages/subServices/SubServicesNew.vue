<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';

import { useAgentStore, useSubServicesStore, useServicesStore } from '@/stores';
import type { Subservice } from '@/models';
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

const agentSrore = useAgentStore();
const store = useSubServicesStore();
const servicestore = useServicesStore();
const router = useRouter();

const services = ref(
  servicestore.list.map((service) => {
    return {
      value: service.id,
      label: service.name_EN,
    };
  }),
);
const image_light = ref(undefined);
const image_dark = ref(undefined);
const subservice = ref<Subservice>({} as unknown as Subservice);

const submit = async () => {
  const isCreated = await store.create(subservice.value, image_dark.value, image_light.value);
  if (isCreated) {
    formStatusSubmit();
    setTimeout(function () {
      BackHim();
      router.push('/subservices');
    }, agentSrore.timeToKill);
  } else {
    formStatusCurrent.value = 2;
    setTimeout(function () {
      BackHim();
    }, agentSrore.timeToKill);
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
    <SectionTitleLineWithButton title="Create Subservice" main />
    <CardBox form @submit.prevent="submit">
      <FormField label="Dropdown">
        <FormControl v-model="subservice.service" :options="services" />
      </FormField>
      <div class="flex">
        <FormField label="English Name" class="mr-3 w-2/5">
          <FormControl
            v-model="subservice.name_EN"
            type="text"
            placeholder="Name in English"
            :required="true"
          />
        </FormField>
        <FormField label="English Desciption" class="w-3/5">
          <FormControl
            v-model="subservice.description_EN"
            type="text"
            placeholder="Description in English"
          />
        </FormField>
      </div>
      <div class="flex">
        <FormField label="French Name" class="mr-3 w-2/5">
          <FormControl v-model="subservice.name_FR" type="text" placeholder="Nom en français" />
        </FormField>
        <FormField label="French Desciption" class="w-3/5">
          <FormControl
            v-model="subservice.description_FR"
            type="text"
            placeholder="Description en French"
          />
        </FormField>
      </div>
      <div class="flex">
        <FormField label="Arabic Name" class="mr-3 w-2/5">
          <FormControl
            v-model="subservice.name_AR"
            type="text"
            placeholder="الاسم بالعربية"
            :style="{ direction: 'rtl' }"
          />
        </FormField>
        <FormField label="Arabic Desciption" class="w-3/5">
          <FormControl
            v-model="subservice.description_AR"
            type="text"
            placeholder="الوصف بالعربية"
            :style="{ direction: 'rtl' }"
          />
        </FormField>
      </div>
      <FormField label="Minimum Price">
        <FormControl v-model="subservice.min_price" type="number" placeholder="Price" />
      </FormField>

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
