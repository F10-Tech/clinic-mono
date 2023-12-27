<script setup lang="ts">
import { ref } from 'vue';
import { useOrderStore, useAgentStore, useStyleStore } from '@/stores';
import { useRoute, useRouter } from 'vue-router';
import type { Order } from '@/models/order';
import SectionMain from '@/vendor/Section/SectionMain.vue';
import CardBox from '@/vendor/CardBox/CardBox.vue';
import FormField from '@/vendor/Form/FormField.vue';
import FormControl from '@/vendor/Form/FormControl.vue';
import BaseDivider from '@/vendor/Base/BaseDivider.vue';
import BaseButton from '@/vendor/Base/BaseButton.vue';
import BaseButtons from '@/vendor/Base/BaseButtons.vue';
import CardBoxModal from '@/vendor/CardBox/CardBoxModal.vue';
import SectionTitleLineWithButton from '@/vendor/Section/SectionTitleLineWithButton.vue';
import NotificationBar from '@/vendor/NotificationBar/NotificationBar.vue';
import VueDatePicker from '@vuepic/vue-datepicker';

const styleStore = useStyleStore();
const store = useOrderStore();
const agentstore = useAgentStore();

const route = useRoute();
const router = useRouter();
const form = ref(null);
const modalActive = ref(false);

store.editedId = route.params.id.toString();
const OrderData = ref<Order>({
  customer: store.edited?.customer,
  price: store.edited?.price,
  location: store.edited?.location,
  scheduled: store.edited?.scheduled,
  state: store.edited?.state,
} as unknown as Order);

const states = [
  { value: 'INPROGRESS', label: 'INPROGRESS' },
  { value: 'PENDING', label: 'PENDING' },
  { value: 'REJECTED', label: 'REJECTED' },
  { value: 'CANCELLED', label: 'CANCELLED' },
  { value: 'COMPLETED', label: 'COMPLETED' },
];
const locations = [{ value: 'El Oued', label: 'El Oued' }];

const deleteOrder = async () => {
  const isDeleted = await store.deleteOrder(store.editedId!);
  if (isDeleted) {
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

const submit = async () => {
  const isUpdated = await store.patch(store.editedId!, OrderData.value);

  if (isUpdated) {
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
    <CardBoxModal
      v-model="modalActive"
      title="Please confirm the delete"
      button-label="Delete"
      button-cancel-label="Cancel"
      button="danger"
      has-cancel
      @confirm="deleteOrder"
    />
    <CardBox form @submit.prevent="submit">
      <div class="flex">
        <FormField label="First Name" class="mr-3 w-2/5">
          <FormControl v-model="OrderData.customer.first_name" :disabled="true" />
        </FormField>
        <FormField label="Last Name" class="mr-3 w-3/5">
          <FormControl v-model="OrderData.customer.last_name" :disabled="true" />
        </FormField>
      </div>

      <FormField label="Price">
        <FormControl v-model="OrderData.price" type="number" placeholder="price" />
      </FormField>
      <FormField label="Location">
        <FormControl v-model="OrderData.location" :options="locations" />
      </FormField>

      <div class="flex">
        <FormField label="Scheduled" class="mr-3 w-2/5">
          <VueDatePicker v-model="OrderData.scheduled" :dark="styleStore.darkMode" />
        </FormField>

        <FormField label="State" class="w-3/5">
          <FormControl v-model="OrderData.state" :options="states" />
        </FormField>
      </div>

      <BaseDivider />
      <BaseButtons class="flex justify-between">
        <div>
          <BaseButton color="danger" label="Delete" @click="modalActive = true" />
          <BaseButton type="submit" color="success" label="Submit" @click="submit" />
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
