<script setup>
import { mdiForwardburger, mdiBackburger, mdiMenu } from '@mdi/js';
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import menuAside from '@/menuAside';
import menuNavBar from '@/menuNavBar';
import { useMainStore } from '@/stores/main';
import { useStyleStore } from '@/stores/style';
import BaseIcon from '@/vendor/Base/BaseIcon.vue';
import NavBar from '@/vendor/NavBar/NavBar.vue';
import NavBarItemPlain from '@/vendor/NavBar/NavBarItemPlain.vue';
import AsideMenu from '@/vendor/AsideMenu/AsideMenu.vue';
import { useAgentStore } from '@/stores/models/agent';
import CardBoxModal from '@/vendor/CardBox/CardBoxModal.vue';

const agent = useAgentStore();

useMainStore().setUser({
  name: `${agent.firstName} ${agent.lastName}`,
  email: agent.email,
  avatar: `https://api.dicebear.com/6.x/avataaars/svg?seed=${agent.firstName}${agent.lastName}`,
});

const modalActive = ref(false);

const layoutAsidePadding = 'xl:pl-60';

const styleStore = useStyleStore();

const router = useRouter();

const isAsideMobileExpanded = ref(false);
const isAsideLgActive = ref(false);

router.beforeEach(() => {
  isAsideMobileExpanded.value = false;
  isAsideLgActive.value = false;
});

const menuClick = (event, item) => {
  if (item.isToggleLightDark) {
    styleStore.setDarkMode();
  }

  if (item.isLogout) {
    modalActive.value = true;
  }
};
</script>

<template>
  <div
    :class="{
      dark: styleStore.darkMode,
      'overflow-hidden lg:overflow-visible': isAsideMobileExpanded,
    }"
  >
    <div
      :class="[layoutAsidePadding, { 'ml-60 lg:ml-0': isAsideMobileExpanded }]"
      class="pt-14 min-h-screen w-screen transition-position lg:w-auto bg-gray-50 dark:bg-slate-800 dark:text-slate-100"
    >
      <NavBar
        :menu="menuNavBar"
        :class="[layoutAsidePadding, { 'ml-60 lg:ml-0': isAsideMobileExpanded }]"
        @menu-click="menuClick"
      >
        <NavBarItemPlain
          display="flex lg:hidden"
          @click.prevent="isAsideMobileExpanded = !isAsideMobileExpanded"
        >
          <BaseIcon :path="isAsideMobileExpanded ? mdiBackburger : mdiForwardburger" size="24" />
        </NavBarItemPlain>
        <NavBarItemPlain display="hidden lg:flex xl:hidden" @click.prevent="isAsideLgActive = true">
          <BaseIcon :path="mdiMenu" size="24" />
        </NavBarItemPlain>
      </NavBar>

      <CardBoxModal
        v-model="modalActive"
        title="Are you sure you want to Logout ?"
        button-label="Logout"
        button-cancel-label="Cancel"
        button="danger"
        has-cancel
        @confirm="router.push({ name: 'logout' })"
      >
      </CardBoxModal>

      <AsideMenu
        :is-aside-mobile-expanded="isAsideMobileExpanded"
        :is-aside-lg-active="isAsideLgActive"
        :menu="menuAside"
        @menu-click="menuClick"
        @aside-lg-close-click="isAsideLgActive = false"
      />
      <slot />
    </div>
  </div>
</template>
