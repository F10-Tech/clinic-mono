<script setup>
import { computed } from 'vue';
import { colorsBgLight, colorsOutline } from '@/colors';
import PillTagPlain from '@/vendor/PillTag/PillTagPlain.vue';

const props = defineProps({
  label: {
    type: String,
    required: true,
  },
  color: {
    type: String,
    required: true,
  },
  icon: {
    type: String,
    default: null,
  },
  small: Boolean,
  outline: Boolean,
});
const typesMap = {
  CANCELLED: { label: 'CANCELLED', color: 'warning' },
  COMPLETED: { label: 'COMPLETED', color: 'success' },
  INPROGRESS: { label: 'IN PROGRESS', color: 'info' },
  REJECTED: { label: 'REJECTED', color: 'danger' },
  PENDING: { label: 'PENDING', color: 'contrast' },
};
const componentClass = computed(() => [
  props.small ? 'py-1 px-3' : 'py-1.5 px-4',
  props.outline ? colorsOutline[props.color] : colorsBgLight[status.value.color],
]);
const status = computed(() => {
  const defaultValue = { label: 'Unknown', color: 'dark' };
  const value = props.label;
  return typesMap[value] || defaultValue;
});
</script>

<template>
  <PillTagPlain
    class="border rounded-full"
    :class="componentClass"
    :icon="icon"
    :label="status.label"
    :small="small"
  />
</template>
