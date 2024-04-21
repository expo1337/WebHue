<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-md-4 text-start">
        <nav aria-label="breadcrumb">
          <ol class="breadcrumb">
            <li class="breadcrumb-item text-white"><a @click="this.$router.push('/')">Home</a></li>
            <li class="breadcrumb-item active text-white" aria-current="page">/</li>
            <li class="breadcrumb-item active text-white" aria-current="page">Controls</li>
          </ol>
        </nav>
      </div>
      <div class="d-flex justify-content-center col mt-md-4 pr-4">
          <h1 class="text-white">{{current_device.name}} Controls</h1>
          <h3 class="text-white">{{current_device.description}}</h3>
      </div>
      <div class="col-md-4">

      </div>
    </div>
    <div class="row justify-content-center mt-4">
      <div class="col-md-4 col-sm-12">
        <h3 class="text-white mb-mb-3 mt-md-4">Color Settings</h3>
        <div class="d-flex justify-content-center align-items-center">
        <ColorPicker theme="dark" :color="color" :sucker-hide="false" :sucker-canvas="suckerCanvas" :sucker-area="suckerArea" @changeColor="changeColor" @openSucker="openSucker"/>
        </div>
      </div>
      <div class="col-md-4 col-sm-12 justify-content-center">
        <div class="row">
          <h3 class="text-white mb-3 mt-4">Brightness Settings</h3>
          <div class="px-5">
            <div class="px-5">
              <Slider v-model="value" class="mt-5"/>
            </div>
          </div>
        </div>
        <div class="row justify-content-center px-5 mt-5">
          <div>
            <h3 class="text-white mb-4 mt-4">Power Settings</h3>
            <button v-if="new_power" class="btn btn-outline-success px-5" type="button" @click="changePower(false)">
            Power: On
          </button>
          <button v-else class="btn btn-outline-danger px-5" type="button" @click="changePower(true)">
            Power: Off
          </button>
          </div>
        </div>
      </div>
  </div>
    <div class="mt-md-5 mt-sm-2">
      <button v-if="isLoading" class="btn btn-outline-primary px-5" type="button" disabled>
      <span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
        Writing Command...
      </button>
      <button v-else class="btn btn-outline-primary px-5" type="button" @click="submitData()">
        Update Device!
      </button>
    </div>
  </div>
</template>

<script>

import VueCookie from "vue-cookie";
import { ColorPicker } from "vue-color-kit"
import Slider from '@vueform/slider'
import '@/theme/colorPicker.css'
import util from "@/util";

export default({
    components: {
      ColorPicker,
      Slider
    },
    data() {
        return{
            value: 0,
            color: null,
            new_brightness: 0,
            new_power: false,
            suckerCanvas: null,
            suckerArea: [],
            isSucking: false,
            isLoading: false,
        }
    },
    computed: {
      current_device() {
        const index = this.$route.params.data - 1;
        return this.$store.state.userDevices[index] || {};
      },
      current_power() {
        return this.current_device.power
      },
      current_color() {
        return this.current_device.color
      },
      current_brightness() {
        return this.current_device.brightness
      }
    },
    created() {
      this.color = "#" + this.current_color
      this.value = this.current_brightness
      this.new_power = this.current_power
    },
    mounted(){
      if (!VueCookie.get('refresh_token') && this.$store.state.accessToken === null) {
        this.$router.push('login')
      }
      else {
        if(this.$store.state.accessToken === null) {
          this.$store.dispatch("refreshAuthToken")
              .then(() => {
                this.$store.dispatch('getUserDevices')
                    .then(() => {
                      this.current_device = this.$store.state.userDevices [this.$route.params.data-1]
                    })
              })
        }
        else {
          this.$store.dispatch('getUserDevices')
        }
      }
    },
    methods: {
      changeColor(color) {
      this.color = color.hex.substr(1)
      },
      changePower(power) {
        this.new_power = power
        console.log(this.new_power, power)
      },
      async submitData() {
        this.isLoading = true
        if(this.current_power !== this.new_power)
        {
          await this.$store.dispatch('sendCommand', {
            address: this.current_device.bluetooth_address,
            command: util.generatePowerCommand(this.new_power)
          })
          await this.$store.dispatch('updateState', {
            uid: this.current_device.uid,
            power: this.new_power
          })
        }
        if(this.current_brightness !== this.value) {
          console.log(util.generateBrightnessCommand(this.value))
          await this.$store.dispatch('sendCommand', {
            address: this.current_device.bluetooth_address,
            command: util.generateBrightnessCommand(this.value)
          })
          await this.$store.dispatch('updateState', {
            uid: this.current_device.uid,
            brightness: this.value
          })
          
        }
        if(this.current_color !== this.color.substring(1)) {
          await this.$store.dispatch('sendCommand', {
            address: this.current_device.bluetooth_address,
            command: util.generateColorCommand(this.color)
          })
          await this.$store.dispatch('updateState', {
            uid: this.current_device.uid,
            color: this.color
          })
        }
        util.toastSuccess("Command written!")
        await this.$store.dispatch('getUserDevices')
            .then(() => {
              this.current_device = this.$store.state.userDevices [this.$route.params.data-1]
            })
        this.isLoading = false
        util.toastSuccess("Device state updated!")
      }
    }
})
</script>
<style src="@vueform/slider/themes/default.css"></style>
