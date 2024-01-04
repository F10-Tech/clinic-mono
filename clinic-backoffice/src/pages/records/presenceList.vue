<script setup lang="ts">
import { mdiClipboardList, mdiMagnify, mdiReceiptTextPlus } from '@mdi/js';
import { onBeforeMount, ref, onUnmounted } from 'vue';
import { usePresenceStore, useStyleStore } from '@/stores';
import SectionMain from '@/vendor/Section/SectionMain.vue';
import TablePresences from '@/components/Tables/TablePresences.vue';
import CardBox from '@/vendor/CardBox/CardBox.vue';
import SectionTitleLineWithButton from '@/vendor/Section/SectionTitleLineWithButton.vue';
import BaseButtons from '@/vendor/Base/BaseButtons.vue';
import BaseButton from '@/vendor/Base/BaseButton.vue';
import { format } from 'date-fns';
import VueDatePicker from '@vuepic/vue-datepicker';
import CardBoxComponentEmpty from '@/vendor/CardBox/CardBoxComponentEmpty.vue';

const store = usePresenceStore();
const styleStore = useStyleStore();


function formatDate(value) {
  if (value) {
    return format(new Date(value), 'yyyy-MM-dd');
  }
}
const reset = () => {
  store.filterQuery = '';
};
onBeforeMount(async () => {
  isLoading.value = true;
  console.log('store');
  await store.fetchAll('today');
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
const formatt = (date) => {
  const day = date.getDate();
  const month = date.getMonth() + 1;
  const year = date.getFullYear();

  return `${day}/${month}/${year}`;
}
const search = (async () =>{
  const date = ref<string>(); 
  const formattedDate = formatDate(query.value);
  if (formattedDate !== undefined) {
    date.value = formattedDate.toString();
    await store.fetchAll(date.value);

  } else {
    console.error('Formatted date is undefined');
    // Handle the case when formattedDate is undefined
  }
});

const searching = ref(false);
const isLoading = ref(false);
const query = ref(formatDate(new Date()));
</script>

<template>
  <SectionMain dir="rtl">
    <SectionTitleLineWithButton  :icon="mdiClipboardList" title=" لإحة الحضور" main>
      
      <BaseButtons type="justify-start lg:justify-end" no-wrap>
        <BaseButton
          label="تسجيل الحضور"
          to="/records"
          color="info"
          class="font-medium ml-2"
          :icon="mdiReceiptTextPlus "
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
    <div class="flex justify-end" v-if="searching">
      <VueDatePicker @clear="reset"   v-if="searching" class="my-4 ml-2 border rounded animate-fade-down animate-duration-[80ms] z-50" v-model="query" :format="formatt" :dark="styleStore.darkMode" />
            <BaseButtons type="justify-start lg:justify-end" no-wrap>
                <BaseButton v-if="searching"
                  label="بحث"
                  color="contrast"
                  to="/records/presences"
                  class="font-medium mr-2"
                  @click="search"
                />
            </BaseButtons>
    </div>
    
    <CardBox v-if="store.filteredList && store.filteredList.length > 0"  class="mb-6" has-table>
      <TablePresences :presences="store.filteredList" :loading="isLoading" />
    </CardBox>
    <CardBox v-else >
      <CardBoxComponentEmpty /> 
    </CardBox>
  </SectionMain>
</template>

<style lang="scss">
:root {
  --dp-input-padding: 10px 30px 12px 12px;
}
@import '@vuepic/vue-datepicker/dist/main.css';

.dp__theme_dark {
  --dp-background-color: #1e293b;
  --dp-text-color: #ffffff;
  --dp-hover-color: #484848;
  --dp-hover-text-color: #ffffff;
  --dp-hover-icon-color: #959595;
  --dp-primary-color: #005cb2;
  --dp-primary-text-color: #ffffff;
  --dp-secondary-color: #a9a9a9;
  --dp-border-color: #374151;
  --dp-menu-border-color: #2d2d2d;
  --dp-border-color-hover: #374151;
  --dp-disabled-color: #4b5563;
  --dp-scroll-bar-background: #212121;
  --dp-scroll-bar-color: #484848;
  --dp-success-color: #00701a;
  --dp-success-color-disabled: #428f59;
  --dp-icon-color: #959595;
  --dp-danger-color: #e53935;
  --dp-highlight-color: rgb(0 92 178 / 20%);
}

.dp__theme_light {
  --dp-background-color: #ffffff;
  --dp-text-color: #212121;
  --dp-hover-color: #f3f3f3;
  --dp-hover-text-color: #212121;
  --dp-hover-icon-color: #959595;
  --dp-primary-color: #1976d2;
  --dp-primary-text-color: #f8f5f5;
  --dp-secondary-color: #c0c4cc;
  --dp-border-color: #374151;
  --dp-menu-border-color: #ddd;
  --dp-border-color-hover: #374151;
  --dp-disabled-color: #f3f4f6;
  --dp-scroll-bar-background: #f3f3f3;
  --dp-scroll-bar-color: #959595;
  --dp-success-color: #00701a;
  --dp-success-color-disabled: #a3d9b1;
  --dp-icon-color: #959595;
  --dp-danger-color: #ff6f60;
  --dp-highlight-color: rgba(25, 118, 210, 0.1);
}
</style>