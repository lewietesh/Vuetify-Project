<template>
    <v-carousel cycle height="450" hide-delimiter-background show-arrows-on-hover>
        <template v-slot:prev="{ on, attrs }">
            <v-btn color="success" v-bind="attrs" v-on="on">Previous slide</v-btn>
        </template>
        <template v-slot:next="{ on, attrs }">
            <v-btn color="info" v-bind="attrs" v-on="on">Next slide</v-btn>
        </template>
        <v-carousel-item v-for="(slide, i) in slides" :key="i" class="carousel-container">

        <div  class="dashboard-content "> </div>
        <v-img :src="images[i]"  class="background-img">  </v-img>
        </v-carousel-item>
    </v-carousel>
</template>

<style scoped>
@media all and (min-width:768px){
.carousel-container{
position: relative;
height:450px;
width: 100%;
}

.background-img{
height: 100%;
width: 100%;
display: block;
position: absolute;
}

.dashboard-content{
    position: absolute;
    background-color:rgba(0, 0, 0, 0.445);
    width: 100%;
    height:100%;
    z-index:900;
}

}
</style>
<script>
import one from './assets/one.jpg'
import two from './assets/two.jpg'
import three from './assets/three.jpg'
import four from './assets/four.jpg'

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

    }
}
</script>