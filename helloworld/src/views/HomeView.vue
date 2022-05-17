<template>
<v-app>
<NavbarVue />
<DashboardVue />
<CategoryScrollVue />
<MainVue />
<FooterVue />
</v-app>
</template>

<script>
// @ is an alias to /src
import NavbarVue from '@/components/navigation/Navbar.vue'
import FooterVue from '@/components/navigation/Footer.vue'
import DashboardVue from '@/components/Dashboard/Dashboard.vue'
import MainVue from '@/components/Body/Main.vue'
import CategoryScrollVue from '@/components/Body/CategoryScroll.vue'

export default {
  name: 'HomeView',
  components: {
    NavbarVue,
    FooterVue,
    DashboardVue,
    MainVue,
    CategoryScrollVue
    
  }
}
</script>
