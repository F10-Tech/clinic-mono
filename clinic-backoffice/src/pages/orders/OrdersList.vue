<script setup lang="ts">
import { mdiCartOutline, mdiMagnify } from '@mdi/js';
import { onBeforeMount, ref, onUnmounted } from 'vue';

import { useOrderStore } from '@/stores/models/orders';
import SectionMain from '@/vendor/Section/SectionMain.vue';
import TableOrders from '@/components/Tables/TableOrders.vue';
import CardBox from '@/vendor/CardBox/CardBox.vue';
import SectionTitleLineWithButton from '@/vendor/Section/SectionTitleLineWithButton.vue';
import BaseButtons from '@/vendor/Base/BaseButtons.vue';
import BaseButton from '@/vendor/Base/BaseButton.vue';
import FormControl from '@/vendor/Form/FormControl.vue';

const store = useOrderStore();

let searching = ref(false);
const isLoading = ref(false);

const reset = () => {
  store.filterQuery = '';
};

const search = () => {
  store.localSearch('id');
};

onBeforeMount(async () => {
  isLoading.value = true; // Set loading to true while fetching data
  await store.fetchAll();
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
  <SectionMain>
    <SectionTitleLineWithButton :icon="mdiCartOutline" title="Orders" main>
      <BaseButtons type="justify-start lg:justify-end" no-wrap>
        <BaseButton
          label="Create Order"
          color="contrast"
          to="/orders/new"
          class="font-medium mr-2"
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
      placeholder="Search (ctrl+k)"
      ctrl-k-focus
      transparent
      borderless
      class="my-4 border rounded animate-fade-down animate-duration-[80ms]"
      @input="search"
      @clear="reset"
    />

    <CardBox class="mb-6" has-table>
      <TableOrders :orders="store.filteredList" :loading="isLoading" />
    </CardBox>
  </SectionMain>
</template>
