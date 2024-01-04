<script setup lang="ts">
import { computed, ref } from 'vue';
import { mdiTextBoxEditOutline, mdiPencil, mdiDeleteForever  } from '@mdi/js';
import { LoopingRhombusesSpinner } from 'epic-spinners';
import { format } from 'date-fns';
import {  usePresenceStore, useAgentStore, usePatientsStore } from '@/stores/models';
import type { Order } from '@/models';
import BaseLevel from '@/vendor/Base/BaseLevel.vue';
import BaseButtons from '@/vendor/Base/BaseButtons.vue';
import BaseButton from '@/vendor/Base/BaseButton.vue';
import CardBoxModal from '@/vendor/CardBox/CardBoxModal.vue';

const store = usePresenceStore();
const storePatients = usePatientsStore();
const agent = useAgentStore();

function formatDate(value) {
  if (value) {
    return format(new Date(value), `HH:mm | yyyy-MM-dd`);
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
const order = ref<Order>({
  id: '',
} as unknown as Order);


const selectId = (id: string) => {
  store.editedId = id;
  modalActive.value = true;
};
const modalActive = ref(false);

const deletePresences = async () => {
  console.log(store.editedId);
  const isDeleted = await store.delete(store.editedId!);
  if (isDeleted) {
      // relod page
      window.location.reload();
  } else {
    alert('حدث خطأ أثناء حذف الحضور');
  }
};

</script>

<template>
  <div v-if="isLoading" class="flex justify-center items-center h-screen">
    <looping-rhombuses-spinner :animation-duration="1500" :rhombus-size="20" color="#fff" />
  </div>
  <div v-else>

    <CardBoxModal
        v-model="modalActive"
        title="هل تريد حذف المرض؟"
        button-label="حذف"
        button-cancel-label="لا"
        button="danger"
        has-cancel
        @confirm="deletePresences"
      />
    <table>
      <thead>
        <tr>
          <th class="text-center">الأسم</th>
          <th class="text-center">التاريخ</th>
          <th class="text-center">المبلغ</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="order in orders" :key="order.id">
          <td data-label="الإسم" class=" text-center">
            {{order.patient.name}}
          </td>
          <td data-label="الأسم" class="text-center">
            {{ formatDate(order.created_at) }}
          </td>
          <td data-label="الأسم" class="text-center">
            {{ order.amount }}
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
