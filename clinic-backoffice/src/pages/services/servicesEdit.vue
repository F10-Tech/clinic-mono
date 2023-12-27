<script setup lang="ts">
import { LoopingRhombusesSpinner } from 'epic-spinners';
import { ref, onUnmounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useServicesStore, useAgentStore } from '@/stores';
import type { Service } from '@/models/service';
import SectionMain from '@/vendor/Section/SectionMain.vue';
import CardBox from '@/vendor/CardBox/CardBox.vue';
import FormField from '@/vendor/Form/FormField.vue';
import FormControl from '@/vendor/Form/FormControl.vue';
import BaseDivider from '@/vendor/Base/BaseDivider.vue';
import BaseButton from '@/vendor/Base/BaseButton.vue';
import BaseButtons from '@/vendor/Base/BaseButtons.vue';
import DropZone from '@/components/Base/DropZone.vue';
import CardBoxModal from '@/vendor/CardBox/CardBoxModal.vue';
import FormCheckRadioGroup from '@/vendor/Form/FormCheckRadioGroup.vue';
import SectionTitleLineWithButton from '@/vendor/Section/SectionTitleLineWithButton.vue';
import NotificationBar from '@/vendor/NotificationBar/NotificationBar.vue';

const store = useServicesStore();
const agent = useAgentStore();

const route = useRoute();
const router = useRouter();
const modalActive = ref(false);
const image_light = ref<File | undefined>(undefined);
const image_dark = ref<File | undefined>(undefined);
const isLoading = ref(true); // Initially, set loading to true

store.editedId = route.params.id.toString();
const service = ref<Service>({
  name_EN: store.edited?.name_EN,
  description_EN: store.edited?.description_EN,
  name_FR: store.edited?.name_FR,
  description_FR: store.edited?.description_FR,
  name_AR: store.edited?.name_AR,
  description_AR: store.edited?.description_AR,
  image_light: store.edited?.image_light,
  image_dark: store.edited?.image_dark,
  is_active: store.edited?.is_active,
} as unknown as Service);
isLoading.value = false;
onUnmounted(() => {
  store.editedId = undefined;
});
const deleteService = async () => {
  const isDeleted = await store.deleteService(store.editedId!);
  if (isDeleted) {
    formStatusSubmit();
    setTimeout(function () {
      BackHim();
      router.push('/services');
    }, agent.timeToKill);
  } else {
    formStatusCurrent.value = 2;
    setTimeout(function () {
      BackHim();
    }, agent.timeToKill);
  }
};
const submit = async () => {
  const isUpdated = await store.patch(
    store.editedId!,
    service.value,
    image_dark.value,
    image_light.value,
  );
  if (isUpdated) {
    formStatusSubmit();
    setTimeout(function () {
      BackHim();
      router.push('/services');
    }, agent.timeToKill);
  } else {
    formStatusCurrent.value = 2;
    setTimeout(function () {
      BackHim();
    }, agent.timeToKill);
  }
};
const BackHim = () => {
  formStatusCurrent.value = 0;
};

const formStatusWithHeader = ref(true);

const formStatusCurrent = ref(0);

const formStatusOptions = ['info', 'success', 'danger', 'warning'];

const formStatusSubmit = () => {
  formStatusCurrent.value = formStatusOptions[formStatusCurrent.value + 1]
    ? formStatusCurrent.value + 1
    : 0;
};
</script>

<template>
  <div v-if="isLoading" class="flex justify-center items-center h-screen">
    <looping-rhombuses-spinner :animation-duration="1500" :rhombus-size="20" color="#fff" />
  </div>

  <div v-else>
    <SectionMain v-if="service">
      <SectionTitleLineWithButton title="Service Profile" main />
      <CardBoxModal
        v-model="modalActive"
        title="Please confirm the delete"
        button-label="Delete"
        button-cancel-label="Cancel"
        button="danger"
        has-cancel
        @confirm="deleteService"
      />
      <CardBox form @submit.prevent="submit">
        <div class="flex">
          <FormField label="English Name" class="mr-3 w-2/5">
            <FormControl v-model="service.name_EN" type="text" placeholder="Name in English" />
          </FormField>
          <FormField label="English Desciption" class="w-3/5">
            <FormControl
              v-model="service.description_EN"
              type="text"
              placeholder="Description in English"
            />
          </FormField>
        </div>
        <div class="flex">
          <FormField label="French Name" class="mr-3 w-2/5">
            <FormControl v-model="service.name_FR" type="text" placeholder="Nom en français" />
          </FormField>
          <FormField label="French Desciption" class="w-3/5">
            <FormControl
              v-model="service.description_FR"
              type="text"
              placeholder="Description en French"
            />
          </FormField>
        </div>
        <div class="flex">
          <FormField label="Arabic Name" class="mr-3 w-2/5">
            <FormControl
              v-model="service.name_AR"
              type="text"
              placeholder="الاسم بالعربية"
              :style="{ direction: 'rtl' }"
            />
          </FormField>
          <FormField label="Arabic Desciption" class="w-3/5">
            <FormControl
              v-model="service.description_AR"
              type="text"
              placeholder="الوصف بالعربية"
              :style="{ direction: 'rtl' }"
            />
          </FormField>
        </div>

        <div class="flex justify-between">
          <DropZone
            v-model="image_light"
            :preview="service.image_light"
            class="w-[95%]"
            text="Drop light image here"
            mode="edit"
          />
          <DropZone
            v-model="image_dark"
            :preview="service.image_dark"
            class="w-[95%]"
            text="Drop dark image here"
            mode="edit"
          />
        </div>
        <BaseDivider />

        <BaseButtons class="flex justify-between">
          <FormCheckRadioGroup
            v-model="service.is_active"
            type="switch"
            name="notifications-switch"
            :options="{ outline: 'Active' }"
          />
          <div>
            <BaseButton color="danger" label="Delete" @click="modalActive = true" />
            <BaseButton type="submit" color="success" label="Submit" @click="submit" />
          </div>
        </BaseButtons>
      </CardBox>
      <NotificationBar
        v-if="formStatusCurrent"
        :color="formStatusOptions[formStatusCurrent]"
        :is-placed-with-header="formStatusWithHeader"
        class="animate-fade-left w-96 right-10 top-20 fixed"
      >
        <span>
          <b class="capitalize">{{ formStatusOptions[formStatusCurrent] }}</b>
        </span>
      </NotificationBar>
    </SectionMain>
  </div>
</template>
