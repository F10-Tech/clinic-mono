<script setup lang="ts">
import { computed, ref } from 'vue';
import { mdiTextBoxEditOutline } from '@mdi/js';
import { LoopingRhombusesSpinner } from 'epic-spinners';
import { format } from 'date-fns';

import type { Order } from '@/models';
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
  orders: { type: Array<Order>, default: [], required: true },
  isLoading: { type: Boolean, default: false },
});

const isArabic = (text) => {
  const arabicRegex = /[\u0600-\u06FF]/;
  return arabicRegex.test(text);
};

const items = computed(() => props.orders);

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
          <th class="text-center">Ref</th>
          <th class="text-center">Customer</th>
          <th class="text-center">Phone</th>
          <th class="text-center">Service</th>
          <th class="text-center">Subservice</th>
          <th class="text-center">Scheduled</th>
          <th class="text-center">Created At</th>
          <th class="text-center">Location</th>
          <th class="text-center">Price</th>
          <th class="text-center">Status</th>
          <th />
        </tr>
      </thead>
      <tbody>
        <tr v-for="order in orders" :key="order.id">
          <td data-label="Name" class="font-bold text-lg">
            {{ order.id }}
          </td>
          <td data-label="Name" :class="{ 'rtl-text': isArabic(order.customer.first_name) }">
            {{ order.customer.first_name }} {{ order.customer.last_name }}
          </td>
          <td data-label=" Name">
            {{ order.customer.phone }}
          </td>
          <td data-label="Name">
            <h2 class="font-bold">
              {{ order.service.name_en }}
            </h2>
          </td>
          <td>
            <h2 class="capitalize">
              {{ order.subservice[0].name_en }}
            </h2>
          </td>
          <td data-label="Name" class="font-bold text-xl text-center">
            {{ formatDate(order.scheduled) }}
          </td>
          <td data-label="Name" class="text-center font-bold text-xl">
            {{ formatDate(order.created_at) }}
          </td>
          <td data-label="Name">
            {{ order.location }}
          </td>
          <td data-label="Name" class="font-bold text-lg text-center">{{ order.price }}.00 DA</td>
          <td class="justify-center items-center flex">
            <PillTagOrderStatus :color="order.state" :label="order.state" />
          </td>

          <td class="before:hidden lg:w-1 whitespace-nowrap">
            <BaseButtons type="justify-start lg:justify-end" no-wrap>
              <BaseButton :icon="mdiTextBoxEditOutline" small :to="'/orders/edit/' + order.id" />
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
