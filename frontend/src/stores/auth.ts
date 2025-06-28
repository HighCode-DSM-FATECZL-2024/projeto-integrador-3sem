import { loginApi, registerApi } from '@/services/authService'
import type { LoginCredentials, RegisterCredentials } from '@/types/authTypes'
import { defineStore } from 'pinia'
import { computed, ref } from 'vue'

export const useAuthStore = defineStore('auth', () => {
  const user = ref('')
  const token = ref<string | null>(localStorage.getItem('token'))
  const isAuthenticated = computed(() => !!token.value)

  async function login(credentials: LoginCredentials) {
    try {
      const data = await loginApi(credentials)
      console.log(data)
      return data
    } catch (error) {
      user.value = ''
      token.value = null
      localStorage.removeItem('token')
    }
  }

  async function register(credentials: RegisterCredentials) {
    try {
      const data = await registerApi(credentials)
      console.log(data)
    } catch (error) {
      user.value = ''
      token.value = null
      localStorage.removeItem('token')
    }
  }

  return {
    user,
    token,
    isAuthenticated,
    login,
    register,
  }
})
