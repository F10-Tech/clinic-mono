<script setup>
import { mdiAccountTieOutline } from '@mdi/js';
import SectionMain from '@/vendor/Section/SectionMain.vue';
import CardBox from '@/vendor/CardBox/CardBox.vue';
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue';
import SectionTitleLineWithButton from '@/vendor/Section/SectionTitleLineWithButton.vue';
import BaseButton from '@/vendor/Base/BaseButton.vue';
</script>

<template>
  <LayoutAuthenticated>
    <SectionMain>
      <SectionTitleLineWithButton :icon="mdiAccountTieOutline" title="staff" main>
        <BaseButton target="_blank" label="Create User" color="contrast" small />
      </SectionTitleLineWithButton>

      <CardBox class="mb-6" has-table>
        <!-- <TableUsers /> -->
      </CardBox>
    </SectionMain>
  </LayoutAuthenticated>
</template>
