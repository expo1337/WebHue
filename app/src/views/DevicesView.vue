<template>
  <div class="home vh-100 bg-body-tertiary home" :style="{'margin-left': sidebarWidth}" data-bs-theme="dark">
    <div class="container ml-5">
      <h2 class="mb-5 text-white">⚡️ Connected Device Controls</h2>
      <div class="row align-items-center">
        <div v-for="device in this.$store.state.userDevices" :key="device.uid" class="col-sm-12 col-md-6 col-lg-4 mb-5 align-content-center" align="center">
          <div class="card text-center" style="width: 18rem;" align="center">
            <img src='@/assets/ledstrip.png' class="card-img-top" alt="...">
            <h4 class="card-title mt-2 lead">⚡️{{device.name}}</h4>
            <hr>
            <p class="card-text">address: {{device.description}}</p>
            <div class="col-md-12 col-lg-12 justify-content-around">
               <div class="row">
                <div class="text-center col-md-6">
                  <div class="col-md-12 mb-4"> 
                      <a href="#" class="btn btn-outline-danger">Controls</a>
                  </div>
                </div>
                <div class="text-center col-md-6">
                    <div class="col-md-12 mb-4"> 
                      <a href="#" class="btn btn-info"></a>
                    </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
  </div>

    <Sidebar/>
  </div>
</template>

<script>
import Sidebar from '@/components/sidebar/Sidebar.vue'
import {sidebarWidth} from "@/components/sidebar/state";

export default {
  name: 'DevicesView',
  components: {
    Sidebar
  },
  setup() {return {sidebarWidth}},
  mounted() {
    this.$store.dispatch('getUserDevices')
  }
}
</script>
<style>
</style>
