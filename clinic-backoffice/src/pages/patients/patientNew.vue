<script setup lang="ts">
import {mdiContentSaveAll, mdiAccountMultiplePlus, mdiMedicalBag} from '@mdi/js';
import { ref, onUnmounted } from 'vue';
import { useRouter } from 'vue-router';
import { useAgentStore, usePriceStore, useStyleStore, useDiseasesStore, useRegimentStore, useCityStore, usePatientsStore, useStateStore } from '@/stores';
import type { Patient } from '@/models/patient';
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
import { format } from 'date-fns';
import VueDatePicker from '@vuepic/vue-datepicker';
import FormCheckRadioGroup from '@/vendor/Form/FormCheckRadioGroup.vue';

const agentStore = useAgentStore();
const router = useRouter();
const store = usePatientsStore();
const diseaseStore = useDiseasesStore();
const regimentStore = useRegimentStore();
const styleStore = useStyleStore();
const cityStore = useCityStore();
const statesStore = useStateStore();
const priceStore = usePriceStore();

function formatDate(value) {
  if (value) {
    return format(new Date(value), 'yyyy-MM-dd');
  }
}
const diseases = ref(
  diseaseStore.list.map((disease) => {
    return {
      value: disease.id,
      label: disease.name,
    };
  }),
);
const regiments = ref(
  regimentStore.list.map((regiment) => {
    return {
      value: regiment.id,
      label: regiment.name,
    };
  }),
);
const states = ref(
  statesStore.list.map((regiment) => {
    return {
      value: regiment.id,
      label: regiment.name,
    };
  }),
);
const prices = ref(
  priceStore.list.map((price) => {
    return {
      value: price.id,
      label: price.name,
    };
  }),
);
onUnmounted(() => {
  cityStore.filterQuery = '';
  cityStore.selectedId = undefined;
  cityStore.unsetFilter();
});
const search = () => {
  cityStore.localSearch('state');
  cities.value = cityStore.filteredList.map((city) => {
      return {
        value: city.id,
        label: city.name,
      };
  })
};
const submit = async () => {
  // console.log(patient.value);
  const dateString = formatDate(patient.value.medical_operation_date)?.toString();
  if (dateString !== undefined) {
      patient.value.medical_operation_date = dateString;
  }
  console.log(patient.value);
  const isCreated = await store.create(patient.value, img_1.value, img_2.value);
  if (isCreated) {
    formStatusSubmit();
    setTimeout(function () {
      BackHim();
      router.push('/patients');
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

const cities = ref();
const img_1 = ref(undefined);
const img_2 = ref(undefined);
const formStatusWithHeader = ref(true);
const formStatusCurrent = ref(0);
const formStatusOptions = ['info', 'success', 'danger', 'warning'];
const patient = ref<Patient>({
  name: '',
  phone: '',
  age: '',
  number_of_days: '',
  medical_operation_date: '',
  doctor: '',
  regiment: '',
  disease: '',
  city: '',
  other_diseases: [],
  price: '',
} as unknown as Patient);
</script>

<template>
  <SectionMain>
    <SectionTitleLineWithButton :icon="mdiAccountMultiplePlus" dir="rtl" title="إضافة مريض" main />
    <CardBox dir="rtl" form @submit.prevent="submit">
      <div class="flex">
        <FormField  label="رقم الهاتف" class="ml-3 w-1/2">
          <FormControl
            v-model="patient.phone"
            type="number"
            placeholder="رقم الهاتف"
            :required="true"
          />
        </FormField>
        <FormField label="الاسم الكامل" class="w-1/2">
          <FormControl
            v-model="patient.name"
            type="text"
            placeholder="الاسم الكامل"
            :required="true"
          />
        </FormField>
      </div>
      <div class="flex">
        <FormField dir="rtl" label="العمر" class="ml-3 w-1/2">
            <FormControl
              v-model="patient.age"
              type="number"
              placeholder="العمر "
            />
          </FormField>
        <FormField label="عدد الحصص" class=" w-1/2">
          <FormControl
              v-model="patient.number_of_days"
              type="number"
              placeholder="عدد الحصص"
              :style="{ direction: 'rtl' }"
            />
        </FormField>  
      </div>
      <div class="flex">
          <FormField dir="rtl" label="تاريخ إجراء العملية" class=" ml-3 w-1/2">
            <VueDatePicker placeholder="تاريخ إجراء العملية" v-model="patient.medical_operation_date"  :format="formatt" :dark="styleStore.darkMode" />
          </FormField>
          <FormField dir="rtl" label="الطبيب" class=" w-1/2">
            <FormControl
              v-model="patient.doctor"
              type="text"
              placeholder="الطبيب"
              :style="{ direction: 'rtl' }"
            />
          </FormField>
      </div>
      <div class="flex mb-4">
          <FormField dir="rtl" label="الفوج" class="ml-3 w-1/3">
           <FormControl
              :options="regiments"
              v-model="patient.regiment"
              type="number"
              placeholder="الفوج"
              :style="{ direction: 'rtl' }"
            />
          </FormField> 
          <FormField dir="rtl" label="الفئة" class="ml-3 w-1/3">
           <FormControl
              :options="prices"
              v-model="patient.price"
              type="number"
              placeholder="الفوج"
              :style="{ direction: 'rtl' }"
            />
          </FormField>
          <FormField dir="rtl" label="مرض" class="w-1/3">
            <FormControl
              :options="diseases"
              v-model="patient.disease"
              type="text"
              placeholder="مرض"
            />
          </FormField>
        </div>
        <div class="flex mb-4">
           <FormField dir="rtl" label="الولاية" class="ml-3 w-1/2">
           <FormControl
              :options="states"
              v-model="cityStore.filterQuery"
              placeholder="الولاية"
              @change="search()"
            />
          </FormField>
          <FormField dir="rtl" label="المدينة" class="ml-3 w-1/2">
           <FormControl
              :options="cities"
              v-model="patient.city"
              placeholder="اختر الولاية أولا"
            /> 
          </FormField>
        </div>
        <div dir="rtl" class="w-full h-full p-4 dark:bg-slate-900 bg-slate-100 mb-4 rounded">
          <SectionTitleLineWithButton dir="rtl" :icon="mdiMedicalBag" title="أمراض أخرى"  />
          <FormCheckRadioGroup
            v-model="patient.other_diseases"
            name="sample-checkbox"
            :options="diseases"
          />
        </div>
      <div class="flex justify-between">
          <DropZone
            v-model="img_1"
            class="w-[95%]"
            text="رفع صورة رقم 1"
          />
          <DropZone
            v-model="img_2"
            class="w-[95%]"
            text="رفع صورة رقم 2"
          />
        </div>
      <BaseDivider />

      <BaseButtons class="justify-end">
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