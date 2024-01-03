<script setup lang="ts">
import { mdiAccountMultiplePlus , mdiMagnify,mdiAccount  } from '@mdi/js';
import { onBeforeMount, ref, onUnmounted } from 'vue';
import { usePatientsStore, useDiseasesStore, useRegimentStore, useStateStore, useCityStore } from '@/stores/models';
import SectionMain from '@/vendor/Section/SectionMain.vue';
import TablePatients from '@/components/Tables/TablePatients.vue';
import CardBox from '@/vendor/CardBox/CardBox.vue';
import SectionTitleLineWithButton from '@/vendor/Section/SectionTitleLineWithButton.vue';
import BaseButtons from '@/vendor/Base/BaseButtons.vue';
import BaseButton from '@/vendor/Base/BaseButton.vue';
import FormControl from '@/vendor/Form/FormControl.vue';

const store = usePatientsStore();
const diseaseStore = useDiseasesStore();
const regimentStore = useRegimentStore();
const stateStore = useStateStore();
const cityStore = useCityStore();

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
  await store.fetchAll();
  await diseaseStore.fetchAll();
  await regimentStore.fetchAll();
  await stateStore.fetchAll();
  await cityStore.fetchAll();
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
      <BaseButtons type="justify-start lg:justify-end" no-wrap>
        <BaseButton
          label="إضافة مريض"
          color="contrast"
          to="/patients/new"
          class="font-medium ml-2"
          :icon="mdiAccountMultiplePlus "
        />
        <BaseButton
          :icon="mdiMagnify"
          icon-size="20"
          class="p-2"
          :color="searching ? 'danger' : 'contrast'"
          @click="searching == false ? (searching = true) : stopSearching()"
        />
      </BaseButtons>
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

    <CardBox class="mb-6" has-table>
      <TablePatients :patients="store.filteredList" :loading="isLoading" />
    </CardBox>
  </SectionMain>
</template>
