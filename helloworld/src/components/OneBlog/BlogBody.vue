<template>
    <v-container>
        <div class="parentHeader">
            <v-img class="coverImage"
                src="https://images.unsplash.com/photo-1573166584647-2c1366f9b219?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MzB8fHNvZnR3YXJlJTIwZW5naW5lZXJ8ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60">
            </v-img>
            <div class="blogTitle">
                <h3>How to Get Hired in the Artificial Intelligence Industry</h3>
            </div>
            <div class="miniDetails">
                <v-btn class="rounded red white--text"> Business</v-btn>
                <span>by John Doe </span>
                <span> 18th Nov 2021</span>
                <span> 5 comments</span>
            </div>
        </div>

        <v-row class="bodyBlock">
            <v-col class=" col-lg-8 col-md-12  col-sm-12 mainBlock">
                <p>Artificial Intelligence (AI) technology has been gaining popularity in recent years. From robots
                    serving food in restaurants to self-driving cars, these applications of artificial intelligence can
                    be seen in our day-to-day lives. John McCarthy, an American computer scientist who coined the term
                    artificial intelligence, defines this discipline as the science and engineering of making
                    intelligent machines, especially intelligent computer programs. Mainly, AI develops intelligent
                    software and systems based on how human minds think, learn, decide, and solve a problem. It enables
                    machines to perform human-like functions by learning through experience.

                    While professionals across the globe are worried about robots replacing humans, a Gartner study
                    reports that AI is an emerging field that will create 2.8 million jobs by 2020. AI is a broad term,
                    encompassing general artificial intelligence, machine learning, expert systems, data mining, and
                    more. In today’s world, AI capabilities are in high demand across industries—gaming, robotics, face
                    recognition software, weaponry, speech recognition, vision recognition, expert systems, and search
                    engines.

                    If you’re evaluating career options in this emerging field, look at these top five jobs in
                    artificial intelligence and the skills that you’ll need to transition into these roles.

                    Are you an AI and Machine Learning enthusiast? If yes, then Simplilearn's AI and Machine Learning
                    Course Certification is a perfect fit for your career growth</p>

                <div class="authCategories">
                    <v-btn rounded color="primary" class="ma-2"> sports</v-btn>
                    <v-btn rounded color="primary" class="ma-3"> science</v-btn>
                    <v-btn rounded color="primary" dark class="ma-3">gaming </v-btn>


                    <v-btn fab small dark color="orange" class="ml-5">
                        <font-awesome-icons :icon="['fab', 'twitter']"></font-awesome-icons>
                    </v-btn>
                    <v-btn fab small class="mx-3 white--text " color="purple">
                        <font-awesome-icons :icon="['fab', 'instagram']"></font-awesome-icons>
                    </v-btn>
                    <v-btn fab small class="mx-3 white--text " color="black">

                        <v-icon> mdi-share-variant-outline</v-icon>
                    </v-btn>
                </div>
                <v-divider class="ma-5"></v-divider>
                <h4 class="blue--text text-left">Author</h4>
                <v-row class="py-5">
                    <v-col class="col-md-4 col-lg-4 col-sm-12 ">
                        <v-avatar size="80">
                            <img src="https://images.unsplash.com/photo-1605379399642-870262d3d051?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NXx8c29mdHdhcmUlMjBlbmdpbmVlcnxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60"
                                alt="">
                        </v-avatar>
                    </v-col>
                    <v-col class="col-md-8 col-lg-8 col-sm-12 d-flex flex-column text-left">
                        <h5>John Doe</h5>
                        <p>
                            Lorem ipsum dolor sit amet consectetur adipisicing elit.
                        </p>
                        <a href="#"> View all posts</a>
                    </v-col>
                </v-row>

                <v-divider class="ma-5"></v-divider>
                <h1 class="sectionSubhead blue--text">Similar Articles</h1>

                <v-carousel cycle height="450" hide-delimiter-background show-arrows-on-hover>
                    <template v-slot:prev="{ on, attrs }">
                        <v-btn color="success" v-bind="attrs" v-on="on">Previous </v-btn>
                    </template>
                    <template v-slot:next="{ on, attrs }">
                        <v-btn color="info" v-bind="attrs" v-on="on">Next</v-btn>
                    </template>
                    <v-carousel-item v-for="(post, i) in posts" :key="i">
                        <v-sheet color="" class="" height="100%">

                            <v-img :src="post.image" max-height="350"></v-img>
                            <h4 class="articleTitle"> <a href="#" class="black--text"> {{ post.title }}</a></h4>
                            <p>
                                <span>
                                    <v-icon color="blue">mdi-circle-small</v-icon> By {{ post.author }}
                                </span> <span>
                                    <v-icon color="red">mdi-circle-small</v-icon> February 13 2022
                                </span>
                                <span>
                                    <v-icon color="blue">mdi-comment-text-multiple</v-icon> 12
                                </span>
                            </p>

                        </v-sheet>
                    </v-carousel-item>
                </v-carousel>


                <h1 class="sectionSubhead">Comments </h1>

                <v-divider></v-divider>
                <v-row class="pa-5">
                    <v-col class="col-md-4 col-lg-4 col-sm-4">
                        <v-avatar size="80">
                            <img src="https://images.unsplash.com/photo-1534665482403-a909d0d97c67?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Nnx8c29mdHdhcmUlMjBlbmdpbmVlcnxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60"
                                alt="">
                        </v-avatar>

                    </v-col>
                    <v-col class="col-md-8 col-sm-8 col-lg-8  commentsColumn">
                        <span>
                            By John Doe
                        </span> <span>
                             13th May 2020
                        </span>
                        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Veritatis nesciunt illo </p>

                        <v-divider></v-divider>
                        <h4 class="blue--text ma-3">REPLY </h4>
                        <v-row class="commentReply pa-4">
                            <v-col class="col-md-3 col-lg-3 ">
                                <v-avatar size="60">
                                    <img src="https://images.unsplash.com/photo-1481437642641-2f0ae875f836?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MzN8fHBlb3BsZXxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60"
                                        alt="">
                                </v-avatar>
                            </v-col>
                            <v-col class="col-md-9 col-lg-9  ">
                                <span>by Jane Doe</span> <span>8th March 2020</span>
                                <p>Lorem ipsum dolor sit, amet tems porro. Ipsum, fuga. </p>
                            </v-col>
                        </v-row>

                    </v-col>
                </v-row>
                <v-divider></v-divider>

            </v-col>
            <v-col class="col-lg-4  col-md-12 col-sm-12  sideBar">
                <v-card class="sideCard" tile>
                    <v-list dense>
                        <v-subheader class="blue--text side-heading">CATEGORIES</v-subheader>
                        <v-list-item-group v-model="selectedItem">
                            <v-list-item rounded class="listItems" v-for="(item, i) in category" :key="i">
                                <v-list-item-icon>
                                    <v-btn color="blue white--text" small fab flat>{{ item.categoryAmount }}</v-btn>
                                </v-list-item-icon>
                                <v-list-item-content>
                                    <v-list-item-title v-text="item.categoryName" class="categoryName blue--text">
                                    </v-list-item-title>
                                </v-list-item-content>
                            </v-list-item>
                        </v-list-item-group>
                    </v-list>
                </v-card>
                <v-card class="sideCard" tile>
                    <v-subheader class="blue--text side-heading">LATEST ARTICLES</v-subheader>
                    <v-row class v-for="(post, i) in posts" :key="i">
                        <v-col class="col-5" color="red">
                            <v-avatar tile size="100">
                                <v-img :src="post.image"></v-img>
                            </v-avatar>
                        </v-col>
                        <v-col class="col-7 text-left">
                            <v-btn tile x-small color="blue white--text " class>{{ post.category }}</v-btn>
                            <h6 class="articleTitles">{{ post.title }}</h6>

                            <span class="smallDate font-weight-light text-left">8th June 2009</span>
                        </v-col>
                    </v-row>
                </v-card>

                <v-card class="sideCard">
                    <v-subheader class="side-heading blue--text">POPULAR TAGS</v-subheader>
                    <v-row class="d-flex justify-space-around tagBlock">
                        <v-btn class="tags black white--text" v-for="(cat, i) in category" :key="i">{{ cat.categoryName
                        }}</v-btn>
                    </v-row>
                </v-card>
            </v-col>
        </v-row>


    </v-container>



