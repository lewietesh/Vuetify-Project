<template>
    <div>
        <v-app-bar elevation="4" dense color="green accent-3">
            <v-toolbar-title class="title-block">
                <v-avatar rounded size="30">
                    <font-awesome-icons :icon="['fab', 'drupal']" class="logo" />
                </v-avatar>Blogpedia
            </v-toolbar-title>
            <v-spacer></v-spacer>
            <v-toolbar-items class="hidden-sm-and-down">
                <v-btn plain small
                v-for="item in menu" 
                :key="item.icon"
                class="nav-elements"
                 :class="{'red--text': item.active == 'true'}"
                
                >{{item.title}}</v-btn>
            </v-toolbar-items>
            <v-spacer></v-spacer>
            <v-app-bar-nav-icon color="white" @click="drawer = true"></v-app-bar-nav-icon>
        </v-app-bar>
          <v-card
    class="mx-auto overflow-hidden"
    height="100vh"
  >


    <v-navigation-drawer
      v-model="drawer"
      absolute
      temporary
    >
      <v-list
        nav
        dense
      >
        <v-list-item-group
          v-model="group"
          active-class="deep-purple--text text--accent-4"
        >
          <v-list-item>
            <v-list-item-icon>
              <v-icon>mdi-account-cog-outline</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Home</v-list-item-title>
          </v-list-item>


        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
  </v-card>
    </div>
</template>

<script>
export default {
    name: 'NavbarVue',
    data: () => {
        return {
            menu: [
                { icon: 'home', title: "Home", active: "true" },
                { icon: 'posts', title: "Posts", active: "false"},
                { icon: 'settings', title: "Settings", active: "false"},
                { icon: 'help', title: "Help", active: "false" },

            ],
            drawer:false,
            group:null,
            minbar: [
                {icon: 'mdi-home', title:"Home"},
                {icon: 'mdi-brief-case-outline', title:"Posts"},
                {icon: 'mdi-account-cog-outline', title:"Setting"},
                {icon: 'mdi-help-circle-outline', title:"Help"}
            ]
        }

    },
    methods:{
        changeColor : () =>{
            console.log('Hello world')
        }
    }

}
</script>

<style  scoped>
@media all and (min-width: 768px) {
    /* styling navbar component title and logo*/

    .title-block {
        color: #fff;
        font-weight: 800;
        font-size: 18pt;
    }
    .nav-elements{
    color:#fff;
    font-weight: 600;
    font-size: 12pt;
    }
}
</style>