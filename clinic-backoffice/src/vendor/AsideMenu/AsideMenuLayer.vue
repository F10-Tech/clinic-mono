<script setup>
import { mdiLogout, mdiClose,mdiAsterisk } from '@mdi/js';
import { computed } from 'vue';
import { useStyleStore } from '@/stores/style';
import AsideMenuList from '@/vendor/AsideMenu/AsideMenuList.vue';
import AsideMenuItem from '@/vendor/AsideMenu/AsideMenuItem.vue';
import BaseIcon from '@/vendor/Base/BaseIcon.vue';

defineProps({
  menu: {
    type: Array,
    required: true,
  },
});

const emit = defineEmits(['menu-click', 'aside-lg-close-click']);

const styleStore = useStyleStore();

const logoutItem = computed(() => ({
  label: 'تسجيل الخروج',
  icon: mdiLogout,
  color: 'info',
  isLogout: true,
}));

const menuClick = (event, item) => {
  emit('menu-click', event, item);
};

const asideLgCloseClick = (event) => {
  emit('aside-lg-close-click', event);
};
</script>

<template>
  <aside 
    id="aside"
    class="lg:py-2 lg:pl-2 w-60 fixed flex z-40 top-0 h-screen transition-position overflow-hidden"
  >
    <div
      :class="styleStore.asideStyle"
      class="lg:rounded-2xl flex-1 flex flex-col overflow-hidden dark:bg-slate-900"
    >
      <div
        :class="styleStore.asideBrandStyle"
        class="flex flex-row h-14 items-center justify-between dark:bg-slate-900"
      >
        <div class="text-center flex lg:text-left lg:pl-6 xl:text-center xl:pl-0 ">
          <div class="mx-10 flex">
            <img src="../.././../public/assets/images/logoo.png"  class="w-10">
          <b class="font-black mt-2 ml-2">Centre Souf</b>
          </div>
          
        </div>
        <button class="hidden lg:inline-block xl:hidden p-3" @click.prevent="asideLgCloseClick">
          <BaseIcon :path="mdiClose" />
        </button>
      </div>
      <div
        :class="styleStore.darkMode ? 'aside-scrollbars-[slate]' : styleStore.asideScrollbarsStyle"
        class="flex-1 overflow-y-auto overflow-x-hidden"
      >
        <AsideMenuList :menu="menu" @menu-click="menuClick" />
      </div>

      <ul>
        <AsideMenuItem :item="logoutItem" @menu-click="menuClick" />
        <!-- @click="agent.logout(router)" -->
      </ul>
    </div>
  </aside>
</template>
