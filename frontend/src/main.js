import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import { library } from '@fortawesome/fontawesome-svg-core'
import '@fortawesome/fontawesome-svg-core/styles.css'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faListCheck } from '@fortawesome/free-solid-svg-icons'

library.add(faListCheck)

const app = createApp(App)

app.component('fa', FontAwesomeIcon)
app.mount('#app')
