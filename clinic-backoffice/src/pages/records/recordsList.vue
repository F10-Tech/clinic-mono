<script setup lang="ts">
import { mdiReceiptTextPlus, mdiMagnify, mdiClipboardList } from '@mdi/js';
import { onBeforeMount, ref, onUnmounted } from 'vue';
import { useRecordStore } from '@/stores/models';
import SectionMain from '@/vendor/Section/SectionMain.vue';
import TableRecordPresences from '@/components/Tables/TableRecordPresences.vue';
import CardBox from '@/vendor/CardBox/CardBox.vue';
import SectionTitleLineWithButton from '@/vendor/Section/SectionTitleLineWithButton.vue';
import BaseButtons from '@/vendor/Base/BaseButtons.vue';
import BaseButton from '@/vendor/Base/BaseButton.vue';
import FormControl from '@/vendor/Form/FormControl.vue';

const store = useRecordStore();


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
  isLoading.value = true;
  await store.fetchAll();
  console.log('store', store.all);
  isLoading.value = false;
});
onUnmounted(() => {
  store.filterQuery = '';
  store.selectedId = undefined;
  store.unsetFilter();
});
</script>

<template>
  <SectionMain dir="rtl">
    <SectionTitleLineWithButton  :icon="mdiReceiptTextPlus" title="تسجيل الحضور" main>
      
      <BaseButtons type="justify-start lg:justify-end" no-wrap>
        <BaseButton
          label="لإحة الحضور"
          color="contrast"
          to="/records/presences"
          class="font-medium ml-2"
          :icon="mdiClipboardList "
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
      <TableRecordPresences :patients="store.filteredList" :loading="isLoading" />
    </CardBox>
  </SectionMain>
</template>
