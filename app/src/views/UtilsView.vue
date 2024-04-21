<template>
  <div class="home" :style="{'margin-left': sidebarWidth}" data-bs-theme="dark">
    <div class="container pt-5">
      <div class="row">
        <div class="col-lg-6">
          <h3 class="text-white col-lg-12 text-center">Find Service UUIDS</h3>
          <div class="row gap justify-content-between">
            <div class="form-group row mb-4">
              <label for="staticEmail" class="col-sm-12 col-form-label text-white">Device Address</label>
              <div class="col-sm-12 col-md-8 mx-auto mt-2">
                <input type="text" class="form-control" placeholder="FF:FF:FF:FF:FF:FF" v-model="service_address">
              </div>
              <button class="btn btn-primary col-lg-4 col-md-8 col-sm-8 mt-2" @click="findServices()">Find Services</button>
            </div>
          </div>
          <div class="table-responsive">
            <table class="table col-sm-12">
              <thead>
                <tr>
                  <th scope="col">Service</th>
                </tr>
              </thead>
              <tbody v-if="this.$store.state?.deviceServices">
                <tr v-for="service in this.$store.state.deviceServices.chars" :key="service" >
                  <td>{{service}}</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
        <div class="col-lg-6">
        <h3 class="text-white col-lg-12 mb-5 text-center">Custom BLE Command</h3>
        <form>
          <div class="form-group row mb-4">
              <label for="staticEmail" class="col-sm-12 col-form-label text-white">Device Address</label>
              <div class="col-sm-4 col-md-8 mx-auto">
              <input type="text" class="form-control" placeholder="FF:FF:FF:FF:FF:FF" v-model="address">
              </div>
          </div>
          <div class="form-group row mb-4">
              <label for="staticEmail" class="col-sm-12 col-form-label text-white">Service UUID</label>
              <div class="col-sm-4 col-md-8 mx-auto">
              <input type="text" class="form-control" placeholder="7e0004000000ff00ef" v-model="uuid">
              </div>
          </div>
          <div class="form-group row mb-4">
              <label for="staticEmail" class="col-sm-12 col-form-label text-white">Command</label>
              <div class="col-sm-4 col-md-8 mx-auto">
              <input type="text" class="form-control" placeholder="7e0004000000ff00ef" v-model="command">
              </div>
          </div>
          <div class="form-group row mb-4">
              <div class="col-sm-4 col-md-8 mx-auto">
                <div class="d-flex flex-wrap justify-content-center gap-4">
                  <div class="btn btn-outline-primary px-5" @click="sendCommand()">Send Command</div>
                </div>
              </div>
          </div>
      </form>
      </div>
      </div>
    </div>
    <Sidebar/>
  </div>
</template>

<script>
import Sidebar from '@/components/sidebar/Sidebar.vue'
import VueCookie from "vue-cookie";
import {sidebarWidth} from "@/components/sidebar/state";
import util from '@/util';

export default {
  name: 'HomeView',
  components: {
    Sidebar,
  },
  setup() {return {sidebarWidth}},
  data() {
    return {
      pageIndex: 1,
      address: '',
      uuid: '',
      command: '' ,
      service_address: ""
    }
  },
  beforeMount() {
    if (!VueCookie.get('refresh_token') && this.$store.state.accessToken === null) {
      this.$router.push('login')
    }
    else {
      if(this.$store.state.accessToken === null) {
        this.$store.dispatch("refreshAuthToken")
            .then(() => {
              this.$store.dispatch('getNearbyDevices')
              .then(() => {
              //   this.$store.state.nearbyDevices.forEach(device => {
              //   console.log(device)
              // });
              console.log(this.$store.state.nearbyDevices)
              })
            })
      }
      else {
        this.$store.dispatch('getNearbyDevices')
        this.$store.state.nearbyDevices.forEach(device => {
                console.log(device)
              });
      }
    }
  },
  mounted() {
  },
  methods: {
    checkToken() {
      util.checkToken(this.$store.state.accessToken)
    },
    sendCommand () {
      this.$store.dispatch('sendCustomCommand', {
        address: this.address,
        uuid: this.uuid,
        command: this.command
      })
    },
    findServices() {
      this.$store.dispatch('getDeviceServices', {
        address: this.service_address
      })
    }
  },
}
</script>
<style>
.home {transition: 0.3s linear;}

body {
  background-color: #212529 !important;
  height: 100vh;
}
</style>
