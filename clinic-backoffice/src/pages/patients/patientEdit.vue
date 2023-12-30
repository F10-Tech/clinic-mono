<script setup lang="ts">
import { LoopingRhombusesSpinner } from 'epic-spinners';
import { ref, onUnmounted,reactive } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { usePatientsStore, useAgentStore, useStyleStore, useDiseasesStore } from '@/stores';
import type { Patient } from '@/models/patient';
import SectionMain from '@/vendor/Section/SectionMain.vue';
import CardBox from '@/vendor/CardBox/CardBox.vue';
import FormField from '@/vendor/Form/FormField.vue';
import FormControl from '@/vendor/Form/FormControl.vue';
import FormCheckRadioGroup from '@/vendor/Form/FormCheckRadioGroup.vue';
import BaseDivider from '@/vendor/Base/BaseDivider.vue';
import BaseButton from '@/vendor/Base/BaseButton.vue';
import BaseButtons from '@/vendor/Base/BaseButtons.vue';
import DropZone from '@/components/Base/DropZone.vue';
import CardBoxModal from '@/vendor/CardBox/CardBoxModal.vue';
import SectionTitleLineWithButton from '@/vendor/Section/SectionTitleLineWithButton.vue';
import NotificationBar from '@/vendor/NotificationBar/NotificationBar.vue';
import { format } from 'date-fns';
import VueDatePicker from '@vuepic/vue-datepicker';



function formatDate(value) {
  if (value) {
    return format(new Date(value), 'yyyy-MM-dd');
  }
}


const store = usePatientsStore();
const agent = useAgentStore();
const styleStore = useStyleStore();
const diseaseStore = useDiseasesStore();
const img_1 = ref<File | undefined>(undefined);
const img_2 = ref<File | undefined>(undefined);
const diseases = ref(
  diseaseStore.list.map((disease) => {
    return {
      value: disease.id,
      label: disease.name,
    };
  }),
);

const route = useRoute();
const router = useRouter();
const modalActive = ref(false);
const image_light = ref<File | undefined>(undefined);
const image_dark = ref<File | undefined>(undefined);
const isLoading = ref(true);

