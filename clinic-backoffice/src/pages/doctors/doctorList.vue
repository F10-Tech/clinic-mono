<script setup lang="ts">
import { mdiAccount, mdiMagnify, mdiMedicalCottonSwab  } from '@mdi/js';
import { onBeforeMount, ref, onUnmounted } from 'vue';
import { useDoctorsStore } from '@/stores/models';
import SectionMain from '@/vendor/Section/SectionMain.vue';
import TableDoctors from '@/components/Tables/TableDoctors.vue';
import CardBox from '@/vendor/CardBox/CardBox.vue';
import CardBoxComponentEmpty from '@/vendor/CardBox/CardBoxComponentEmpty.vue';
import SectionTitleLineWithButton from '@/vendor/Section/SectionTitleLineWithButton.vue';
import BaseButtons from '@/vendor/Base/BaseButtons.vue';
import BaseButton from '@/vendor/Base/BaseButton.vue';
import FormControl from '@/vendor/Form/FormControl.vue';

const store = useDoctorsStore();

let searching = ref(false);
const isLoading = ref(false);

const reset = () => {
  store.filterQuery = '';
};

const search = () => {
  store.localSearch('name');
};

onBeforeMount(async () => {
  isLoading.value = true;
  await store.fetchAll();
  isLoading.value = false;
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
    <SectionTitleLineWithButton  :icon="mdiAccount" title="الأطباء" main>
      
      <BaseButtons type="justify-start lg:justify-end" no-wrap>
        <BaseButton
          label="إضافة طبيب"
          color="contrast"
          :icon="mdiMedicalCottonSwab"
          to="/doctors/new"
          class="font-medium ml-2"
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
        placeholder="البحث عن مرض"
        ctrl-k-focus
        transparent
        borderless
        class="my-4 border rounded animate-fade-down animate-duration-[80ms]"
        @input="search"
        @clear="reset"
      />
      <CardBox v-if="store.filteredList && store.filteredList.length > 0"  class="mb-6" has-table>
        <TableDoctors :diseases="store.filteredList" :loading="isLoading"  />
      </CardBox>
      <CardBox v-else >
        <CardBoxComponentEmpty /> 
      </CardBox>
  </SectionMain>
</template>
