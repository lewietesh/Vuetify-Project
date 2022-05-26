<template>
  <v-app id="inspire">
    <v-main>
      <v-container class="fill-height" fluid>
        <v-row align="center" justify="center">
          <v-col cols="12" sm="8" md="8">
            <v-card class="elevation-12">
              <v-window v-model="step">
                <v-window-item :value="1">
                  <v-row>
                    <v-col cols="12" md="8" class="mb-4">
                      <v-card-text class="mt-5">
                        <h3 class="text-center large-headings teal--text text--accent-3">Sign in to Blogpedia</h3>
                        <div class="text-center mt-4">
                          <v-btn class="mx-2" fab color="blue" outlined small>
                            <font-awesome-icons :icon="['fab', 'facebook']"></font-awesome-icons>
                          </v-btn>

                          <v-btn class="mx-2" fab color="orange" outlined small>
                            <font-awesome-icons :icon="['fab', 'google']"></font-awesome-icons>
                          </v-btn>
                          <v-btn class="mx-2" fab color="red" outlined small>
                            <font-awesome-icons :icon="['fab', 'twitter']"></font-awesome-icons>
                          </v-btn>
                        </div>
                        <h4 class="text-center mt-4">Use your registered email</h4>
                        <form>
                          <v-text-field label="Email" name="Email" prepend-icon="email" type="text"
                            color="teal accent-3" />

                          <v-text-field id="password" label="Password" name="password" prepend-icon="lock"
                            type="password" color="teal accent-3" />
                        </form>
                        <h3 class="text-center mt-4">Forgot your password ?</h3>
                      </v-card-text>
                      <div class="text-center mt-3">
                        <v-btn rounded color="teal accent-3" dark>SIGN IN</v-btn>
                      </div>
                    </v-col>
                    <v-col cols="12" md="4" class="teal accent-3 mt-">
                      <v-card-text class="white--text mt-12">
                        <h3 class="text-center large-headings">New Account</h3>
                        <h5 class="text-center">Enter your personal details to log in</h5>
                      </v-card-text>
                      <div class="text-center">
                        <v-btn rounded outlined dark @click="step++">SIGN UP</v-btn>
                      </div>
                      <v-img class="center my-3"
                        lazy-src="https://images.unsplash.com/photo-1523825036634-aab3cce05919?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MjB8fGhhcHB5YWZyaWNhbiUyMGFtZXJpY2Fuc3xlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60"
                        max-height="150" max-width="250"
                        src="https://images.unsplash.com/photo-1523825036634-aab3cce05919?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MjB8fGhhcHB5YWZyaWNhbiUyMGFtZXJpY2Fuc3xlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60">
                      </v-img>
                    </v-col>
                  </v-row>
                </v-window-item>
                <v-window-item :value="2">
                  <v-row class="fill-height">
                    <v-col cols="12" md="4" class="teal accent-3">
                      <v-card-text class="white--text mt-12">
                        <h3 class="text-center large-headings">Welcome Back!</h3>
                        <h5 class="text-center">To Keep connected with us please login with your personnel info</h5>
                      </v-card-text>
                      <div class="text-center">
                        <v-btn rounded outlined dark @click="step--">Sign in</v-btn>
                      </div>
                    </v-col>

                    <v-col cols="12" md="8" class="mb-4">
                      <v-card-text class="mt-12">
                        <h3 class="text-center large-headings teal--text text--accent-3">Create Account</h3>
                        <div class="text-center mt-4">
                          <v-btn class="mx-2" fab color="blue" outlined>
                            <font-awesome-icons :icon="['fab', 'facebook']"></font-awesome-icons>
                          </v-btn>

                          <v-btn class="mx-2" fab color="orange" outlined>
                            <font-awesome-icons :icon="['fab', 'google']"></font-awesome-icons>
                          </v-btn>
                          <v-btn class="mx-2" fab color="red" outlined>
                            <font-awesome-icons :icon="['fab', 'twitter']"></font-awesome-icons>
                          </v-btn>
                        </div>
                        <h4 class="text-center mt-4">Ensure your email for registration</h4>
                        <ValidationObserver v-slot="{ invalid }">
                          <form @submit.prevent="onSubmit">


                            <ValidationProvider name="Username" rules="required" v-slot="{ errors }">
                              <v-text-field label="username" name="username" prepend-icon="person" type="text"
                                v-model.trim="username" color="teal accent-3" />
                              <span>{{ errors[0] }}</span>
                            </ValidationProvider>


                            <ValidationProvider name="E-mail" rules="required|email" v-slot="{ errors }">
                              <v-text-field label="Email" name="email" prepend-icon="email" type="email" v-model="email"
                                color="teal accent-3" />
                              <span>{{ errors[0] }}</span>
                            </ValidationProvider>

                            <ValidationProvider name="password" rules="required|min:8" v-slot="{ errors }" ref="password">

                              <v-text-field id="password" label="Password" v-model="password" 
                                name="password" prepend-icon="lock" type="password" color="teal accent-3" />
                              <span>{{ errors[0] }}</span>
                            </ValidationProvider>

                            <validationProvider name="Confirm Password" rules="required|confirmed:password"
                              v-slot="{ errors }">
                              <v-text-field id="confirmpassword" label="Confirm Password" v-model="confpassword"
                                name="confirmpassword" prepend-icon="lock" data-vv-as="password" type="password" color="teal accent-3" />

                              <span>{{ errors[0] }}</span>
                            </validationProvider>

                            <div class="text-center mt-5">
                              <v-btn rounded color="teal accent-3" type="submit" :disabled="invalid" dark>SIGN UP
                              </v-btn>
                            </div>

                          </form>
                        </ValidationObserver>
                      </v-card-text>

                    </v-col>
                  </v-row>
                </v-window-item>
              </v-window>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  data: () => ({
    step: 1,
    username: '',
    email: '',
    password: '',
    confirmPassword: '',
    errors: []
  }),
  props: {
    source: String
  },
  methods: {

    onSubmit() {
      alert("Your form was successfully submitted")
    }
  }


};
</script>
<style scoped>
.large-headings {
  font-size: 22pt;
  font-weight: 800;
}
span{
  color:red;
}
</style>