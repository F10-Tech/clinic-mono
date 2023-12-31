<script setup lang="ts">
import { mdiListBox, mdiMagnify, mdiAccountMultiplePlus } from '@mdi/js';
import { onBeforeMount, ref, onUnmounted } from 'vue';
import { useAgentStore, usePresenceStore } from '@/stores/models';
import SectionMain from '@/vendor/Section/SectionMain.vue';
import TablePresences from '@/components/Tables/TablePresences.vue';
import CardBox from '@/vendor/CardBox/CardBox.vue';
import SectionTitleLineWithButton from '@/vendor/Section/SectionTitleLineWithButton.vue';
import BaseButtons from '@/vendor/Base/BaseButtons.vue';
import BaseButton from '@/vendor/Base/BaseButton.vue';
import FormControl from '@/vendor/Form/FormControl.vue';

const store = usePresenceStore();
const agent = useAgentStore();


let searching = ref(false);
const isLoading = ref(false);

const reset = () => {
  store.filterQuery = '';
};

// const search = () => {
//   store.localSearch('name');
// };


onBeforeMount(async () => {
  isLoading.value = true; // Set loading to true while fetching data
  console.log('store');
  await store.fetchAll('today');
  // console.log('store', store.all);
  isLoading.value = false; // Set loading to false after the data has loaded
});

onUnmounted(() => {
  store.filterQuery = '';
  store.selectedId = undefined;
  store.unsetFilter();
});
const stopSearching = () => {
  searching.value = false;
  store.filterQuery = '';
  store.selectedId = undefined;
  store.unsetFilter();
};
</script>

<template>
  <SectionMain dir="rtl">
    <SectionTitleLineWithButton  :icon="mdiListBox" title=" لإحة الحضور" main>
      
      <BaseButtons type="justify-start lg:justify-end" no-wrap>
        <BaseButton
          label="تسجيل الحضور"
          to="/records"
          color="info"
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
      @clear="reset"
    />
    <!-- @input="search" -->


    <CardBox class="mb-6" has-table>
      <TablePresences :presences="store.filteredList" :loading="isLoading" />
    </CardBox>
  </SectionMain>
</template>
