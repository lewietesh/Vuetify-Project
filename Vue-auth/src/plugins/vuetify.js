// Vuetify
import { createVuetify } from 'vuetify'

// Styles
import 'material-design-icons-iconfont/dist/material-design-icons.css'
import 'vuetify/styles'
import { aliases, md} from 'vuetify/lib/iconsets/md';




export default createVuetify({
    icons: {
       defaultSet:'md',
       aliases,
       sets:{
           md,
       },
    },
})