</template>
<script>


export default {
    name: 'BlogBodyVue',
    data: () => {
        return {
            posts: [
                {
                    title: "Making Money Online",
                    category: "Hustle",
                    content: "lorem ipsium is a dummy text",
                    image: "https://images.unsplash.com/photo-1646725432541-689c5661f8f5?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8Y3J5cG9jdXJyZW5jeXxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60",
                    date: "18-11-2021",
                    author: "Lewis",
                    comments: 10,
                    likes: 120

                },
                {
                    title: "Hiking places in Nairobi",
                    category: "lifestyle",
                    content: "lorem ipsium is a dummy text",
                    image: "https://images.unsplash.com/photo-1566371486490-560ded23b5e4?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NXx8dmFjYXRpb258ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60",
                    date: "21-02-2021",
                    author: "Jessica",
                    comments: 9,
                    likes: 290



                },
                {
                    title: "Becoming a Tech Entreprenuer",
                    category: "Business",
                    content: "lorem ipsium is a dummy text",
                    image: "https://images.unsplash.com/photo-1600880292203-757bb62b4baf?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Nnx8YnVzaW5lc3N8ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60",
                    date: "3-06-2021",
                    author: "Idah",
                    comments: 4,
                    likes: 800



                },
                {
                    title: "Becoming a Tech Entreprenuer",
                    category: "Business",
                    content: "lorem ipsium is a dummy text",
                    image: "https://images.unsplash.com/photo-1600880292203-757bb62b4baf?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Nnx8YnVzaW5lc3N8ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60",
                    date: "3-06-2021",
                    author: "Max",
                    comments: 4,
                    likes: 800



                }


            ],
            category: [
                {
                    id: 1,
                    categoryName: "Sports",
                    categoryAmount: 80
                },
                {
                    id: 2,
                    categoryName: "Lifestyle",
                    categoryAmount: 40
                },
                {
                    id: 3,
                    categoryName: "Entertainment",
                    categoryAmount: 23
                },
                {
                    id: 4,
                    categoryName: "Business",
                    categoryAmount: 15
                },
                {
                    id: 5,
                    categoryName: "Health",
                    categoryAmount: 29
                }
            ],
            newarticles: [

            ],





        }


    },
}
</script>
<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Bona+Nova:wght@400;700&family=Fredoka:wght@400;500&family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&family=Playfair+Display:wght@500&display=swap');

