<script setup lang="ts">
import { ref, computed, onMounted } from 'vue';
import { mdiFileUploadOutline, mdiDeleteForever } from '@mdi/js';
import { apiUrl } from '../../main';
import BaseImg from '@/components/Base/BaseImg.vue';
import BaseIcon from '@/vendor/Base/BaseIcon.vue';
import BaseButton from '@/vendor/Base/BaseButton.vue';

var defaultSvgFile: File;
onMounted(async () => {
  const svgString = (await import('../../../public/assets/images/default.svg?raw')).default;
  defaultSvgFile = new File([svgString], 'default.svg', { type: 'image/svg+xml' });
});

const props = defineProps({
  preview: { type: String, default: '' },
  text: { type: String, default: '' },
  mode: { type: String, default: 'new' },
  modelValue: { type: File },
  disabled: { type: Boolean, default: false },
});

const uniqueId = ref(`dropzone-input-${Date.now() + Math.random()}`);

const emit = defineEmits(['update:modelValue']);

const computedValue = computed({
  get: () => props.modelValue,
  set: (value) => {
    emit('update:modelValue', value);
  },
});

const showPreview = ref<boolean>(!!props.preview);
const newPreview = ref(apiUrl + props.preview);
const active = ref(false);

const previewImage = (event: Event) => {
  const input = event.target as HTMLInputElement;
  if (input.files) {
    computedValue.value = input.files[0];
    const reader = new FileReader();
    reader.onload = (e) => {
      newPreview.value = e.target?.result as string;
    };
    reader.readAsDataURL(input.files[0]);
  }
  showPreview.value = true;
};

const onDrop = (event: DragEvent) => {
  if (event.dataTransfer) {
    active.value = false;
    const input = event.dataTransfer.files[0];
    if (input) {
      computedValue.value = input;
      const reader = new FileReader();
      reader.onload = (ev) => {
        newPreview.value = ev.target?.result as string;
      };
      reader.readAsDataURL(input);
    }
    showPreview.value = true;
  }
};

const reset = () => {
  newPreview.value = '';
  showPreview.value = false;
  computedValue.value = defaultSvgFile;
};
const computedClasses = computed(() => {
  const classes: String[] = [];
  if (active.value) {
    classes.push('active-dropzone');
  }
  if (!showPreview.value) {
    classes.push('empty-dropzone');
  }
  if (showPreview.value) {
    classes.push('dropzone');
  }
  return classes.join(' ');
});
const fileInput = ref<HTMLInputElement | null>(null);

const openFileBrowser = () => {
  fileInput.value?.click();
};
const handleFileChange = (event) => {
  const file = event.target.files[0];
  if (file) {
    // You can handle the selected file here, e.g., preview the image.
    const reader = new FileReader();
    reader.onload = (e) => {
      newPreview.value = e.target?.result as string;
    };
    reader.readAsDataURL(file);
  }
};
</script>

<template>
  <div v-if="mode == 'new'">
    <div
      :class="computedClasses"
      class="bg-[#f2f8f7] dark:bg-gray-800 relative"
      @dragenter.prevent="active = true"
      @dragleave.prevent="active = false"
      @dragover.prevent
      @change="previewImage"
      @drop.prevent="onDrop"
    >
      <div v-if="showPreview" class="full-height full-width">
        <BaseButton
          class="absolute"
          style="top: 0.5rem; right: 0.5rem; z-index: 1"
          color="negative"
          round
          flat
          :icon="mdiDeleteForever"
          @click="reset"
        />
        <div class="flex justify-center q-mt-sm items-center">
          <img v-if="newPreview" :src="newPreview" style="height: 14rem; max-width: 90%" />
          <BaseImg v-else :src="preview" style-addon="height: 14rem; width: 90%" fit="contain" />
        </div>
      </div>

      <div v-else class="idleDropzone">
        <BaseIcon :path="mdiFileUploadOutline" size="5rem" h="full-height" w="max-width" />
        <span>{{ text }}</span>
        <label :for="uniqueId">Browse</label>
        <input
          :id="uniqueId"
          type="file"
          accept="image/*"
          class="dropzoneFile"
          @change="previewImage"
        />
      </div>
    </div>
  </div>

  <div v-else>
    <div
      class="bg-[#f2f8f7] dark:bg-gray-800 dropzone relative"
      @dragenter.prevent="active = true"
      @dragleave.prevent="active = false"
      @dragover.prevent
      @change="previewImage"
      @drop.prevent="onDrop"
      @click="openFileBrowser"
    >
      <div v-if="!newPreview" class="idleDropzone">
        <BaseIcon :path="mdiFileUploadOutline" size="5rem" h="full-height" w="max-width" />
        <span>{{ text }}</span>
        <label :for="uniqueId">Browse</label>
        <input
          :id="uniqueId"
          type="file"
          accept="image/*"
          class="dropzoneFile"
          @change="previewImage"
        />
      </div>
      <div v-else>
        <BaseButton
          class="absolute"
          style="top: 0.5rem; right: 0.5rem; z-index: 1"
          color="negative"
          round
          flat
          :icon="mdiDeleteForever"
          @click="reset"
        />

        <div class="full-height full-width relative">
          <div class="flex justify-center q-mt-sm items-center">
            <img :src="newPreview" style="height: 14rem; max-width: 90%" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
.empty-dropzone {
  width: 49.5 * 2%;
  height: 15rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  row-gap: 20px;
  border-radius: 2%;
  border: 0.12rem dashed #49958d;
  // background-color: #f2f8f7;
  transition: 0.3s ease all;

  label {
    padding: 0.5rem 2rem;
    color: #fff;
    border: 0px;
    background-color: #0d283d;
    border-radius: 0.3rem;
    transition: 0.3s ease all;
  }

  input {
    display: none;
  }
}

.dropzone {
  width: 49.5 * 2%;
  height: 15rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  row-gap: 20px;
  border-radius: 2%;
  border: 0.12rem dashed #49958d;
  // background-color: #fff;
  transition: 0.3s ease all;

  label {
    padding: 0.5rem 2rem;
    color: #fff;
    border: 0px;
    background-color: #0d283d;
    border-radius: 0.3rem;
    transition: 0.3s ease all;
  }

  input {
    display: none;
  }
}

.idleDropzone {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  row-gap: 1.5rem;
  border: 0px;
}

.active-dropzone {
  color: #fff;
  border-color: #fff;
  background-color: #49958d;

  label {
    background-color: #fff;
    color: #41b883;
  }
}
</style>
