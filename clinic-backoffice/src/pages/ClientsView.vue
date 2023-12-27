<script setup>
import { mdiAccountGroupOutline } from '@mdi/js';
import SectionMain from '@/vendor/Section/SectionMain.vue';
import TableClients from '@/components/Tables/TableClients.vue';
import CardBox from '@/vendor/CardBox/CardBox.vue';
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue';
import SectionTitleLineWithButton from '@/vendor/Section/SectionTitleLineWithButton.vue';
import BaseButton from '@/vendor/Base/BaseButton.vue';
</script>

<template>
  <LayoutAuthenticated>
    <SectionMain>
      <SectionTitleLineWithButton :icon="mdiAccountGroupOutline" title="Clients" main>
        <BaseButton target="_blank" label="Create Client" color="contrast" small />
      </SectionTitleLineWithButton>

      <CardBox class="mb-6" has-table>
        <!-- <TableClients /> -->
      </CardBox>
    </SectionMain>
  </LayoutAuthenticated>
</template>
