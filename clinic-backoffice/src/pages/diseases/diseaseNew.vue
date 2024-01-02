<script setup lang="ts">
import {mdiContentSaveAll, mdiDelete, mdiClipboardList, mdiMedicalBag} from '@mdi/js';

import { ref, onUnmounted } from 'vue';
import { useRouter } from 'vue-router';
import { useAgentStore, useDiseasesStore} from '@/stores';
import type { Disease } from '@/models';
import SectionMain from '@/vendor/Section/SectionMain.vue';
import CardBox from '@/vendor/CardBox/CardBox.vue';
import FormField from '@/vendor/Form/FormField.vue';
import FormControl from '@/vendor/Form/FormControl.vue';
import BaseDivider from '@/vendor/Base/BaseDivider.vue';
import BaseButton from '@/vendor/Base/BaseButton.vue';
import BaseButtons from '@/vendor/Base/BaseButtons.vue';
import NotificationBar from '@/vendor/NotificationBar/NotificationBar.vue';
import SectionTitleLineWithButton from '@/vendor/Section/SectionTitleLineWithButton.vue';





const agentStore = useAgentStore();
const router = useRouter();
const store = useDiseasesStore();

const disease = ref<Disease>({} as unknown as Disease);


const submit = async () => {
  const isCreated = await store.create(disease.value);
  if (isCreated) {
    formStatusSubmit();
    setTimeout(function () {
      BackHim();
      router.push('/diseases');
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
const formatt = (date) => {
  const day = date.getDate();
  const month = date.getMonth() + 1;
  const year = date.getFullYear();

  return `${day}/${month}/${year}`;
}
</script>

<template>
  <SectionMain>
    <SectionTitleLineWithButton :icon="mdiMedicalBag" dir="rtl" title="إضافة مرض" main />
    <CardBox dir="rtl" form @submit.prevent="submit">
      <div class="flex">
        <FormField  label=" إسم المرض" class="ml-3 w-full">
          <FormControl
            v-model="disease.name"
            type="text"
            placeholder="إسم المرض"
            :required="true"
          />
        </FormField>
      </div>
      <BaseDivider />

      <BaseButtons dir="rtl" class="justify-end">
        <BaseButton :icon="mdiContentSaveAll" class=" w-full" type="submit" color="success" label="حفظ" @click="submit" />
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