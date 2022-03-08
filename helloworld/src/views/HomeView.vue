<template>
<v-app>
<NavbarVue />
<FooterVue />
</v-app>
</template>

<script>
// @ is an alias to /src
import NavbarVue from '@/components/navigation/Navbar.vue'
import FooterVue from '@/components/navigation/Footer.vue'

export default {
  name: 'HomeView',
  components: {
    NavbarVue,
    FooterVue,
    
  }
}
</script>
