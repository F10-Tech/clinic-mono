import { createApp } from 'vue';
import { createPinia } from 'pinia';
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate';

import App from './App.vue';
import router from './router';
import { useStyleStore } from '@/stores/style';
import { darkModeKey, styleKey } from '@/config';

import './css/main.css';

export const apiUrl = import.meta.env.MODE === 'production' ? '' : import.meta.env.VITE_API_URL;
/* Init Pinia */
const pinia = createPinia();
pinia.use(piniaPluginPersistedstate);

/* Create Vue app */
const app = createApp(App);
app.use(pinia);
app.use(router);
router.isReady().then(() => app.mount('#app'));

/* Init Pinia stores */
const styleStore = useStyleStore(pinia);

/* App style */
styleStore.setStyle(localStorage[styleKey] ?? 'basic');

/* Dark mode */
if (
  (!localStorage[darkModeKey] && window.matchMedia('(prefers-color-scheme: dark)').matches) ||
  localStorage[darkModeKey] === '1'
) {
  styleStore.setDarkMode(true);
}

/* Default title tag */
const defaultDocumentTitle = 'Khfif Backoffice';

/* Set document title from route meta */
router.afterEach((to) => {
  document.title = to.meta?.title
    ? `${to.meta.title} — ${defaultDocumentTitle}`
    : defaultDocumentTitle;
});
