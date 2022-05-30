<template>
    <v-carousel cycle height="450" hide-delimiter-background show-arrows-on-hover>
        <template v-slot:prev="{ on, attrs }">
            <v-btn color="success" v-bind="attrs" v-on="on">
                <v-icon>mdi-chevron-left</v-icon>
            </v-btn>
        </template>
        <template v-slot:next="{ on, attrs }">
            <v-btn color="info" v-bind="attrs" v-on="on">
                <v-icon>mdi-chevron-right</v-icon>
            </v-btn>
        </template>
        <v-carousel-item v-for="(slide, i) in slides" :key="i" class="carousel-container">

            <div class="dashboard-content ">
                <h4> We Build Our Society</h4>
                <p> Lorem ipsum dolor sit amet consectetur adipisicing elit. itaque quae voluptas suscipit deserunt ipsa
                    dolore reiciendis </p>
                <p v-if="token == null">
                    <v-btn elevation="3" x-large color="red white--text " class="text--lg--h3">Signup</v-btn>

                </p>
                <p v-else>
                </p>

            </div>
            <v-img :src="images[i]" class="background-img"> </v-img>
        </v-carousel-item>
    </v-carousel>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Bona+Nova:wght@400;700&family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&display=swap');

@media all and (min-width:768px) {
    .carousel-container {
        position: relative;
        height: 450px;
        width: 100%;
    }

    .background-img {
        height: 100%;
        width: 100%;
        display: block;
        position: absolute;
    }

    .dashboard-content {
        position: absolute;
        background-color: rgba(0, 0, 0, 0.445);
        width: 100%;
        height: 100%;
        z-index: 900;
        padding: 5%;
        font-family: 'Libre Baskerville', serif;
    }

    /* Dashboard title  / subtitle section */
    .dashboard-content h4 {
        font-size: 38pt;
        font-weight: 600;
        color: #fff;


    }

    .dashboard-content p {
        font-size: 18pt;
        color: #fff;
        margin-top: 3%;
        padding: 0 3%;
    }

}

@media all and (max-width:768px) {

    .carousel-container {
        position: relative;
        height: 450px;
        width: 100%;
    }

    .background-img {
        height: 100%;
        width: 100%;
        display: block;
        position: absolute;
    }

    .dashboard-content {
        position: absolute;
        background-color: rgba(0, 0, 0, 0.445);
        width: 100%;
        height: 100%;
        z-index: 900;
        padding: 10% 4%;
        font-family: 'Libre Baskerville', serif;
    }

    /* Dashboard title  / subtitle section */
    .dashboard-content h4 {
        font-size: 24pt;
        font-weight: 600;
        color: #fff;


    }

    .dashboard-content p {
        font-size: 15pt;
        color: #fff;
        margin-top: 3%;
        padding: 0 3%;
        font-weight: 600;
    }
}

@media all and (max-width:600px) {
    .carousel-container {
        height: 400px;
    }

    .dashboard-content {
        padding: 20% 4%;

    }

    .dashboard-content h4 {
        font-size: 18pt;

    }

    .dashboard-content p {
        font-size: 14pt;

    }
}

@media all and (max-width: 400px) {
    .dashboard-content {}

    .dashboard-content h4 {}

    .dashboard-content p {
        font-size: 12pt;
    }
}
</style>
<script>
import one from './assets/one.jpg'
import two from './assets/two.jpg'
import three from './assets/three.jpg'
import four from './assets/four.jpg'
import { mapState } from 'vuex'

export default {
    name: "DashboardVue",
    data: () => {
        return {
            images: [
                one,
                two,
                three,
                four

            ],
            slides: [
                'First',
                'Second',
                'Third',
                'Fourth'

            ],
        }

    },
    computed: mapState([
        'user', 'token', 'username'
    ])



    // activeUser() {
    //     return this.$store.getters.activeUser
    // },



}
</script>