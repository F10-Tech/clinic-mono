<script setup lang="ts">
import { computed, ref } from 'vue';
import { mdiTextBoxEditOutline } from '@mdi/js';
import { LoopingRhombusesSpinner } from 'epic-spinners';
import { format } from 'date-fns';

import type { Patient } from '@/models';
import BaseLevel from '@/vendor/Base/BaseLevel.vue';
import BaseButtons from '@/vendor/Base/BaseButtons.vue';
import BaseButton from '@/vendor/Base/BaseButton.vue';
import PillTagOrderStatus from '@/components/PillTag/PillTagOrderStatus.vue';

function formatDate(value) {
  if (value) {
    return format(new Date(value), 'dd/MM/yyyy HH:mm ');
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

const orders = computed(() => {
  const itemsArray = Object.values(items.value); // Convert object values into an array
  return itemsArray.slice(
    perPage.value * currentPage.value,
    perPage.value * (currentPage.value + 1),
  );
});
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
</script>

<template>
  <div v-if="isLoading" class="flex justify-center items-center h-screen">
    <looping-rhombuses-spinner :animation-duration="1500" :rhombus-size="20" color="#fff" />
  </div>
  <div v-else>
    <table>
      <thead>
        <tr>
          <th class="text-center">رقم الهاتف</th>
          <th class="text-center">الأسم</th>
          <th class="text-center">العنوان</th>
          <th class="text-center">الفوج</th>
          <th class="text-center">الطبيب</th>
          <th class="text-center">المرض</th>
          <th class="text-center">أمراض أخرى</th>
          <th class="text-center">الحصص</th>
          <th class="text-center">الحالة</th>
          <th />
        </tr>
      </thead>
      <tbody>
        <tr v-for="patient in patients" :key="patient.id">
          <td data-label="Id" class="font-bold text-lg">
            {{ patient.phone }}
          </td>
          <td data-label="Name" :class="{ 'rtl-text': isArabic(patient.name) }">
            {{ patient.name }}
          </td>
          <td data-label="Phone">
            {{ patient.city?.state?.name }} - {{ patient.city?.name }} 
          </td>
          <td data-label="Regiment" :class="{ 'rtl-text': isArabic(patient.regiment?.name) }">
            <h2 class="font-bold">
              {{ patient.regiment?.name }}
            </h2>
          </td>
          <td data-label="Doctor">
            <h2 class="font-bold">
              {{ patient.doctor }}
            </h2>
          </td>
          <td data-label="disease">
            <h2 class="capitalize">
              {{ patient.disease?.name }}
            </h2>
          </td>
          <td data-label="Name" class="font-bold text-xl text-center flex" >
            <div v-for="disease in patient.other_diseases" :key="disease.id" class=" mr-1">
                {{ disease.name }}
            </div>
          </td>
          <td data-label="Name" class="text-center font-bold text-xl">
            {{ patient.number_of_days }}
          </td>
          <td class="justify-center items-center flex">
            <!-- working on it -->
            <PillTagOrderStatus :color="patient.status" :label="patient.status" />
          </td>

          <td class="before:hidden lg:w-1 whitespace-nowrap">
            <BaseButtons type="justify-start lg:justify-end" no-wrap>
              <BaseButton :icon="mdiTextBoxEditOutline" small :to="'/orders/edit/' + patient.id" />
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
