<template>
<section class="vh-100 bg-body-tertiary" data-bs-theme="dark">
  <div class="container py-5 h-100">
    <div class="row d-flex justify-content-center align-items-center h-100">
      <div class="col col-xl-10">
        <div class="card" style="border-radius: 1rem;">
          <div class="row g-0">
            <div class="col-md-6 col-lg-5 d-none d-md-block">
                <img src="../assets/register.png"
                alt="login form" class="img-fluid" style="border-radius: 1rem 0 0 1rem;" />
            </div>
            <div class="col-md-6 col-lg-7 d-flex align-items-center">
              <div class="card-body p-4 p-lg-5 text-white">
                <form>
                  <div class=" align-items-center mb-3 pb-1">
                    <span class="h1 fw-bold mb-4">⚡️Dashboard</span>
                  </div>
                  <div class="align-items-center mb-3 mt-1">
                    <span class="fw-bold mb-4">Create an account</span>
                  </div>
                  <div class="form-group mt-6 mb-4 col-8 justify-content-center align-items-center mx-auto">
                    <input type="username" class="form-control" id="exampleInputUsername1" placeholder="Username" v-model="username">
                  </div>
                  <div class="form-group mb-4 col-8 justify-content-center align-items-center mx-auto">
                    <input type="password" class="form-control" id="exampleInputPassword1" placeholder="Password" v-model="password">
                  </div>
                  <div class="form-group mb-4 col-8 justify-content-center align-items-center mx-auto">
                    <input type="password" class="form-control" id="exampleInputPassword2" placeholder="Confirm Password" v-model="confirm_password">
                  </div>

                  <div class="pt-1 mb-4">
                    <button type="button" @click="beforeRegister()" class="btn btn-outline-info">Register</button>
                  </div>

                  <p class="mb-5 pb-lg-2 text-white">Already have an account? 
                    <a href="/login" class="text-white text-bold">Login here</a>
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
import { toast} from 'vue3-toastify'
import 'vue3-toastify/dist/index.css'

export default {
    name: 'RegisterView',
    data() {
      return {
        username: '',
        password: '',
        confirm_password: '',
      }
    },
    methods: {
      register () {
        this.$store.dispatch('register', {
          username: this.username,
          password: this.password
        })
            .then(() => {
              this.$router.push({name: 'home'})
            })
            .catch(err => {
              console.log(err)
            })
      },
      beforeRegister () {
        if (this.password === this.confirm_password) {
          this.register()
        }
        else {
          this.username = ''
          this.password = ''
          toast.error("Passwords don't match!", {
            autoClose: 1500,
            position: toast.POSITION.BOTTOM_RIGHT,
            transition: toast.TRANSITIONS.SLIDE,
            theme: 'dark'
          });
        }
      }
    },

}

  

</script>

