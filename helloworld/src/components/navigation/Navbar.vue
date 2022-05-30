<template>
  <v-container fluid class="red pa-0">
    <v-app-bar elevation="3" elevate-on-scroll fade-img-on-scroll color="black" class="header-content p-0 m-0">
      <v-toolbar-title class="title-block">
        <v-avatar rounded size="35" class="mr-5">
          <v-img src="./assets/logo3.png"></v-img>
        </v-avatar>Blogpedia
      </v-toolbar-title>
      <v-spacer class="spacer-element"></v-spacer>
      <v-toolbar-items class="hidden-sm-and-down">
        <v-btn plain rounded elevation="0" v-for="item in menu" :key="item.icon" class="nav-elements white--text">
          <router-link class="links" :to="item.icon" :class="{ 'red--text': item.active == 'true' }">{{ item.title }}
          </router-link>
        </v-btn>
      </v-toolbar-items>
      <v-form class="form-styling hidden-sm-and-down">
        <v-text-field  class="search-form" solo append-icon="mdi-magnify">
          <template v-slot:label>

          </template>
        </v-text-field>
      </v-form>
      <v-app-bar-nav-icon elevation="2 " class="ml-md-2 mb-3" color="white" @click="drawer = true"></v-app-bar-nav-icon>
    </v-app-bar>

    <v-navigation-drawer v-model="drawer" absolute temporary class="side-block">
      <v-avatar rounded size="40" class="mt-2">
        <v-img src="./assets/logo3.png"></v-img>

      </v-avatar>

      <h4> Blogpedia </h4>
      <v-form class="form-box">
        <v-text-field label="Search" outlined dense rounded clearable class=""></v-text-field>

      </v-form>

      <v-list shaped>
        <v-list-item-group v-model="group" active-class="deep-purple--text ">
          <v-list-item v-for="(item) in minbar" :key="item.icon" class="side-bar" elevation="2">
            <v-list-item-icon class="">
              <v-icon class="side-text ">{{ item.icon }}</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title class="side-text"> 
              <router-link :to="{name: item.to}">  {{ item.title }}</router-link>
             
              </v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>

  </v-container>
</template>

<script>
import one from '../Dashboard/assets/three.jpg'
export default {
  name: 'NavbarVue',
  data: () => {
    return {
      one,
      menu: [
        { icon: '/', title: "Home", active: "true" , to: 'home'},
        { icon: '/post', title: "Manage", active: "false"  },
        { icon: '/settings', title: "Setting", active: "false" },


      ],
      drawer: false,
      group: null,
      minbar: [
        { icon: 'mdi-home', title: "Home", to:"home"},
        { icon: 'mdi-briefcase-outline', title: "Manage", to:"manage" },
        { icon: 'mdi-account-cog-outline', title: "Setting", to: "setting" },

      ]
    }

  },
  methods: {
    changeColor: () => {
      console.log('Hello world')
    }
  }

}
</script>

<style  scoped>
@media all and (min-width: 768px) {
  /* styling navbar component title and logo*/


  /* Header content*/
  .header-content {
    width: 100% !important;
    padding: 0 !important;
    margin: 0 !important;
  }

  .title-block {
    color: #fff;
    font-family: "Gill Sans", "Gill Sans MT", Calibri, "Trebuchet MS",
      sans-serif;
    font-weight: 600;
    font-size: 24pt;
  }

  .nav-elements {
    font-weight: 600;
    font-size: 12pt;
    margin: 0 6pt;
    padding: 3pt;
  }

  .nav-elements .links {
    text-decoration: none;
    color: #fff !important;
  }

  .side-text {
    font-size: 12pt !important;
    font-weight: 600 !important;
    color: blue !important;


  }

  .side-bar {
    margin: 3pt 0 !important;
    background-color: rgba(100, 92, 92, 0.1);
  }

  .form-box {
    padding: 4pt;
  }

  .search-button {
    display: inline !important;

  }

  .form-styling {
    margin-top: 12pt;
    padding-top: 12pt !important;
  }

  .search-form {
    border-radius: 24pt !important;

  }

  /* Sideblock Nagivation*/

  .side-block h4 {
    font-weight: 700;
    color: #000;
    font-size: 24pt;
    font-family: "Gill Sans", "Gill Sans MT", Calibri, "Trebuchet MS",



  }
}

@media all and (max-width:768px) {
  .side-block h4 {
    font-weight: 700;
    color: #000;
    font-size: 24pt;
    font-family: "Gill Sans", "Gill Sans MT", Calibri, "Trebuchet MS",



  }

  .title-block {
    color: #fff;
    font-family: "Gill Sans", "Gill Sans MT", Calibri, "Trebuchet MS",
      sans-serif;
    font-weight: 600;
    font-size: 24pt;
  }

  .form-styling {
    margin-top: 12pt;
  }

  .search-form {
    border-radius: 17pt;
    width: 100%;
    height: 80% !important;

  }

  .side-text {
    font-size: 12pt !important;
    font-weight: 600 !important;
    color: blue !important;


  }

  .side-bar {
    margin: 3pt 0 !important;
    background-color: rgba(100, 92, 92, 0.1);
  }

  .form-box {
    padding: 4pt;
  }

}

@media all and (max-width:600px) {
  .title-block {
    font-size: 20pt;
  }

  .search-form {
    width: 75%;
  }

}

@media all and (max-width:500px) {
  .search-form {
    width: 50%;
  }
}
</style>