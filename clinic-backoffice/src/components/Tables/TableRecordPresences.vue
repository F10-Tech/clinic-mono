<script setup lang="ts">
import { computed, ref } from 'vue';
import { mdiTextBoxEditOutline, mdiPencil, mdiAccountCheck, mdiCashFast  } from '@mdi/js';
import { LoopingRhombusesSpinner } from 'epic-spinners';
import { format } from 'date-fns';
import {  usePresenceStore, useAgentStore, usePatientsStore, useOrdersStore } from '@/stores/models';
import type { Presence } from '@/models';
import type { Patient } from '@/models';
import type { Order } from '@/models';
import BaseLevel from '@/vendor/Base/BaseLevel.vue';
import BaseButtons from '@/vendor/Base/BaseButtons.vue';
import BaseButton from '@/vendor/Base/BaseButton.vue';
import PillTagNumber from '@/vendor/PillTag/PillTagNumber.vue';
import CardBoxModal from '@/vendor/CardBox/CardBoxModal.vue';
import FormField from '@/vendor/Form/FormField.vue';
import FormControl from '@/vendor/Form/FormControl.vue';
const store = usePresenceStore();
const storePatients = usePatientsStore();
const agent = useAgentStore();
const orderStore = useOrdersStore();

function formatDate(value) {
  if (value) {
    return format(new Date(value), 'yyyy-MM-dd');
  }
}
const props = defineProps({
  patients: { type: Array<Patient>, default: [], required: true },
  isLoading: { type: Boolean, default: false },
});

const isArabic = (text) => {
  const arabicRegex = /[\u0600-\u06FF]/;
  return arabicRegex.test(text);
};

const items = computed(() => props.patients);

const perPage = ref(11);

const currentPage = ref(0);

const itemsArrayLength = computed(() => {
  const itemsArray = Object.values(items.value);
  return itemsArray.length;
});

const numPages = computed(() => Math.ceil(itemsArrayLength.value / perPage.value));

const currentPageHuman = computed(() => currentPage.value + 1);

const pagesList = computed(() => {
  const pagesList: number[] = [];

  for (let i = 0; i < numPages.value; i++) {
    pagesList.push(i);
  }

  return pagesList;
});
const presence = ref<Presence>({
  id: '',
} as unknown as Presence);
const order = ref<Order>({
  patient: '',
  amount: 0,
} as unknown as Order);

const createPresence = async (id: string) => {
  // console.log(id)
  presence.value.patient = id;
  const isDeleted = await store.create(presence.value);
  if (isDeleted) {
      // relod page
      window.location.reload();
  } 
  else {
    alert('حدث خطأ أثناء تسجيل الحضور');
  }
};

const selectId = (id: string) => {
  console.log(id);
  order.value.patient = id;
  // store.editedId = id;
  modalActive.value = true;
};
const modalActive = ref(false);

const createOrder = async () => {
  const isDeleted = await orderStore.create(order.value);
  if (isDeleted) {
      // relod page
      window.location.reload();
  } else {
    alert(' خطأ أثناء دفع المستحقات ');
  }
};

</script>

<template>
  <div v-if="isLoading" class="flex justify-center items-center h-screen">
    <looping-rhombuses-spinner :animation-duration="1500" :rhombus-size="20" color="#fff" />
  </div>
  <div  v-else>
    <CardBoxModal
        v-model="modalActive"
        title="دفع المستحقات   "
        button-label="دفع"
        button-cancel-label="الغاء"
        button="success"
        has-cancel
        @confirm="createOrder"
      >
      <FormField  label=" المبلغ" class=" ml-3">
            <FormControl
              v-model="order.amount"
              type="number"
              placeholder="المبلغ المدفوع"
              :style="{ direction: 'rtl' }"
            />
        </FormField>
    </CardBoxModal>


    <table>
      <thead>
        <tr>
          <th class="text-start">رقم الهاتف</th>
          <th class="text-start">الأسم</th>
          <th class="text-start">العنوان</th>
          <th class="text-start">الفوج</th>
          <th class="text-start">المرض</th>
          <th class="text-start">الباقي</th>
          <th class="text-start">الحصص المدفوعة</th>
          <th class="text-center"> دفع المستحقات</th>
          <th class="text-center"></th>
          <th />
        </tr>
      </thead>
      <tbody>
        <tr v-for="patient in patients" :key="patient.id">
          <td data-label="الهاتف" class="text-start">
            {{ patient.phone }}
          </td>
          <td data-label="الأسم" :class="{ 'rtl-text': isArabic(patient.name) }">
            {{ patient.name }}
          </td>
          <td data-label="العنوان" class="w-44" :class="{ 'rtl-text': isArabic(patient.city?.state) }">
            {{ patient.city?.state }} - {{ patient.city?.name }} 
          </td>
          <td data-label="الفوج" :class="{ 'rtl-text': isArabic(patient.regiment?.name) }">
            <h2 class=" ">
              {{ patient.regiment?.name }}
            </h2>
          </td>
          <td data-label="المرض" :class="{ 'rtl-text': isArabic(patient.disease?.name) }">
            <h2>
              {{ patient.disease?.name }}
            </h2>
          </td>
          <td data-label=" الباقي " dir="rtr" class="text-start font-bold text-red-500" >
            {{patient.rest}} دج
          </td>
          <td  data-label="الحصص المدفوعة"  dir="ltr" class="text-center text-xl w-40">
            <div v-if="patient.sessions > 0">
              <PillTagNumber color="success" :label="patient.sessions" />
            </div>
            <div v-else>
              <PillTagNumber color="danger" :label="patient.sessions" />
            </div>
          </td>
          <td  data-label="دفع المستحقات"  dir="rtr" class="text-center text-xl w-40">
            <div v-if="patient.rest > 0">
              <BaseButton :icon="mdiCashFast" label="دفع" small color="info" @click="selectId(patient.id)" />
            </div>
            <div v-else>
              <BaseButton :icon="mdiCashFast" label="تم دفع " small color="success" disabled />
            </div>
          </td>
          
          <td data-label="" class="lg:justify-center items-center flex">
            
            <div v-if="!patient.checkout">
              <BaseButtons type="justify-start lg:justify-end" no-wrap>
                  <BaseButton label="تسجيل حضور" color="success" :icon="mdiPencil " small @click="createPresence(patient.id)" />
              </BaseButtons>
            </div>
            <div v-else>
              <BaseButtons type="justify-start lg:justify-end" no-wrap>
                  <BaseButton disabled label="تم تسجيل"  :icon="mdiAccountCheck" small  />
              </BaseButtons>
            </div>
           
          </td>

          <td class="before:hidden lg:w-1 whitespace-nowrap">
            <BaseButtons type="justify-start lg:justify-end" no-wrap>
              <BaseButton :icon="mdiTextBoxEditOutline" small :to="'/patients/edit/' + patient.id" />
            </BaseButtons>
          </td>
        </tr>
      </tbody>
    </table>
    <div class="p-3 lg:px-6 border-t border-gray-100 dark:border-slate-800">
      <BaseLevel>
        <BaseButtons>
          <BaseButton
            v-for="page in pagesList"
            :key="page"
            :active="page === currentPage"
            :label="page + 1"
            :color="page === currentPage ? 'lightDark' : 'whiteDark'"
            small
            @click="currentPage = page"
          />
        </BaseButtons>
        <small>Page {{ currentPageHuman }} of {{ numPages }}</small>
      </BaseLevel>
    </div>
  </div>
</template>
<style>
.rtl-text {
  text-align: right;
}
</style>
