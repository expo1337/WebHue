<template>
  <div class="home bg-body home" :style="{'margin-left': sidebarWidth}" data-bs-theme="dark">
    <div class="container ml-5 pt-5">
      <h2 v-if="this.$store.state.userDevices.length != 0" class="mb-5 text-white">⚡️ Connected Device Controls</h2>
      <h2 v-else class="mb-5 text-white">You haven't added any devices yet !</h2>
      <div class="row align-items-center">
        <div v-for="device in this.$store.state.userDevices" :key="device.uid" class="col-sm-12 col-md-6 col-lg-4 mb-5 align-content-center" align="center">
          <div class="card text-center w-100" align="center">
            <img src='@/assets/ledstrip.png' class="card-img-top" alt="...">
            <h4 class="card-title mt-3 lead">⚡️{{device.name}}</h4>
            <p class="card-text">{{device.description}}</p>
            <div class="col-md-12 col-lg-12 justify-content-around">
               <div class="row pb-3">
                <div class="text-center col-6">
                  <a class="btn btn-outline-danger" @click="this.$router.push(`/controls/${findDeviceIndex(device)+1}`)">Controls</a>
                </div>
                <div class="text-center col-6">
                  <button type="button" class="btn btn-info" @click="openModal(device)" >Remove</button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
  </div>
<Sidebar/>
</div>

<!-- MODAL BODY -->
<div class="modal fade" ref="myModal" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true" data-bs-theme="dark">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title fs-5 text-white" id="exampleModalLabel">Are you sure?</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <p class="text-white">Are you sure you want to delete "{{modalDevice.name}}"?</p>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary" @click="deleteDevice(modalDevice.device_id)">Delete!</button>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import Sidebar from '@/components/sidebar/Sidebar.vue'
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
      modalController: false,
      myModal: null,
      modalDevice: {
        name: null,
        device_id: null
      }
    }
  },
  beforeMount() {
    this.$store.dispatch('getUserDevices')
  },
  mounted() {
    this.myModal = new this.$bootstrap.Modal(this.$refs.myModal)
  },
  methods: {
    deleteDevice(device_id) {
      this.$store.dispatch('deleteDevice', device_id)
      .then(() => {
        this.myModal.hide()
        this.$store.dispatch('getUserDevices')
      })
    },
    openModal(device) {
      this.myModal.show()
      this.modalDevice.name = device.name
      this.modalDevice.device_id = device.uid
    },
    closeModal() {
      this.myModal.hide()
    },
    findDeviceIndex(object) {
      const index = this.$store.state.userDevices.findIndex(device => device.uid === object.uid)
      if (index !== -1) {
        return index
      } else {
        util.toastError("Device not found in memory, try refreshing! :<")
        return null
      }
    }
  }
}
</script>
<style>
.home {transition: 0.3s linear;}

body { 
  background-color: #212529 !important;
  height: 100vh;
}

</style>
