<template>
<section class="vh-100 bg-body-tertiary" data-bs-theme="dark">
  <div class="container py-5 h-100">
    <div class="row d-flex justify-content-center align-items-center h-100">
      <div class="col col-xl-10">
        <div class="card" style="border-radius: 1rem;">
          <div class="row g-0">
            <div class="col-md-6 col-lg-5 d-none d-md-block login-banner">
                <img src="../assets/login.png"
                alt="login form" class="img-fluid" style="border-radius: 1rem 0 0 1rem;" />
            </div>
            <div class="col-md-6 col-lg-7 d-flex align-items-center">
              <div class="card-body p-4 p-lg-5 text-white">
                <form>
                  <div class=" align-items-center mb-3 pb-1 mt-4">
                    <span class="h1 fw-bold mb-4">⚡️WebHue</span>
                  </div>
                  <div class="align-items-center mb-3 mt-1">
                    <span class="fw-bold mb-4">Log in</span>
                  </div>
                  <div class="form-group mt-6 mb-4 col-8 justify-content-center align-items-center mx-auto">
                    <input type="email" class="form-control" id="exampleInputEmail1" placeholder="Username" v-model="username"/>
                  </div>
                  <div class="form-group mb-4 col-8 justify-content-center align-items-center mx-auto">
                    <input type="password" class="form-control" id="exampleInputPassword1" placeholder="Password" v-model="password">
                  </div>
                  <div class="pt-1 mb-4">
                    <button class="btn btn-outline-danger" type="button" @click="login()">Login</button>
                  </div>

                  <p class="mb-5 pb-lg-2 text-white text-light">Don't have an account? 
                    <a href="/register" class="text-white font-weight-bold">Register here</a>
                  </p>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
</template>

<script>
import 'vue3-toastify/dist/index.css'
//import util from '@/util';

export default {
  name: 'Login',
  data() {
    return {
      username: '',
      password: '',
      rememberMe: true,
    }
  },
  mounted() {
    // if (VueCookie.get('refresh_token') || this.$store.state.accessToken !== null) {
    //   if(this.$store.state.accessToken === null) {
    //     this.$store.dispatch("refreshAuthToken")
    //   }
    //   this.$router.push('/')
    // }
  },
  methods: {
    login () {
      this.$store.dispatch('login', {
        username: this.username,
        password: this.password,
        remember: this.rememberMe
      })
          .then(() => {
            this.$router.push({name: 'home'})
          })
    },
  },
}
</script>
<style >
.login-banner {
  background: linear-gradient(74deg, #00c5ff, #e700ff, #00a3ff, #d000ff);
  background-size: 800% 800%;
  border-radius: 4% 0% 0% 4%;
  -webkit-animation: AnimationName 30s ease infinite;
  -moz-animation: AnimationName 30s ease infinite;
  animation: AnimationName 30s ease infinite;
}

@-webkit-keyframes AnimationName {
  0%{background-position:0% 35%}
  50%{background-position:100% 66%}
  100%{background-position:0% 35%}
}
@-moz-keyframes AnimationName {
  0%{background-position:0% 35%}
  50%{background-position:100% 66%}
  100%{background-position:0% 35%}
}
@keyframes AnimationName {
  0%{background-position:0% 35%}
  50%{background-position:100% 66%}
  100%{background-position:0% 35%}
}
</style>

