<template>
<v-app>
<NavbarVue />
<DashboardVue />
<FooterVue />
</v-app>
</template>

<script>
// @ is an alias to /src
import NavbarVue from '@/components/navigation/Navbar.vue'
import FooterVue from '@/components/navigation/Footer.vue'
import DashboardVue from '@/components/Dashboard/Dashboard.vue'

export default {
  name: 'HomeView',
  components: {
    NavbarVue,
    FooterVue,
    DashboardVue
    
  }
}
</script>
