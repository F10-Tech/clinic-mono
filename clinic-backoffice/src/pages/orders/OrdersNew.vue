<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';

import { useOrderStore, useSubServicesStore, useAgentStore, useStyleStore } from '@/stores';
import type { Order } from '@/models';
import SectionMain from '@/vendor/Section/SectionMain.vue';
import CardBox from '@/vendor/CardBox/CardBox.vue';
import FormField from '@/vendor/Form/FormField.vue';
import FormControl from '@/vendor/Form/FormControl.vue';
import BaseDivider from '@/vendor/Base/BaseDivider.vue';
import BaseButton from '@/vendor/Base/BaseButton.vue';
import BaseButtons from '@/vendor/Base/BaseButtons.vue';
import SectionTitleLineWithButton from '@/vendor/Section/SectionTitleLineWithButton.vue';
import NotificationBar from '@/vendor/NotificationBar/NotificationBar.vue';
import VueDatePicker from '@vuepic/vue-datepicker';

const styleStore = useStyleStore();
const store = useOrderStore();
const agentstore = useAgentStore();
const subserviceStore = useSubServicesStore();
const router = useRouter();

const order = ref<Partial<Order>>({} as unknown as Order);

const locations = [{ value: 'El Oued', label: 'El Oued' }];
const subservices = ref(
  subserviceStore.list.map((subservice) => {
    return {
      value: subservice.id,
      label: subservice.name_EN,
    };
  }),
);
const submit = async () => {
  const isCreated = await store.create(order.value);
  if (isCreated) {
    formStatusSubmit();
    setTimeout(function () {
      BackHim();
      router.push('/orders');
    }, agentstore.timeToKill);
  } else {
    formStatusCurrent.value = 2;
    setTimeout(function () {
      BackHim();
    }, agentstore.timeToKill);
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
    <SectionTitleLineWithButton title="Order Profile" main />

    <CardBox form @submit.prevent="submit">
      <FormField label="Subservice">
        <FormControl v-model="order.subservice" :options="subservices" />
      </FormField>
      <FormField label="Price">
        <FormControl v-model="order.price" type="number" placeholder="price" />
      </FormField>
      <FormField label="Location">
        <FormControl v-model="order.location" :options="locations" />
      </FormField>

      <FormField label="Scheduled">
        <VueDatePicker
          v-model="order.scheduled"
          :dark="styleStore.darkMode"
          placeholder="Select Date"
        />
      </FormField>

      <BaseDivider />
      <BaseButtons class="flex justify-between">
        <div>
          <BaseButton type="submit" color="success" label="Create" @click="submit" />
        </div>
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

<style lang="scss">
:root {
  --dp-input-padding: 10px 30px 12px 12px;
}
@import '@vuepic/vue-datepicker/dist/main.css';

.dp__theme_dark {
  --dp-background-color: #1e293b;
  --dp-text-color: #ffffff;
  --dp-hover-color: #484848;
  --dp-hover-text-color: #ffffff;
  --dp-hover-icon-color: #959595;
  --dp-primary-color: #005cb2;
  --dp-primary-text-color: #ffffff;
  --dp-secondary-color: #a9a9a9;
  --dp-border-color: #374151;
  --dp-menu-border-color: #2d2d2d;
  --dp-border-color-hover: #374151;
  --dp-disabled-color: #4b5563;
  --dp-scroll-bar-background: #212121;
  --dp-scroll-bar-color: #484848;
  --dp-success-color: #00701a;
  --dp-success-color-disabled: #428f59;
  --dp-icon-color: #959595;
  --dp-danger-color: #e53935;
  --dp-highlight-color: rgb(0 92 178 / 20%);
}

.dp__theme_light {
  --dp-background-color: #ffffff;
  --dp-text-color: #212121;
  --dp-hover-color: #f3f3f3;
  --dp-hover-text-color: #212121;
  --dp-hover-icon-color: #959595;
  --dp-primary-color: #1976d2;
  --dp-primary-text-color: #f8f5f5;
  --dp-secondary-color: #c0c4cc;
  --dp-border-color: #374151;
  --dp-menu-border-color: #ddd;
  --dp-border-color-hover: #374151;
  --dp-disabled-color: #f3f4f6;
  --dp-scroll-bar-background: #f3f3f3;
  --dp-scroll-bar-color: #959595;
  --dp-success-color: #00701a;
  --dp-success-color-disabled: #a3d9b1;
  --dp-icon-color: #959595;
  --dp-danger-color: #ff6f60;
  --dp-highlight-color: rgba(25, 118, 210, 0.1);
}
</style>
