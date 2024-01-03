<script setup>
import { mdiCog } from '@mdi/js'
import CardBox from '@/vendor/CardBox/CardBox.vue'
import NumberDynamic from '@/vendor/NumberDynamic.vue'
import BaseIcon from '@/vendor/Base/BaseIcon.vue'
import BaseLevel from '@/vendor/Base/BaseLevel.vue'
import PillTagTrend from '@/vendor/PillTag/PillTagTrend.vue'
import BaseButton from '@/vendor/Base/BaseButton.vue'

defineProps({
  number: {
    type: Number,
    default: 0
  },
  icon: {
    type: String,
    default: null
  },
  prefix: {
    type: String,
    default: null
  },
  suffix: {
    type: String,
    default: null
  },
  label: {
    type: String,
    default: null
  },
  color: {
    type: String,
    default: null
  },
  trend: {
    type: String,
    default: null
  },
  trendType: {
    type: String,
    default: null
  }
})
</script>

<template>
  <CardBox>
    <BaseLevel v-if="trend" class="mb-3" mobile>
      <PillTagTrend :trend="trend" :trend-type="trendType" small />
      <BaseButton :icon="mdiCog" icon-w="w-4" icon-h="h-4" color="lightDark" small />
    </BaseLevel>
    <BaseLevel mobile>
      <div>
        <h3 class="text-lg leading-tight text-gray-500 dark:text-slate-400">
          {{ label }}
        </h3>
        <h1 class="text-3xl leading-tight font-semibold flex">
          <NumberDynamic :value="number" :prefix="prefix" :suffix="suffix" />  <span class="mx-2"> دج </span>
        </h1>
      </div>
      <BaseIcon v-if="icon" :path="icon" size="48" w="" h="h-16" :class="color" />
    </BaseLevel>
  </CardBox>
</template>