store.editedId = route.params.id.toString();
const patient = ref<Patient>({
  name: store.edited?.name,
  phone: store.edited?.phone,
  age: store.edited?.age,
  number_of_days: store.edited?.number_of_days,
  disease: store.edited?.disease?.id,
  other_diseases: store.edited?.other_diseases,
  img_1: store.edited?.img_1,
  img_2: store.edited?.img_2,
  presence: store.edited?.presence,
  medical_operation_date: store.edited?.medical_operation_date,
  doctor: store.edited?.doctor
} as unknown as Patient);
isLoading.value = false;
onUnmounted(() => {
  store.editedId = undefined;
});
// const deleteService = async () => {
//   const isDeleted = await store.deleteService(store.editedId!);
//   if (isDeleted) {
//     formStatusSubmit();
//     setTimeout(function () {
//       BackHim();
//       router.push('/services');
//     }, agent.timeToKill);
//   } else {
//     formStatusCurrent.value = 2;
//     setTimeout(function () {
//       BackHim();
//     }, agent.timeToKill);
//   }
// };
const submit = async () => {
  console.log(img_1);
  // patient.value.medical_operation_date = formatDate(patient.value.medical_operation_date);
  const isUpdated = await store.patch(
    store.editedId!,
    patient.value,
    img_1.value,
    img_2.value,
  );
  if (isUpdated) {
    formStatusSubmit();
    setTimeout(function () {
      BackHim();
      router.push('/patients');
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

<template >
  <div v-if="isLoading" class="flex justify-center items-center h-screen">
    <looping-rhombuses-spinner :animation-duration="1500" :rhombus-size="20" color="#fff" />
  </div>

  <div v-else>
    <SectionMain  v-if="patient">
      <SectionTitleLineWithButton dir="rtl" title="الملف الشخصي للمريض" main />
      <CardBoxModal
        v-model="modalActive"
        title="Please confirm the delete"
        button-label="Delete"
        button-cancel-label="Cancel"
        button="danger"
        has-cancel
      />
        <!-- @confirm="deleteService" -->

      <CardBox form @submit.prevent="submit">
       
        <div class="flex">
          <FormField dir="rtl" label="رقم الهاتف" class=" mr-3 w-1/2">
            <FormControl
              v-model="patient.phone"
              type="text"
              placeholder="رقم الهاتف "
              :style="{ direction: 'rtl' }"
            />
          </FormField>
          <FormField dir="rtl" label="الاسم" class=" w-1/2">
            <FormControl
              v-model="patient.name"
              type="text"
              placeholder="الاسم بالعربية"
              :style="{ direction: 'rtl' }"
            />
          </FormField>
        </div>
        <div class="flex">
          <FormField dir="rtl" label="عدد الحصص" class="mr-3 w-1/2">
            <FormControl
              v-model="patient.number_of_days"
              type="number"
              placeholder="عدد الحصص"
              :style="{ direction: 'rtl' }"
            />
          </FormField>

          <FormField dir="rtl" label="العمر" class=" w-1/2">
            <FormControl
              v-model="patient.age"
              type="number"
              placeholder="العمر "
            />
          </FormField>
        </div>
        <div class="flex">
          <FormField dir="rtl" label="تاريخ إجراء العملية" class=" mr-3 w-1/2">
            <VueDatePicker v-model="patient.medical_operation_date" :format="formatt" :dark="styleStore.darkMode" />
          </FormField>
          <FormField dir="rtl" label="الطبيب" class=" w-1/2">
            <FormControl
              v-model="patient.doctor"
              type="text"
              placeholder="المرض الأساسي "
              :style="{ direction: 'rtl' }"
            />
          </FormField>
          
        </div>
        <div class="flex mb-4">
          <!-- <FormField dir="rtl" label="أمراض أخرى" class="mr-3 w-1/2">
            <FormControl
              v-model="patient.other_diseases"
              :options="diseases"
              type="number"
              placeholder="أمراض أخرى"
              :style="{ direction: 'rtl' }"
            />
          </FormField> -->

          <FormField dir="rtl" label="مرض" class=" w-full">
            <FormControl
              v-model="patient.disease"
              :options="diseases"
              type="text"
              placeholder="مرض"
            />
          </FormField>
        </div>
        <div dir="rtl" class="w-full h-full p-4 bg-slate-900 mb-4 rounded">
          <div class=" text-2xl mb-4 font-bold "> أمراض اخرى:</div>
          <!-- {{patient.other_diseases}} -->
          <FormCheckRadioGroup
            v-model="patient.other_diseases"
            name="sample-checkbox"
            :options="diseases"
          />
        </div>
        <div dir="rtl" class="w-full h-full p-4 bg-slate-900 mb-4 rounded">
          <div class=" text-2xl mb-4 font-bold "> الحضور:</div>
          <div class=" ml-4 mb-2 text-xl flex" v-for="one in patient.presence" :key="one.id">
              - <div v-if="one.day == 'Thursday' " class="mx-2">
                      الخميس 
              </div>
              <div v-if="one.day == 'Friday' " class="mx-2">
                      الجمعة 
              </div>
              <div v-if="one.day == 'Saturday' " class="mx-2">
                      السبت 
              </div>
              <div v-if="one.day == 'Sunday' " class="mx-2">
                      الأحد 
              </div>
              <div v-if="one.day == 'Monday' " class="mx-2">
                      الإثنين 
              </div>
              <div v-if="one.day == 'Tuesday' " class="mx-2">
                      الثلاثاء 
              </div>
              <div v-if="one.day == 'Wednesday' " class="mx-2">
                      اللإربعاء 
              </div>

               -- {{ formatDate(one.created_at) }}
          </div>
        </div>

        <div class="flex justify-between">
          <DropZone
            v-model="img_1"
            :preview="patient.img_1"
            class="w-[95%]"
            text="رفع صورة رقم 1"
            mode="edit"
          />
          <DropZone
            v-model="img_2"
            :preview="patient.img_2"
            class="w-[95%]"
            text="رفع صورة رقم 2"
            mode="edit"
          />
        </div>
        <BaseDivider />

        <BaseButtons class="flex justify-between">
          <!-- <FormCheckRadioGroup
            v-model="service.is_active"
            type="switch"
            name="notifications-switch"
            :options="{ outline: 'Active' }"
          /> -->
          <div>
            <BaseButton color="danger" label="حذف" @click="modalActive = true" />
            <BaseButton type="submit" color="success" label="حفظ" @click="submit" />
          </div>
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