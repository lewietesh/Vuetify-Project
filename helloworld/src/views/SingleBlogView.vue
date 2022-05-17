<template>
    <v-app>
        <NavbarVue />
        <BlogBodyVue />
        <FooterVue />
    </v-app>

</template>


<script>
import NavbarVue from "@/components/navigation/Navbar.vue"
import BlogBodyVue from '@/components/OneBlog/BlogBody.vue'
import FooterVue from "@/components/navigation/Footer.vue"
export default {
    name: "SingleBlogView",
    components: {
    NavbarVue,
    BlogBodyVue,
    FooterVue,
},
    data: () => {
        return {
            blog: [
                {
                title: "Making Money Online",
                category: "Hustle",
                content: "lorem ipsium is a dummy text",
                image: "https://images.unsplash.com/photo-1646725432541-689c5661f8f5?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8Y3J5cG9jdXJyZW5jeXxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60",
                date: "18-11-2021",
                author: "Lewis",
                comments:[
                    {
                        name: "Lewis",
                        date: "3rd Nov 2021",
                        message: "Comments can be something hilarious. I think the first step towards anything is the most important one",
                        reply: "Nice comment",
                        likes: 4,
                        profile: "https://images.unsplash.com/photo-1488161628813-04466f872be2?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8OXx8cGVvcGxlfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60" 

                    }
                ],
                commentCount: 10,
                likes: 120
                }
            ],
            similarPosts: [

            ],
            categories: [
                {
                    
                }
            ]
        }
    }

}
</script>

<style scoped>
</style>