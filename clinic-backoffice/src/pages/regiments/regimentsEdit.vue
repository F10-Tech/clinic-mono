<script setup lang="ts">
import { LoopingRhombusesSpinner } from 'epic-spinners';
import { ref, onUnmounted, onBeforeMount } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useRegimentStore, useAgentStore, useDaysStore } from '@/stores';
import type { Regiment } from '@/models';
import SectionMain from '@/vendor/Section/SectionMain.vue';
import CardBox from '@/vendor/CardBox/CardBox.vue';
import FormField from '@/vendor/Form/FormField.vue';
import FormControl from '@/vendor/Form/FormControl.vue';
import FormCheckRadioGroup from '@/vendor/Form/FormCheckRadioGroup.vue';
import BaseDivider from '@/vendor/Base/BaseDivider.vue';
import BaseButton from '@/vendor/Base/BaseButton.vue';
import BaseButtons from '@/vendor/Base/BaseButtons.vue';
import CardBoxModal from '@/vendor/CardBox/CardBoxModal.vue';
import SectionTitleLineWithButton from '@/vendor/Section/SectionTitleLineWithButton.vue';
import NotificationBar from '@/vendor/NotificationBar/NotificationBar.vue';

const store = useRegimentStore();
const agent = useAgentStore();
const daysStore = useDaysStore();

const formStatusSubmit = () => {
  formStatusCurrent.value = formStatusOptions[formStatusCurrent.value + 1]
    ? formStatusCurrent.value + 1
    : 0;
};
const deleteRegiment = async () => {
  const isDeleted = await store.delete(store.editedId!);
  if (isDeleted) {
    formStatusSubmit();
    setTimeout(function () {
      BackHim();
      router.push('/regiments');
    }, agent.timeToKill);
  } else {
    formStatusCurrent.value = 2;
    setTimeout(function () {
      BackHim();
    }, agent.timeToKill);
  }
};
const submit = async () => {
  
  const isUpdated = await store.patch(
    store.editedId!,
    regiment.value,
  );
  if (isUpdated) {
    formStatusSubmit();
    setTimeout(function () {
      BackHim();
      router.push('/regiments');
    }, agent.timeToKill);
  } else {
    formStatusCurrent.value = 2;
    setTimeout(function () {
      BackHim();
    }, agent.timeToKill);
  }
};
const BackHim = () => {
  formStatusCurrent.value = 0;
};
onUnmounted(() => {
  store.filterQuery = '';
  store.editedId = undefined;
  // cityStore.unsetFilter();
});

const days = ref(
  daysStore.list.map((day) => {
    return {
      value: day.id,
      label: day.name,
    };
  }),
);

const route = useRoute();
const router = useRouter();

const modalActive = ref(false);
const isLoading = ref(true);
const periods = [
  { value: 'MORNING', label: 'صباحية' },
  { value: 'EVENING', label: 'مسائية' },
] 
store.editedId = route.params.id.toString();
const regiment = ref<Regiment>({
  name: store.edited?.name,
  id: store.edited?.id,
  days: store.edited?.days,
  period: store.edited?.period,
} as unknown as Regiment);
isLoading.value = false;
const formStatusWithHeader = ref(true);
const formStatusCurrent = ref(0);
const formStatusOptions = ['info', 'success', 'danger', 'warning'];
</script>

<template >
  <div v-if="isLoading" class="flex justify-center items-center h-screen">
    <looping-rhombuses-spinner :animation-duration="1500" :rhombus-size="20" color="#fff" />
  </div>

  <div v-else>
    <SectionMain  v-if="regiment">
      <SectionTitleLineWithButton dir="rtl" :title="regiment.name" main />
      <CardBoxModal
        v-model="modalActive"
        title="Please confirm the delete"
        button-label="Delete"
        button-cancel-label="Cancel"
        button="danger"
        has-cancel
        @confirm="deleteRegiment"
      
      />
      <CardBox dir="rtl" form @submit.prevent="submit">
        <div class="flex w-full">
          <FormField  label="اسم الفوج " class=" ml-3 w-1/2" >
            <FormControl
              v-model="regiment.name"
              type="text"
              placeholder=" اسم الفوج "
              :style="{ direction: 'rtl' }"
            />
          </FormField>
          <FormField  label="الفترة " class="w-1/2" >
            <FormControl
              v-model="regiment.period"
              type="text"
              placeholder="رقم الهاتف "
              :options="periods"
              :style="{ direction: 'rtl' }"
            />
          </FormField>
        </div>
        <div  class="w-full h-full p-4 bg-slate-900 mb-4 rounded">
          <div class=" text-2xl mb-4 font-bold "> الأيام :</div>
          <FormCheckRadioGroup
            v-model="regiment.days"
            name="sample-checkbox"
            :options="days"
          />
        </div>
        <BaseDivider />

        <BaseButtons class="flex justify-between">
          
          <BaseButton class="mr-0 lg:ml-4  lg:w-[77%] w-full" type="submit" color="success" label="حفظ" @click="submit" />
          <BaseButton class=" lg:w-[20%] w-full" color="danger" label="حذف" @click="modalActive = true" />
        </BaseButtons>
      </CardBox>
      <NotificationBar
        v-if="formStatusCurrent"
        :color="formStatusOptions[formStatusCurrent]"
        :is-placed-with-header="formStatusWithHeader"
        class="animate-fade-left w-96 right-10 top-20 fixed"
      >
        <span>
          <b class="capitalize">{{ formStatusOptions[formStatusCurrent] }}</b>
        </span>
      </NotificationBar>
    </SectionMain>
  </div>
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
