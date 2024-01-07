<script setup lang="ts">
import {mdiContentSaveAll, mdiDelete, mdiClipboardList, mdiMedicalBag, mdiBookEdit, mdiPrinter} from '@mdi/js';
import { LoopingRhombusesSpinner } from 'epic-spinners';
import { ref, onUnmounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { usePatientsStore, usePriceStore, useCityStore ,useStateStore,  useAgentStore, useStyleStore, useDiseasesStore, useRegimentStore } from '@/stores';
import type { Patient } from '@/models/patient';
import SectionMain from '@/vendor/Section/SectionMain.vue';
import PillTag from '@/vendor/PillTag/PillTag.vue';
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

const store = usePatientsStore();
const agent = useAgentStore();
const styleStore = useStyleStore();
const diseaseStore = useDiseasesStore();
const regimentStore = useRegimentStore();
const statesStore = useStateStore();
const cityStore = useCityStore();
const priceStore = usePriceStore();

const formatt = (date) => {
  const day = date.getDate();
  const month = date.getMonth() + 1;
  const year = date.getFullYear();
  return `${day}/${month}/${year}`;
}
function formatDate(value) {
  if (value) {
    return format(new Date(value), 'yyyy-MM-dd');
  }
}
const states = ref(
  statesStore.list.map((state) => {
    return {
      value: state.id,
      label: state.name,
    };
  }),
);
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
const cities = ref(
  cityStore.filteredList.map((city) => {
      return {
        value: city.id,
        label: city.name,
      };
  })
);
const prices = ref(
  priceStore.list.map((price) => {
    return {
      value: price.id,
      label: price.name,
    };
  }),
);
const search = () => {
  cityStore.localSearch('state');
  cities.value = cityStore.filteredList.map((city) => {
      return {
        value: city.id,
        label: city.name,
      };
  })
};
const deletePatient = async () => {
  const isDeleted = await store.deletePatient(store.editedId!);
  if (isDeleted) {
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
const submit = async () => {
  const dateString = formatDate(patient.value.medical_operation_date)?.toString();
  if (dateString !== undefined) {
    let medicalOperationDate: string | null;

      if (patient.value.surgery) {
        medicalOperationDate = dateString;
      } else {
        medicalOperationDate = null;
      }
      patient.value.medical_operation_date = medicalOperationDate as string;
  }
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
const formStatusSubmit = () => {
  formStatusCurrent.value = formStatusOptions[formStatusCurrent.value + 1]
    ? formStatusCurrent.value + 1
    : 0;
};
onUnmounted(() => {
  cityStore.filterQuery = '';
  cityStore.selectedId = undefined;
  cityStore.unsetFilter();
  store.editedId = undefined;
});



const route = useRoute();
const router = useRouter();

const modalActive = ref(false);
const isLoading = ref(true);

const img_1 = ref<File | undefined>(undefined);
const img_2 = ref<File | undefined>(undefined);

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
  doctor: store.edited?.doctor,
  regiment: store.edited?.regiment?.id,
  city: store.edited?.city?.id,
  rest: store.edited?.rest,
  price : store.edited?.price,
  surgery: store.edited?.surgery,
  created_at: store.edited?.created_at,
} as unknown as Patient);

const formStatusWithHeader = ref(true);
const formStatusCurrent = ref(0);
const formStatusOptions = ['info', 'success', 'danger', 'warning'];
isLoading.value = false;

const getImageAsBase64 = async (url) => {
  const response = await fetch(url);
  const blob = await response.blob();

  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onloadend = () => resolve(reader.result);
    reader.onerror = reject;
    reader.readAsDataURL(blob);
  });
};
const generatePdf = async  () => {
  const imageUrl_1 = '../../public/assets/images/gg.jpg';
  const imageUrl_2 = '../../public/assets/images/logo_2.png';
  const imageUrl_3 = '../../public/assets/images/logoo.png';
  const base64Image = await  getImageAsBase64(imageUrl_1);
  const base64Image_2 = await  getImageAsBase64(imageUrl_2);
  const base64Image_3 = await  getImageAsBase64(imageUrl_3);
  const shippingSlip = `<div>
  <div style="display: flex; justify-content: space-between; margin-top: 0px; margin-bottom: 0px;">
      <img src="${base64Image}" style="width: 7rem; background-size: cover;">
      <h1 class="font-bold my-auto text-lg"> مركز سوف للعلاج الطبيعي و الفزيولوجي </h1>
      <img src="${base64Image_2}" style="width: 7rem; background-size: cover;">
    </div>
    <div style=" display: flex; justify-content: space-between; height: 10rem">
      <div style="margin: auto;width: 30%; ">
        <h1 style="--tw-bg-opacity: 1;  font-size: 1rem;">Djarmonune Abd Elhakim</h1>
        <h1 style="font-size: 0.75rem">Kinesitherapeute</h1>
      </div>
      <div  style="display: flex;width: 50%;"> 
        <img src="${base64Image_3}" style="width: 10rem; background-size: cover; margin-left: auto; margin-right: auto;" >
      </div>
      <div style="margin: auto;width: 20%; ">
        <h1 style="--tw-bg-opacity: 1;text-align: right;  font-size: 1rem"> جرمون عبد الحكيم</h1>
        <h1 style="font-size: 0.75rem; margin-left: 2rem;">العلاج الطبيعي والفزيولوجي</h1>
      </div>
    </div>
    <hr >
    <div style="display: flex;margin: 0rem;  margin-left: auto; margin-right: auto;">
      <h1  style="font-size: 4.5rem;margin: 0rem; margin-left: auto; margin-right: auto; ">تقريــر</h1>
    </div>
    <div style="font-size: 1.5rem;display: flex;margin-top: 2rem; margin-bottom: 2rem; width: 100%; text-align: right; ">
      <div style="margin-left: auto; margin-right: auto;">
          <p style="margin-bottom: 1rem; line-height: 3rem">
            انا الممضي أسفله السيد : <span style=" font-weight: 700;"> جرمون عبد الحكيم</span>       
            أخصــائي العــلاج الطبيعــي و الفـزيــولــوجــي
            يشهد أن السيد : <span style=" font-weight: 700;"> ${patient.value.name}</span>
            المــولــود بــتــاريــخ : <span style=" font-weight: 700;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
            يزاول العلاج بمركزنا من تاريخ : <span style=" font-weight: 700;"> ${formatDate(patient.value.created_at)}</span> 
           الى تاريخ 
          </p>
          <p style="margin-bottom: 3rem; line-height: 3rem">
            :ملاحظات
          </p>
          <p style="margin: 0rem;">
            .منح هدا التقرير لاستعماله فيما يسمح به النطاق القانوني
          </p>
          <div style="display: flex; justify-content: space-between;">
              <p style="margin-left: 4rem; margin-bottom: 3rem"  >
                الوادي في
              </p>
              <p style="height: 1rem; margin-bottom: 3rem">
                .الختم والإمضاء
              </p>
             
          </div> 
      </div>
    </div>
    <hr >
        <div style="display: flex; justify-content: space-between;">
              <p style=" line-height: 1rem;">
               ${'06 66 57 58 69'} :الهاتف  
              </p>
              <p style=" line-height: 1rem;"  >
                حي النزلة - بالقرب من صيدلية الاشعري - الوادي
              </p>
          </div> 
  </div> `;
    const print = window.open("", "_blank"); 
    if (print) {
      print.document.write(shippingSlip);
      print.document.close();
      print.print();
    }
    
};
</script>

