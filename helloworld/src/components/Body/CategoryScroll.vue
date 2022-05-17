<template>
    <v-container class="scrollCategory hidden-lg-and-up"  >
        <v-btn class="buttons blue" rounded v-for="(cat, i) in categories" :key="i">{{ cat.name }}</v-btn>
    </v-container>
</template>

<script>
export default {
    name: "CategoryScrollVue",
    data: () => {
        return {
            categories: [
                {
                    id: 1,
                    name: 'health'

                },
                {
                    id: 2,
                    name: 'sports'
                },
                {
                    id: 3,
                    name: 'entertainment'
                },
                {
                    id: 4,
                    name: 'food'
                },
                {
                    id: 5,
                    name: 'health'
                },
                {
                    id: 6,
                    name: 'gaming'
                }
                ,
                {
                    id: 7,
                    name: 'music'
                }

            ]
        }
    }
}
</script>

<style scoped>

.scrollCategory {
    height: 60pt;
    padding: 10pt 20pt;
    width: 100%;
    overflow-x:scroll;
    white-space: nowrap;
}
.scrollCategory::-webkit-scrollbar{
width:0;
}
.buttons {
    background-color: blue;
    color: #fff;
    margin: 0 5pt;
}
</style>