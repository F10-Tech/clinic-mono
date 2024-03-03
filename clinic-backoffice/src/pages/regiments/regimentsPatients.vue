<script setup lang="ts">
import { mdiAccountMultiplePlus , mdiMagnify,mdiAccount  } from '@mdi/js';
import { onBeforeMount, ref, onUnmounted } from 'vue';
import { usePatientsStore, useDiseasesStore, usePriceStore, useRegimentStore, useStateStore, useCityStore } from '@/stores/models';
import SectionMain from '@/vendor/Section/SectionMain.vue';
import TablePatients from '@/components/Tables/TablePatients.vue';
import CardBox from '@/vendor/CardBox/CardBox.vue';
import SectionTitleLineWithButton from '@/vendor/Section/SectionTitleLineWithButton.vue';
import BaseButtons from '@/vendor/Base/BaseButtons.vue';
import BaseButton from '@/vendor/Base/BaseButton.vue';
import FormControl from '@/vendor/Form/FormControl.vue';
import CardBoxComponentEmpty from '@/vendor/CardBox/CardBoxComponentEmpty.vue';
import { useRoute, useRouter } from 'vue-router';

const store = usePatientsStore();
const diseaseStore = useDiseasesStore();
const regimentStore = useRegimentStore();
const stateStore = useStateStore();
const cityStore = useCityStore();
const priceStore = usePriceStore();


const route = useRoute();
const router = useRouter();


let searching = ref(false);
const isLoading = ref(false);

const reset = () => {
  store.filterQuery = '';
};
const search = () => {
  store.localSearch('name');
};
const stopSearching = () => {
  searching.value = false;
  store.filterQuery = '';
  store.selectedId = undefined;
  store.unsetFilter();
};
onBeforeMount(async () => {
  isLoading.value = true; // Set loading to true while fetching data
  await store.fetchByRegiments(route.params.id.toString());
  // await diseaseStore.fetchAll();
  // await regimentStore.fetchAll();
  // await stateStore.fetchAll();
  // await cityStore.fetchAll();
  // await priceStore.fetchAll();
  // console.log('store.list', priceStore.list);
  isLoading.value = false; // Set loading to false after the data has loaded
});
onUnmounted(() => {
  store.filterQuery = '';
  store.selectedId = undefined;
  store.unsetFilter();
});
</script>

<template>
  <SectionMain dir="rtl">
    <SectionTitleLineWithButton  :icon="mdiAccount" title="المرضى" main>
      
    </SectionTitleLineWithButton>
    <FormControl
      v-if="searching"
      v-model="store.filterQuery"
      placeholder="البحث عن مريض"
      ctrl-k-focus
      transparent
      borderless
      class="my-4 border rounded animate-fade-down animate-duration-[80ms]"
      @input="search"
      @clear="reset"
    />
    <CardBox v-if="store.filteredList && store.filteredList.length > 0"  class="mb-6" has-table>
      <TablePatients :patients="store.filteredList" :loading="isLoading" />
    </CardBox>
    <CardBox v-else >
      <CardBoxComponentEmpty /> 
    </CardBox>
  </SectionMain>
</template>