<template >
  <div v-if="isLoading" class="flex justify-center items-center h-screen">
    <looping-rhombuses-spinner :animation-duration="1500" :rhombus-size="20" color="#fff" />
  </div>

  <div v-else>
    <SectionMain  v-if="patient">
      <SectionTitleLineWithButton :icon="mdiBookEdit" dir="rtl" title="الملف الشخصي للمريض" main >
        <div class="flex">
          <h1 class="mx-4 text-2xl">
          الباقي : 
          </h1>
        
          
          <PillTag  class="text-2xl rounded-sm"   color="danger" :label="`${patient.rest} دج`" />
        </div>
        
        <BaseButton :icon="mdiPrinter" class=" lg:w-[20%] w-full" color="" label="طباعة التقرير" @click="generatePdf" />

      </SectionTitleLineWithButton>
      <CardBoxModal
        v-model="modalActive"
        title="Please confirm the delete"
        button-label="Delete"
        button-cancel-label="Cancel"
        button="danger"
        has-cancel
        @confirm="deletePatient"
      />

      <CardBox dir="rtl" form @submit.prevent="submit">
       
        <div class="flex">
          <FormField  label="رقم الهاتف" class=" ml-3 w-1/2">
            <FormControl
              v-model="patient.phone"
              type="text"
              placeholder="رقم الهاتف "
              :style="{ direction: 'rtl' }"
            />
          </FormField>
          <FormField  label="الاسم الكامل" class=" w-1/2">
            <FormControl
              v-model="patient.name"
              type="text"
              placeholder="الاسم بالعربية"
              :style="{ direction: 'rtl' }"
            />
          </FormField>
        </div>
        <div class="flex">
          <FormField  label="العمر" class="ml-3 w-1/2">
            <FormControl
              v-model="patient.age"
              type="number"
              placeholder="العمر "
            />
          </FormField>
          <FormField  label="عدد الحصص" class=" w-1/2">
            <FormControl
              v-model="patient.number_of_days"
              type="number"
              placeholder="عدد الحصص"
              :style="{ direction: 'rtl' }"
            />
          </FormField>

          
        </div>
        <div class="flex w-full">
          <FormField  label="أجرى عملية" class="ml-3 w-[8%]">
            <FormCheckRadioGroup
              class="my-5 mx-4"
              v-model="patient.surgery"
              type="switch"
              name="notifications-switch"
              :options="{ outline: 'Active' }"
            />
          </FormField>
          <FormField  label="تاريخ إجراء العملية" class=" ml-3 w-[46%]">
            <VueDatePicker :disabled="!patient.surgery" v-model="patient.medical_operation_date" :format="formatt" :dark="styleStore.darkMode" />
          </FormField>
          <FormField  label="الطبيب" class=" w-[46%]">
            <FormControl
              v-model="patient.doctor"
              type="text"
              placeholder="المرض الأساسي "
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
        <div  class="w-full h-full p-4 dark:bg-slate-900 bg-slate-100 mb-4 rounded">
          <SectionTitleLineWithButton dir="rtl" :icon="mdiMedicalBag" title="أمراض أخرى"  />
          <!-- <div class=" text-2xl mb-4 font-bold "> أمراض اخرى:</div> -->
          <FormCheckRadioGroup
            v-model="patient.other_diseases"
            name="sample-checkbox"
            :options="diseases"
          />
        </div>
        <div class="w-full h-full p-4 dark:bg-slate-900 bg-slate-100 mb-4 rounded">
          
          <SectionTitleLineWithButton :icon="mdiClipboardList" dir="rtl" title=" الحضور:" >

            <!-- <BaseButton :icon="mdiPrinter" class=" lg:w-[20%] w-full" color="" label="طباعة الحضور" @click="generatePdf" /> -->
          </SectionTitleLineWithButton>
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
          
          <BaseButton :icon="mdiContentSaveAll" class="mx-0 lg:ml-4  lg:w-[77%] w-full" type="submit" color="success" label="حفظ" @click="submit" />
          <BaseButton :icon="mdiDelete" class=" lg:w-[20%] w-full" color="danger" label="حذف" @click="modalActive = true" />
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
