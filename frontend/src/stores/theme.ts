import { ref, watch } from 'vue'
import { defineStore } from 'pinia'

export const useThemeStore = defineStore('theme', () => {
  const darkTheme = ref(false)

  function switchTheme() {
    darkTheme.value = !darkTheme.value
  }

  const initTheme = () => {
    const savedTheme = localStorage.getItem('theme')
    if (savedTheme) {
      darkTheme.value = savedTheme === 'dark'
    } else {
      darkTheme.value = window.matchMedia('(prefers-color-scheme: dark)').matches
    }
  }

  watch(
    darkTheme,
    (newVal) => {
      if (newVal) {
        document.documentElement.classList.add('dark')
      } else {
        document.documentElement.classList.remove('dark')
      }

      localStorage.setItem('theme', newVal ? 'dark' : 'light')
    },
    { immediate: true },
  )

  return { darkTheme, switchTheme, initTheme }
})
