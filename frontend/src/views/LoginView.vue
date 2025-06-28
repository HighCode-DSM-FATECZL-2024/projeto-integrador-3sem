<script setup lang="ts">
import InputComponent from '@/components/inputComponent.vue'
import { Heart } from 'lucide-vue-next'
import { ref } from 'vue'

const data = ref({
  email: '',
  pass: '',
})
</script>

<template>
  <div
    class="min-w-screen min-h-[calc(100dvh-4rem)] flex p-8 justify-center items-center dark:bg-gray-800"
  >
    <div
      class="w-full md:w-1/2 lg:w-1/3 p-2 py-6 bg-gray-100 dark:bg-gray-600 rounded-sm shadow-xl"
    >
      <!-- //welcome section -->
      <div class="w-full flex flex-col items-center justify-center">
        <Heart class="w-16 h-16 bg-blue-400 dark:bg-indigo-500 text-white p-4 rounded-full mb-4" />
        <span class="text-black font-normal dark:text-white text-md tracking-wider"
          >Bem-vindo de volta</span
        >
        <span class="text-black font-light dark:text-white text-sm"
          >Entre na sua conta para continuar</span
        >
      </div>

      <!-- //inputs section -->
      <div class="w-full p-2 flex flex-col gap-8">
        <InputComponent
          v-model="data.email"
          name="email"
          type="email"
          place-holder="seuEmail@email.com"
          text="Email"
        />
        <InputComponent
          v-model="data.pass"
          name="pass"
          :pass="true"
          place-holder="Sua senha"
          text="Senha"
        />
      </div>

      <!-- // login btn section -->
      <div class="w-full p-4">
        <button
          class="w-full py-4 px-6 text-base font-medium rounded-lg bg-blue-400 hover:bg-blue-600 dark:bg-indigo-500 dark:hover:bg-indigo-700 text-white transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-blue-200 dark:focus:ring-indigo-300 disabled:opacity-50 disabled:cursor-not-allowed"
        >
          Login
        </button>
      </div>
      <!-- // texts above login section -->
      <div class="w-full p-6">
        <RouterLink
          to="/forgot-password"
          class="text-sm flex justify-center items-center text-gray-600 dark:text-gray-400 hover:text-blue-500 dark:hover:text-indigo-400 transition-colors"
          >Esqueceu sua senha?</RouterLink
        >
        <span class="flex items-center justify-center mt-8 text-gray-600 dark:text-gray-400 text-xs"
          >Nao tem uma conta?
          <RouterLink
            class="font-medium pl-2 text-blue-500 dark:text-indigo-400 hover:text-blue-600 dark:hover:text-indigo-300 transition-colors"
            to="/register"
            >Registre-se</RouterLink
          >
        </span>
      </div>
    </div>
  </div>
</template>
