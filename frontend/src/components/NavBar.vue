<template>
  <nav
    class="min-w-screen min-h-16 bg-blue-400 dark:bg-indigo-500 justify-between flex px-12 relative z-20"
  >
    <div class="w-1/2 flex justify-start items-center">a</div>
    <div class="hidden w-1/2 lg:flex items-center justify-end items-center">
      <div
        @click="switchTheme"
        class="w-12 h-12 flex items-center cursor-pointer justify-center p-2 bg-blue-500 rounded-lg border-2 hover:shadow-xl hover:-translate-y-[2px] transition-shadow transition-transform duration-300 border-blue-700"
      >
        <component
          :class="[darkTheme ? 'text-white' : 'text-black']"
          :size="24"
          :is="darkTheme ? Sun : Moon"
        />
      </div>
    </div>
    <HamburguerMenu />
  </nav>
</template>

<script setup lang="ts">
import { Sun, Moon } from 'lucide-vue-next'
import { useThemeStore } from '@/stores/theme'
import HamburguerMenu from './HamburguerMenu.vue'
import { storeToRefs } from 'pinia'
const { switchTheme } = useThemeStore()
const { darkTheme } = storeToRefs(useThemeStore())
</script>
