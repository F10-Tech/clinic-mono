<script setup>
import { computed } from 'vue';
import FormCheckRadio from '@/vendor/Form/FormCheckRadio.vue';

const props = defineProps({
  options: {
    type: Object,
    default: () => {}
  },
  name: {
    type: String,
    required: true
  },
  type: {
    type: String,
    default: 'checkbox',
    validator: (value) => ['checkbox', 'radio', 'switch'].includes(value)
  },
  componentClass: {
    type: String,
    default: null
  },
  isColumn: Boolean,
  modelValue: {
    type: [Array, String, Number, Object, Boolean],
    default: null
  }
})

const emit = defineEmits(['update:modelValue'])

const computedValue = computed({
  get: () => props.modelValue,
  set: (value) => {
    emit('update:modelValue', value)
  }
})
</script>

<template>
  <div class="flex justify-start flex-wrap -mb-3" :class="{ 'flex-col': isColumn }">
    <FormCheckRadio
     dir="ltr"
      v-for="option in options"
      :key="option.value"
      v-model="computedValue"
      :type="type"
      :name="name"
      :input-value="option.value"
      :label="option.label"
      :class="componentClass"
      class="mr-6 mb-3 last:mr-0"
    />
  </div>
</template>