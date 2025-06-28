import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { MaskInput } from 'vue-3-mask'

import App from './App.vue'
import router from './router'

const app = createApp(App)

app.component('MaskInput', MaskInput)
app.use(createPinia())
app.use(router)

app.mount('#app')
