<script setup>
import { reactive, ref } from 'vue';
import { useRouter } from 'vue-router';
import { mdiAccount, mdiAsterisk } from '@mdi/js';
import { LoopingRhombusesSpinner } from 'epic-spinners';

import { useAgentStore } from '@/stores';
import SectionFullScreen from '@/vendor/Section/SectionFullScreen.vue';
import CardBox from '@/vendor/CardBox/CardBox.vue';
import FormCheckRadio from '@/vendor/Form/FormCheckRadio.vue';
import FormField from '@/vendor/Form/FormField.vue';
import FormControl from '@/vendor/Form/FormControl.vue';
import BaseButton from '@/vendor/Base/BaseButton.vue';
import BaseButtons from '@/vendor/Base/BaseButtons.vue';
import LayoutGuest from '@/layouts/LayoutGuest.vue';

const agentStore = useAgentStore();

const isLoading = ref(false); // Initially, set loading to true
const errorMessage = ref(''); // To store any error messages from the login attempt
const form = reactive({
  login: '',
  pass: '',
  remember: true,
});

const router = useRouter();

const submit = async () => {
  isLoading.value = true;
  try {
    await agentStore.login(form.login, form.pass);
    router.push('/services');
  } catch (error) {
    errorMessage.value = 'Failed to login. Please check your credentials.';
  } finally {
    isLoading.value = false; // Ensure spinner is deactivated whether login succeeds or fails
  }
};
</script>

<template>
  <LayoutGuest>
    <div v-if="isLoading" class="flex justify-center items-center h-screen">
      <looping-rhombuses-spinner :animation-duration="1500" :rhombus-size="20" color="#fff" />
    </div>
    <div v-else>
      <SectionFullScreen v-slot="{ cardClass }" bg="purplePink">
        <CardBox :class="cardClass" is-form @submit.prevent="submit">
          <div v-if="errorMessage" class="text-red-500 mb-4">{{ errorMessage }}</div>
          <FormField label="Login" help="Please enter your login">
            <FormControl
              v-model="form.login"
              :icon="mdiAccount"
              label="login"
              autocomplete="username"
            />
          </FormField>

          <FormField label="Password" help="Please enter your password">
            <FormControl
              v-model="form.pass"
              :icon="mdiAsterisk"
              type="password"
              label="password"
              autocomplete="current-password"
            />
          </FormField>

          <FormCheckRadio
            v-model="form.remember"
            name="remember"
            label="Remember"
            :input-value="true"
          />

          <template #footer>
            <BaseButtons>
              <BaseButton type="submit" color="info" label="Login" />
              <BaseButton to="/" color="info" outline label="Back" />
            </BaseButtons>
          </template>
        </CardBox>
      </SectionFullScreen>
    </div>
  </LayoutGuest>
</template>
