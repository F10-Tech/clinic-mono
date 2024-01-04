<script setup lang="ts">
import { mdiDiamondStone, mdiCash} from '@mdi/js';
import { onBeforeMount, ref } from 'vue';
import { usePriceStore } from '@/stores';
import SectionMain from '@/vendor/Section/SectionMain.vue';
import SectionTitleLineWithButton from '@/vendor/Section/SectionTitleLineWithButton.vue';
import CardBox from '@/vendor/CardBox/CardBox.vue';
import CardBoxComponentEmpty from '@/vendor/CardBox/CardBoxComponentEmpty.vue';
import BaseButtons from '@/vendor/Base/BaseButtons.vue';
import TablePrices from '@/components/Tables/TablePrices.vue';
import BaseButton from '@/vendor/Base/BaseButton.vue';

const store = usePriceStore();
const isLoading = ref(false);

const reset = () => {
  store.filterQuery = '';
};

onBeforeMount(async () => {
  isLoading.value = true; 
  await store.fetchAll();
  console.log('store.filteredList', store.filteredList);
  isLoading.value = false;
});

</script>

<template>
  <SectionMain dir="rtl">
    <SectionTitleLineWithButton  :icon="mdiDiamondStone" title="فئة السعر" main>
      
      <BaseButtons type="justify-start lg:justify-end" no-wrap>
        <BaseButton
          label="إضافة فئة سعر"
          color="contrast"
          to="/prices/new"
          class="font-medium ml-2"
          :icon="mdiCash "
        />
      </BaseButtons>
    </SectionTitleLineWithButton>
    <CardBox v-if="store.filteredList && store.filteredList.length > 0"  class="mb-6" has-table>
      <TablePrices :prices="store.filteredList" :loading="isLoading" />
    </CardBox>
    <CardBox v-else >
      <CardBoxComponentEmpty /> 
    </CardBox>
  </SectionMain>
</template>
