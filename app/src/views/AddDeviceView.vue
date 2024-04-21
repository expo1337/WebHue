<template>
  <div class="home" :style="{'margin-left': sidebarWidth}" data-bs-theme="dark">
    <div class="container pt-5">
      <h2 class="mb-4 text-white">⚡️ Add a new device</h2>
      <form>
        <div class="form-group row mb-4">
            <label for="staticEmail" class="col-sm-12 col-form-label text-white">Device Name</label>
            <div class="col-sm-4 mx-auto">
            <input type="text" class="form-control" placeholder="Device Name" v-model="name">
            </div>
        </div>
        <div class="form-group row mb-4">
            <label for="staticEmail" class="col-sm-12 col-form-label text-white">Bluetooth Address</label>
            <div class="col-sm-4 mx-auto">
            <input type="text" class="form-control" placeholder="FF:FF:FF:FF:FF" v-model="bluetooth_address">
            </div>
        </div>
        <div class="form-group row mb-4">
            <label for="staticEmail" class="col-sm-12 col-form-label text-white">Device Description</label>
            <div class="col-sm-4 mx-auto">
            <textarea class="form-control" rows="4" v-model="description"></textarea>
            </div>
        </div>
        <div class="form-group row mb-4">
            <div class="col-sm-4 mx-auto">
              <div class="d-flex flex-wrap justify-content-center gap-4">
                <div class="btn btn-outline-danger px-5" @click="addDevice()">Submit</div>
                <div class="btn btn-outline-info px-5" @click="resetForm()">Reset</div>
              </div>
            </div>
        </div>
      </form>
    </div>
    <Sidebar/>
  </div>
</template>

<script>
import Sidebar from '@/components/sidebar/Sidebar.vue'
import {sidebarWidth} from "@/components/sidebar/state";
export default {
  name: 'HomeView',
  components: {
    Sidebar,
  },
  data() {
    return {
      name: '',
      bluetooth_address: '',
      description: ''
    }
  },
  methods: {
    addDevice() {
      this.$store.dispatch('addDevice', {
        name: this.name,
        bluetooth_address: this.bluetooth_address,
        description: this.description
      })
      .then(() => {
        this.$router.push('/')
      })
    },
    resetForm() {
      this.name = '',
      this.bluetooth_address = '',
      this.description = ''
    }
  },
  setup() {return {sidebarWidth}},
}
</script>
<style>
</style>
