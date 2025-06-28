<script setup lang="ts">
import InputComponent from '@/components/inputComponent.vue'
import { useAuthStore } from '@/stores/auth'
import type { RegisterCredentials } from '@/types/authTypes'
import { Dot, Heart } from 'lucide-vue-next'
import { reactive, ref } from 'vue'
import { isEmail } from 'validator'

const { register } = useAuthStore()

const isLoading = ref(false)

const data = ref({
  username: '',
  email: '',
  phone: '',
  pass: '',
  passConfirm: '',
})

const errors = reactive({
  username: '',
  email: '',
  phone: '',
  pass: '',
  passConfirm: '',
})

function validateInputs() {
  errors.email = ''
  errors.pass = ''
  errors.passConfirm = ''
  errors.phone = ''
  errors.username = ''

  let err = false

  if (!data.value.username) {
    errors.username = 'Nome de usuario nao pode estar vazio!'
    err = true
  } else if (data.value.username.length < 3 || data.value.username.length > 28) {
    errors.username = 'Nome de usuario nao deve ser menor que 3 caracteres e maior que 28'
    err = true
  }

  if (!data.value.email) {
    errors.email = 'Email nao pode estar vazio!'
    err = true
  } else if (!isEmail(data.value.email)) {
    errors.email = 'Utilize um email valido!'
    err = true
  }
  const rawPhone = data.value.phone.replace(/\D/g, '')
  if (!rawPhone) {
    errors.phone = 'Telefone não pode estar vazio!'
    err = true
  } else if (rawPhone.length != 11) {
    errors.phone = 'Telefone deve ter 11 dígitos (incluindo DDD).'
    err = true
  }

  if (!data.value.pass) {
    errors.pass = 'Senha não pode estar vazia!'
    err = true
  } else if (data.value.pass.length < 6) {
    errors.pass = 'A senha deve ter pelo menos 6 caracteres.'
    err = true
  } else if (!/[A-Z]/.test(data.value.pass)) {
    errors.pass = 'A senha deve conter pelo menos uma letra maiúscula.'
    err = true
  } else if (!/[a-z]/.test(data.value.pass)) {
    errors.pass = 'A senha deve conter pelo menos uma letra minúscula.'
    err = true
  } else if (!/[0-9]/.test(data.value.pass)) {
    errors.pass = 'A senha deve conter pelo menos um número.'
    err = true
  }

  if (!data.value.passConfirm) {
    errors.passConfirm = 'Confirmação de senha não pode estar vazia!'
    err = true
  } else if (data.value.passConfirm !== data.value.pass) {
    errors.passConfirm = 'As senhas não coincidem.'
    err = true
  }

  return !err
}

async function tryRegister() {
  console.log(data.value)
  if (validateInputs()) {
    isLoading.value = true
    let dataReg: RegisterCredentials = {
      email: data.value.email,
      password: data.value.pass,
      phone: data.value.phone.replace(/\D/g, ''),
      username: data.value.username,
    }
    try {
      const data = await register(dataReg)
      console.log(data)
    } catch (error) {
      console.error(error)
    } finally {
      isLoading.value = false
    }
  }
}
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
          >Crie sua conta</span
        >
        <span class="text-black font-light dark:text-white text-sm"
          >Junte-se a nossa comunidade!</span
        >
      </div>

      <!-- //inputs section -->
      <div class="w-full p-2 flex flex-col gap-4">
        <InputComponent
          v-model="data.username"
          name="username"
          type="text"
          place-holder="Seu nome de usuario"
          text="Nome de usuario"
        />
        <span v-if="errors.username" class="text-red-400 flex text-sm items-center">
          <Dot /> {{ errors.username }}</span
        >
        <InputComponent
          v-model="data.email"
          name="email"
          type="text"
          place-holder="seuEmail@email.com"
          text="Email"
        />
        <span v-if="errors.email" class="text-red-400 flex text-sm items-center">
          <Dot /> {{ errors.email }}</span
        >
        <InputComponent
          v-model="data.phone"
          name="phone"
          type="tel"
          place-holder="Seu numero de celular"
          text="N. de celular"
          mask="(##) #####-####"
        />
        <span v-if="errors.phone" class="text-red-400 flex text-sm items-center">
          <Dot /> {{ errors.phone }}</span
        >
        <InputComponent
          v-model="data.pass"
          name="pass"
          :pass="true"
          place-holder="Sua senha"
          text="Senha"
        />
        <span v-if="errors.pass" class="text-red-400 flex text-sm items-center">
          <Dot /> {{ errors.pass }}</span
        >
        <InputComponent
          v-model="data.passConfirm"
          name="passConfirm"
          :pass="true"
          place-holder="Confirme sua senha"
          text="Confirme sua senha"
        />
        <span v-if="errors.passConfirm" class="text-red-400 flex text-sm items-center">
          <Dot /> {{ errors.passConfirm }}</span
        >
      </div>

      <!-- // register btn section -->
      <div class="w-full p-4">
        <button
          @click="tryRegister"
          :disabled="isLoading"
          class="w-full py-4 px-6 text-base font-medium rounded-lg bg-blue-400 hover:bg-blue-600 dark:bg-indigo-500 dark:hover:bg-indigo-700 text-white transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-blue-200 dark:focus:ring-indigo-300 disabled:opacity-50 disabled:cursor-not-allowed"
        >
          Registrar-se
        </button>
      </div>
      <!-- // texts above register section -->
      <div class="w-full p-6">
        <span class="flex items-center justify-center mt-2 text-gray-600 dark:text-gray-400 text-xs"
          >Ja tem uma conta?
          <RouterLink
            class="font-medium pl-2 text-blue-500 dark:text-indigo-400 hover:text-blue-600 dark:hover:text-indigo-300 transition-colors"
            to="/login"
            >Entre aqui</RouterLink
          >
        </span>
      </div>
    </div>
  </div>
</template>
