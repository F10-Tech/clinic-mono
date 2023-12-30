<script setup lang="ts">
import { computed, ref } from 'vue';
import { mdiDeleteForever, mdiWeatherMoonsetDown  } from '@mdi/js';
import { LoopingRhombusesSpinner } from 'epic-spinners';
import { useRoute, useRouter } from 'vue-router';
import type { Disease } from '@/models';
import BaseLevel from '@/vendor/Base/BaseLevel.vue';
import BaseButtons from '@/vendor/Base/BaseButtons.vue';
import BaseButton from '@/vendor/Base/BaseButton.vue';
import {  useDiseasesStore, useAgentStore } from '@/stores/models';
import CardBoxModal from '@/vendor/CardBox/CardBoxModal.vue';

const store = useDiseasesStore();
const agent = useAgentStore();


const props = defineProps({
  diseases: { type: Array<Disease>, default: [], required: true },
  isLoading: { type: Boolean, default: false },
});

// const isArabic = (text) => {
//   const arabicRegex = /[\u0600-\u06FF]/;
//   return arabicRegex.test(text);
// };

const items = computed(() => props.diseases);

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

const formStatusWithHeader = ref(true);

const formStatusCurrent = ref(0);

const formStatusOptions = ['info', 'success', 'danger', 'warning'];

const formStatusSubmit = () => {
  formStatusCurrent.value = formStatusOptions[formStatusCurrent.value + 1]
    ? formStatusCurrent.value + 1
    : 0;
};
const modalActive = ref(false);

const deleteDisease = async () => {
  const isDeleted = await store.delete(store.editedId!);
  if (isDeleted) {
      // relod page
      window.location.reload();
  } else {
    setTimeout(function () {
      BackHim();
    }, agent.timeToKill);
  }
};


const route = useRoute();
const router = useRouter();

const BackHim = () => {
  formStatusCurrent.value = 0;
};

const selectId = (id: string) => {
  store.editedId = id;
  modalActive.value = true;
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
        @confirm="deleteDisease"
      />
    <table>
      <thead>
        <tr>
          <th class="text-center text-xl">المرض</th>
          <th />
        </tr>
      </thead>
      <tbody>
        <tr v-for="disease in diseases" :key="disease.id">
          <td data-label="المرض" class=" text-center">
            {{ disease.name }}
          </td>
          <td class="before:hidden lg:w-1 whitespace-nowrap">
            <BaseButtons type="justify-start lg:justify-end" no-wrap>
              <BaseButton color="danger" :icon="mdiDeleteForever " small @click="selectId(disease.id)" />
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
