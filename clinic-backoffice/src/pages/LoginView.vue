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
    errorMessage.value = 'خطأ في اسم المستخدم أو كلمة المرور';
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
      <SectionFullScreen class="block"  dir="rtl" v-slot="{ cardClass }" bg="purplePink">
        <div></div>
        <CardBox :class="cardClass" is-form @submit.prevent="submit">
          <div v-if="errorMessage" class="text-red-500 mb-4">{{ errorMessage }}</div>
          <FormField label="الأسم" help="أدخل الأسم">
            <FormControl
              v-model="form.login"
              :icon="mdiAccount"
              label="login"
              autocomplete="username"
            />
          </FormField>

          <FormField label="كلمة المرور" help="ادخل كلمة السر">
            <FormControl
              v-model="form.pass"
              :icon="mdiAsterisk"
              type="password"
              label="password"
              autocomplete="current-password"
            />
          </FormField>


          <template #footer>
            <BaseButtons>
              <BaseButton type="submit" color="info" label="الدخول" />
            </BaseButtons>
            <div class=" text-slate-600">
              تم التطوير بواسطة F10 Tech
            </div>
          </template>
        </CardBox>
        
      </SectionFullScreen>
    </div>
  </LayoutGuest>
</template>