@media all and (min-width: 768px) {
    .parentHeader {
        display: flex;
        flex-direction: column;
        justify-content: center;
        padding: 15pt 0;

    }

    .parentHeader .coverImage {
        width: 90%;
        height: 450px;
        display: block;
        margin: auto;
    }

    .parentHeader h3 {
        font-weight: 600;
        font-size: 28pt;
        color: #000;
        margin: 10pt;

    }

    .parentHeader .miniDetails {}

    .parentHeader span {
        margin: 10pt;
        font-size: 12pt;
        font-weight: 400;
        color: #696969;
    }

    .bodyBlock {
        margin: 15pt 0;

    }

    .bodyBlock .mainBlock {}

    .bodyBlock .mainBlock p {
        text-align: left;
    }

    .bodyBlock .sectionSubhead {
        font-size: 24pt;
        text-align: left;
        margin: 20pt 0;
        color: #000;
    }

    .bodyBlock .articleTitle {
        text-align: left;
        font-size: 20pt;
        font-weight: 600;
        margin: 5pt 10pt;

    }

    .bodyBlock span {
        font-weight: 600;
        font-size: 12pt;
        /* color:#838282; */
        color: #838282;
        margin: 5pt 10pt;
    }

    .bodyBlock .commentsColumn {
        text-align: left;
    }

    .bodyBlock .commentsColumn p {
        margin-top: 10pt;
        color: #000;
    }

    .bodyBlock .mainBlock .authCategories {
        text-align: left;
    }

    .bodyBlock .sideBar {}

    /* CSS for the Sidebar */
    .side-block {
        padding: 10pt 8pt;
    }

    .sideCard {
        margin: 30pt 4pt !important;
        font-family: "Bona Nova", serif;
    }

    .side-heading {
        font-size: 14pt;
        font-weight: 600;
        margin-bottom: 12pt;
    }

    .listItems {
        height: 40pt;

        border-top: 1px solid rgba(0, 0, 0, 0.11);
    }

    .categoryName {
        font-size: 13pt !important;
        text-align: right;
        font-weight: 600;
        font-weight: 550;
    }

    .articleTitles {
        font-size: 12pt;
        font-weight: 550;
        letter-spacing: 0.01px;
        text-align: left;
    }

    .smallDate {
        font-size: 9pt;
    }

    .tagBlock {
        padding: 12pt;
    }

    .tagBlock .tags {
        margin: 4pt;
    }
}



@media all and (max-width:768px) {
    .parentHeader {
        display: flex;
        flex-direction: column;
        justify-content: center;
        padding: 10pt 0;

    }

    .parentHeader .coverImage {
        width: 95%;
        height: 300px;
        display: block;
        margin: auto;
    }

    .parentHeader h3 {
        font-weight: 600;
        font-size: 16pt;
        color: #000;
        margin: 10pt;

    }

    .parentHeader .miniDetails {}

    .parentHeader span {
        margin: 10pt;
        font-size: 11pt;
        font-weight: 400;
        color: #696969;
    }

    .bodyBlock {
        margin: 10pt 0;

    }

    .bodyBlock .mainBlock {}

    .bodyBlock .mainBlock p {
        text-align: left;
    }

    .bodyBlock .sectionSubhead {
        font-size: 18pt;
        text-align: left;
        margin: 10pt 0;
        color: #000;
    }

    .bodyBlock .articleTitle {
        text-align: left;
        font-size: 14pt;
        font-weight: 600;
        margin: 5pt 10pt;
        color:#000 !important;

    }
    .bodyBlock .articleTitle a{
    color:#000;
    text-decoration:none;
    }

    .bodyBlock span {
        font-weight: 400;
        font-size: 12pt;
        /* color:#838282; */
        color: #838282;
        margin: 5pt 10pt;
    }

    .bodyBlock .commentsColumn {
        text-align: left;
    }

    .bodyBlock .commentsColumn p {
        margin-top: 10pt;
      
        
         }

    .bodyBlock .mainBlock .authCategories {
        text-align: left;
    }

}
</style>