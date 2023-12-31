<script setup lang="ts">
import { computed, ref } from 'vue';
import { mdiTextBoxEditOutline, mdiPencil, mdiAccountCheck  } from '@mdi/js';
import { LoopingRhombusesSpinner } from 'epic-spinners';
import { format } from 'date-fns';
import {  usePresenceStore, useAgentStore, usePatientsStore } from '@/stores/models';
import type { Presence } from '@/models';
import type { Patient } from '@/models';
import BaseLevel from '@/vendor/Base/BaseLevel.vue';
import BaseButtons from '@/vendor/Base/BaseButtons.vue';
import BaseButton from '@/vendor/Base/BaseButton.vue';

const store = usePresenceStore();
const storePatients = usePatientsStore();
const agent = useAgentStore();

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

</script>

<template>
  <div v-if="isLoading" class="flex justify-center items-center h-screen">
    <looping-rhombuses-spinner :animation-duration="1500" :rhombus-size="20" color="#fff" />
  </div>
  <div  v-else>
    <table>
      <thead>
        <tr>
          <th class="text-center">رقم الهاتف</th>
          <th class="text-center">الأسم</th>
          <th class="text-center">العنوان</th>
          <th class="text-center">الفوج</th>
          <th class="text-center">الطبيب</th>
          <th class="text-center">المرض</th>
          <th class="text-center">تاريخ العملية</th>
          <!-- <th class="text-center">الحصص</th> -->
          <th class="text-center"></th>
          <th />
        </tr>
      </thead>
      <tbody>
        <tr v-for="patient in patients" :key="patient.id">
          <td data-label="الهاتف" class="">
            {{ patient.phone }}
          </td>
          <td data-label="الأسم" :class="{ 'rtl-text': isArabic(patient.name) }">
            {{ patient.name }}
          </td>
          <td data-label="العنوان">
            {{ patient.city?.state }} - {{ patient.city?.name }} 
          </td>
          <td data-label="الفوج" :class="{ 'rtl-text': isArabic(patient.regiment?.name) }">
            <h2 class=" ">
              {{ patient.regiment?.name }}
            </h2>
          </td>
          <td data-label="الطبيب" :class="{ 'rtl-text': isArabic(patient.doctor) }">
            <h2 class="">
              {{ patient.doctor }}
            </h2>
          </td>
          <td data-label="المرض" :class="{ 'rtl-text': isArabic(patient.disease?.name) }">
            <h2>
              {{ patient.disease?.name }}
            </h2>
          </td>
          <td data-label="تاريخ إجراء العملية" class=" text-center " >
            {{formatDate(patient.medical_operation_date)}}
          </td>
          <!-- <td data-label="الحصص المتبقية" class="text-center text-xl">
            {{ patient.number_of_days }}
          </td> -->
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
