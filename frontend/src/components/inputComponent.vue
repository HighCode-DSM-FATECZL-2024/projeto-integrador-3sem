<template>
  <div v-if="!pass" class="w-full flex flex-col gap-4">
    <label :for="`${name}id`" class="block text-sm font-medium text-gray-800 dark:text-gray-200">{{
      text
    }}</label>
    <input
      v-if="mask == undefined"
      v-model="model"
      class="w-full px-4 py-4 text-base bg-white dark:bg-gray-800 border-2 rounded-lg text-gray-800 dark:text-gray-200 placeholder-gray-500 dark:placeholder-gray-400 transition-colors duration-200 focus:outline-none focus:ring-0 border-gray-300 dark:border-gray-600 focus:border-blue-500 dark:focus:border-indigo-500"
      :placeholder="`${placeHolder}`"
      :type="`${type}`"
      :name="`${name}`"
      :id="`${name}id`"
    />
    <MaskInput
      v-else
      v-model="model"
      class="w-full px-4 py-4 text-base bg-white dark:bg-gray-800 border-2 rounded-lg text-gray-800 dark:text-gray-200 placeholder-gray-500 dark:placeholder-gray-400 transition-colors duration-200 focus:outline-none focus:ring-0 border-gray-300 dark:border-gray-600 focus:border-blue-500 dark:focus:border-indigo-500"
      :placeholder="`${placeHolder}`"
      :type="`${type}`"
      :name="`${name}`"
      :id="`${name}id`"
      :mask="mask"
    />
  </div>
  <div v-if="pass" class="w-full flex flex-col gap-4">
    <label :for="`${name}id`" class="block text-sm font-medium text-gray-800 dark:text-gray-200">{{
      text
    }}</label>
    <div class="relative">
      <input
        v-model="model"
        class="w-full px-4 py-4 text-base bg-white dark:bg-gray-800 border-2 rounded-lg text-gray-800 dark:text-gray-200 placeholder-gray-500 dark:placeholder-gray-400 transition-colors duration-200 focus:outline-none focus:ring-0 border-gray-300 dark:border-gray-600 focus:border-blue-500 dark:focus:border-indigo-500"
        :placeholder="`${placeHolder}`"
        :type="showPass ? 'text' : 'password'"
        :name="`${name}`"
        :id="`${name}id`"
      />
      <button
        @click="showPass = !showPass"
        class="absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-500 dark:text-gray-400 hover:text-gray-700 dark:hover:text-gray-300 transition-colors"
      >
        <Component :is="showPass ? EyeOff : Eye" />
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { Eye, EyeOff } from 'lucide-vue-next'
import { ref } from 'vue'

const showPass = ref(false)
const model = defineModel({
  type: String,
  default: '',
  required: true,
})
const props = defineProps({
  pass: { type: Boolean, default: false },
  name: { type: String, required: true },
  type: { type: String, required: false },
  text: { type: String, required: true },
  placeHolder: { type: String, required: true },
  mask: { type: String, default: undefined },
})
</script>
