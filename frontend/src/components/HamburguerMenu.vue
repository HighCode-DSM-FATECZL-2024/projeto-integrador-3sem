<template>
  <div class="relative flex lg:hidden items-center justify-end z-40">
    <div
      @click="toggleMenu"
      class="w-12 h-12 flex items-center cursor-pointer justify-center p-2 bg-blue-500 dark:bg-indigo-400 rounded-lg border-2 hover:shadow-xl hover:-translate-y-[2px] transition-shadow transition-transform duration-300 border-blue-700"
    >
      <Component :is="menuOpen ? X : Menu" class="text-gray-700" />
    </div>
  </div>
  <div
    v-show="menuOpen"
    class="fixed z-20 top-0 right-0 h-full w-48 md:w-80 pt-16 bg-blue-400 dark:bg-indigo-500 lg:hidden"
  >
    <RouterLink
      to="/"
      class="w-full h-24 px-4 py-8 group flex gap-8 hover:-translate-x-[2px] hover:text-blue-600 dark:hover:text-blue-400 justify-around transition-transform duration-300"
      active-class="-translate-x-[2px]"
    >
      <div class="w-1/4 flex justify-center">
        <Home class="w-8 h-auto" />
      </div>
      <span
        class="border-b border-gray-600 w-3/4 text-xs md:text-md font-semibold text-gray-800 dark:text-gray-100 group-hover:text-blue-600 dark:group-hover:text-blue-400"
        >Pagina inicial</span
      >
    </RouterLink>
    <RouterLink
      to="/chat"
      active-class="-translate-x-[2px]"
      class="w-full group h-24 px-4 py-8 flex gap-8 hover:-translate-x-[2px] hover:text-blue-600 dark:hover:text-blue-400 justify-around transition-transform duration-300"
    >
      <div class="w-1/4 flex justify-center">
        <BotMessageSquare class="w-8 h-auto" />
      </div>
      <span
        class="border-b border-gray-600 w-3/4 text-xs md:text-md  font-semibold text-gray-800 dark:text-gray-100 group-hover:text-blue-600 dark:group-hover:text-blue-400"
        >Converse com a IA</span
      >
    </RouterLink>
    <RouterLink
      to="/login"
      active-class="-translate-x-[2px]"
      class="w-full group h-24 px-4 py-8 flex gap-8 hover:-translate-x-[2px] hover:text-blue-600 dark:hover:text-blue-400 justify-around transition-transform duration-300"
    >
      <div class="w-1/4 flex justify-center">
        <User class="w-8 h-auto" />
      </div>
      <span
        class="border-b border-gray-600 w-3/4 text-xs md:text-md  font-semibold text-gray-800 dark:text-gray-100 group-hover:text-blue-600 dark:group-hover:text-blue-400"
        >Login</span
      >
    </RouterLink>
    <RouterLink
      to="/register"
      active-class="-translate-x-[2px]"
      class="w-full group h-24 px-4 py-8 flex gap-8 hover:-translate-x-[2px] hover:text-blue-600 dark:hover:text-blue-400 justify-around transition-transform duration-300"
    >
      <div class="w-1/4 flex justify-center">
        <UserPlus class="w-8 h-auto" />
      </div>
      <span
        class="border-b border-gray-600 w-3/4 text-xs md:text-md  font-semibold text-gray-800 dark:text-gray-100 group-hover:text-blue-600 dark:group-hover:text-blue-400"
        >Registrar-se</span
      >
    </RouterLink>
    <div
      @click="switchTheme"
      class="w-full h-12 gap-6 dark:bg-indigo-400 text-md font-semibold text-gray-800 dark:text-gray-100 group-hover:text-blue-600 dark:group-hover:text-blue-400 flex items-center cursor-pointer justify-center p-2 bg-blue-500 border-y-2 hover:shadow-xl hover:-translate-y-[2px] transition-shadow transition-transform duration-300 border-blue-700"
    >
      <component
        :class="[darkTheme ? 'text-white' : 'text-black']"
        :size="24"
        :is="darkTheme ? Sun : Moon"
      />
      Trocar tema
    </div>
  </div>
  <div
    v-if="menuOpen"
    @click="toggleMenu"
    class="fixed top-16 inset-0 bg-black bg-opacity-50 lg:hidden z-10"
  ></div>
</template>

<script lang="ts" setup>
import { useThemeStore } from '@/stores/theme'
import { Home, Menu, X, BotMessageSquare, Sun, Moon, User, UserPlus } from 'lucide-vue-next'
import { storeToRefs } from 'pinia'
import { ref, watchEffect } from 'vue'
const { switchTheme } = useThemeStore()
const { darkTheme } = storeToRefs(useThemeStore())

const menuOpen = ref(false)

const toggleMenu = () => {
  menuOpen.value = !menuOpen.value
}

watchEffect(() => {
  if (typeof window != undefined) {
    const handleResize = () => {
      if (window.innerWidth > 1024 && menuOpen.value) {
        menuOpen.value = false
      }
    }

    window.addEventListener('resize', handleResize)
    return () => {
      window.removeEventListener('resize', handleResize)
    }
  }
})
</script>
