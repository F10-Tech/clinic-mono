<script setup lang="ts">
import { apiUrl } from '@/main';
import { computed, type PropType } from 'vue';

type FitType = 'cover' | 'fill' | 'contain' | 'none' | 'scale-down' | undefined;

const props = defineProps({
  src: { type: String },
  api: {
    type: Boolean,
    default: true,
  },
  alt: {
    type: String,
    default: 'image',
  },
  styleAddon: {
    type: String,
    default: 'width: 6vh',
  },
  fit: {
    type: String as PropType<FitType>,
    default: 'cover',
  },
});

let newSrc = computed(() =>
  props.api && props.src
    ? apiUrl + props.src
    : props.src != null
    ? props.src
    : '/assets/images/favicon.png',
);
</script>

<template>
  <img :src="newSrc" :alt="alt" :style="styleAddon" spinner-color="blue-grey" :fit="fit" />
</template>
