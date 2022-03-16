<template>
    <v-container-fluid class="contentBody">
        <v-row>
            <v-col class="col-lg-9 col-sm-12 col-md-12 blog-block">
                <v-card class="blog-cards" tile v-for="post in posts" :key="post.author">
                    <v-img height="250" :src="post.image"></v-img>
                    <v-card-title class="post-title">{{ post.title }}</v-card-title>
                    <div class="date-author-block">
                        <span class="author">John Doe</span>
                        <span class="date">18 Nov 2022</span>
                    </div>
                    <div
                        class="blog-body"
                    >Sarah watched the whirlpool mesmerized. She couldn't take her eyes off the water swirling around and around. She stuck in small twigs and leaves to watch the whirlpool catch them and then suck them down. It bothered her more than a little bit that this could also be used as a metaphor for her life</div>
                    <div class="card-footer">
                        <v-btn icon color="blue " class="mr-5">
                            <v-icon>mdi-share-variant</v-icon>
                        </v-btn>
                        <v-btn color="red darken-1" fab class="ml-5" small>
                            <v-icon color="white">mdi-heart</v-icon>
                        </v-btn>
                        <span>10</span>
                        <v-btn class="ml-5 blue--text">
                            <v-icon fab small class="blue--text">mdi-message</v-icon>
                        </v-btn>
                        <span class="mr-5">12</span>
                    </div>
                </v-card>
            </v-col>
            <v-col class="col-lg-3 hidden-sm-and-down side-block">
                <v-form>
                    <v-text-field
                        label="Search"
                        placeholder
                        filled
                        rounded
                        dense
                        elevation="3"
                        append-icon="mdi-magnify"
                    ></v-text-field>
                </v-form>
                <v-card class="sideCard" tile>
                    <v-list dense>
                        <v-subheader class="blue--text side-heading">CATEGORIES</v-subheader>
                        <v-list-item-group v-model="selectedItem">
                            <v-list-item
                                rounded
                                class="listItems"
                                v-for="(item, i) in category"
                                :key="i"
                            >
                                <v-list-item-icon>
                                    <v-btn
                                        color="blue white--text"
                                        small
                                        fab
                                        flat
                                    >{{ item.categoryAmount }}</v-btn>
                                </v-list-item-icon>
                                <v-list-item-content>
                                    <v-list-item-title
                                        v-text="item.categoryName"
                                        class="categoryName blue--text"
                                    ></v-list-item-title>
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
                        <v-btn
                            class="tags black white--text"
                            v-for="(cat, i) in category"
                            :key="i"
                        >{{ cat.categoryName }}</v-btn>
                    </v-row>
                </v-card>

                <v-card>
                    <v-subheader
                        class="side-heading blue--text d-flex justify-space-between"
                    >Instagram</v-subheader>
                    <v-avatar size="80" class="mx-2 my-2" color="blue" tile>
                        <v-img
                            src="https://images.unsplash.com/photo-1600880292203-757bb62b4baf?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Nnx8YnVzaW5lc3N8ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60"
                        ></v-img>
                    </v-avatar>
                    <v-avatar size="80" class="mx-2 my-2" color="blue" tile>
                        <v-img
                            src="https://images.unsplash.com/photo-1489710437720-ebb67ec84dd2?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8N3x8aGFwcHl8ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60"
                        ></v-img>
                    </v-avatar>
                    <v-avatar size="80" class="mx-2 my-2" color="blue" tile>
                        <v-img
                            src="https://images.unsplash.com/photo-1477959858617-67f85cf4f1df?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTR8fGJ1c2luZXNzfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60"
                        ></v-img>
                    </v-avatar>
                    <v-avatar size="80" class="mx-2 my-2" color="blue" tile>
                        <v-img
                            src="https://images.unsplash.com/photo-1493770348161-369560ae357d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTJ8fGZvb2R8ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60"
                        ></v-img>
                    </v-avatar>
                    <v-avatar size="80" class="mx-2 my-2" color="blue" tile>
                        <v-img
                            src="https://images.unsplash.com/photo-1522204523234-8729aa6e3d5f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTV8fG9ubGluZXxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60"
                        ></v-img>
                    </v-avatar>
                    <v-avatar size="80" class="mx-2 my-2" color="blue" tile>
                        <v-img
                            src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8ZGF0YSUyMGFuYWx5c2lzfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60"
                        ></v-img>
                    </v-avatar>
                </v-card>
            </v-col>
        </v-row>
    </v-container-fluid>
</template>

<script>
export default {
    name: "MainVue",
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
                    author: "Faith",
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

            ]




        }


    }

}
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Bona+Nova:wght@400;700&family=Fredoka:wght@400;500&family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&display=swap");
.contentBody {
    font-family: "Libre Baskerville", serif;
}
@media all and (min-width: 768px) {
    .blog-block {
    }
    .blog-cards {
        display: inline-block;
        width: 360px;
        margin: 12pt 8pt;
    }
    .blog-body {
        text-align: left;
        padding: 10pt;
        font-family: "Fredoka", sans-serif;
        font-weight: 400;
        font-size: 12pt;
    }
    .card-footer {
    }
    .date-author-block {
        text-align: left;
        padding: 0 10pt;
    }
    .post-title {
        font-weight: 700;
        font-size: 14pt;
        padding: 4pt !important;
    }
    .date-author-block {
        font-size: 11pt;
        font-weight: 600;
        color: rgba(0, 0, 0, 0.479);
    }
    .date-author-block .date {
        margin-left: 12pt;
    }
    hr {
        color: rgba(0, 0, 0, 1);
    }

    .card-footer {
        padding: 8pt 4pt;
        text-align: left;
    }
    .card-footer span {
        margin: 0 2pt;
        color: rgba(0, 0, 0, 0.877);
        font-weight: 500;
    }
    /* CSS for the Sidebar */
    .side-block {
        padding: 20pt 8pt;
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
</style>