import type { LoginCredentials, RegisterCredentials } from '@/types/authTypes'
import axios from 'axios'

const API_BASE_URL = 'http://localhost:8000/api/auth'

export async function loginApi(data: LoginCredentials) {
  try {
    const res = await axios.post(`${API_BASE_URL}/login`, {
      email: data.email,
      password: data.password,
    })
    return res.data
  } catch (error) {
    console.error(`Erro na api (login): ${error}`)
    throw error
  }
}

export async function registerApi(data: RegisterCredentials) {
  try {
    const res = await axios.post(`${API_BASE_URL}/signup`, {
      first_name: 'Vinicius',
      last_name: 'Mattera',
      email: data.email,
      telephone: data.phone,
      password: data.password,
      confirm_password: data.password,
    })
    return res.data
  } catch (error) {
    console.error(`Erro na api (register): ${error}`)
    throw error
  }
}
