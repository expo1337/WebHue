<template>
  <div class="home" :style="{'margin-left': sidebarWidth}" data-bs-theme="dark">
    <div class="container-lg text-center pt-5">
      <div class="row">
        <div class="col-md-6 col-sm-12">
          <h5 class="text-white mb-3">Server Stats</h5>
          <cpu-chart/>
        </div>
        <div class="col-md-6 col-sm-12">
          <h5 class="text-white">Bluetooth Info</h5>
          <table class="table">
            <thead>
              <tr>
                <th scope="col">Device Name</th>
                <th scope="col">BLE Address</th>
              </tr>
            </thead>
            <!-- <tbody v-if="this.$store.state.nearbyDevices"> -->
            <tbody v-if="this.$store.state?.nearbyDevices">
              <tr v-for="device in this.$store.state.nearbyDevices[pageIndex-1]" :key="device.id">
                <td>{{device.name}}</td>
                <td>{{device.address}}</td>
              </tr>
            </tbody>
          </table>
          <div class="d-flex">
            <nav aria-label="..." class="d-flex">
              <ul class="pagination pagination-md page-list">
                <li v-for="(list, index) in this.$store.state.nearbyDevices" :key="index" :class="{ 'page-item': true, 'active': pageIndex === index+1 }"><a class="page-link" @click="changePageIndex(index+1)">{{index+1}}</a></li>
              </ul>
              <button class="mb-5 pl-2 btn btn-outline-primary" @click="refreshDevices">Refresh</button>
            </nav>
          </div>
        </div>
      </div>  
    </div>
    
    <Sidebar/>

  </div>
</template>

<script>
import Sidebar  from "@/components/sidebar/Sidebar.vue";
import {sidebarWidth} from "@/components/sidebar/state";
import CpuChart from '@/components/CpuChart.vue'

export default {
  name: 'HomeView',
  components: {
    Sidebar,
    CpuChart,
  },
  data() {
    return {
        sidebarWidth,
        chartInterval: null,
        pageIndex: 1
    }
  },

  beforeMount() {
    clearInterval(this.chartInterval)
    this.startInterval()
    this.refreshDevices()
  },
  mounted() {
    this.$store.dispatch('getNearbyDevices')
  },
  beforeUnmount() {
    clearInterval(this.chartInterval)
  },
  methods: {
    startInterval() {
      this.chartInterval = setInterval(() => {
                this.$store.dispatch('getServerStats')
              }, 1000);
    },
    refreshDevices() {
      this.$store.dispatch('getNearbyDevices')
    },
    changePageIndex(index) {
      this.pageIndex = index
    },
  }
}
</script>
<style>
.home {transition: 0.3s linear;}

.page-list {
  margin-right: 1rem;
}
</style>
