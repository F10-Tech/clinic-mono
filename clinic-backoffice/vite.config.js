import { fileURLToPath, URL } from 'node:url';

import { defineConfig, loadEnv } from 'vite';
import vue from '@vitejs/plugin-vue';

export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd(), '');
  return {
    server: {
      port: Number(env.PORT) || 5173,
    },
    plugins: [vue()],
    resolve: {
      alias: {
        '@': fileURLToPath(new URL('./src', import.meta.url)),
      },
    },
  };
});


   // "dev": "vite --host spa.earthmeta.ai --port 443",
    // "view": "vite preview --host spa.earthmeta.ai",
    // 127.0.0.1 spa.earthmeta.ai