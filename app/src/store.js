//import Vue from 'vue'
import {createStore} from 'vuex'
import {noAuthApi, authApi} from "@/axios";
import VueCookie from 'vue-cookie'
import util from './util';
import router from './router';

//Vue.use(Vuex)
export default createStore({
    state: {
        accessToken: null,
        loggedIn: false,
        userDevices: [],
        userId: null,
        username: null,
        ramLoad: [],
        cpuLoad: [],
        deleteDevice: null,
        nearbyDevices: [],
        deviceServices: [],
    },
    mutations: {
        updateStorage (state, { access, userId, username}){
            state.accessToken = access
            state.userId = userId
            state.username = username
            state.loggedIn = true
        },
        updateUserDevices (state, {devices}) {
            state.userDevices = JSON.parse(devices)
        },
        updateAuthToken (state, {accessToken}) {
            state.accessToken = accessToken
        },
        updateServerStats (state, {current_ram_usage, current_cpu_usage}) {
            if(state.cpuLoad.length > 20) {
                state.cpuLoad.shift()
                state.cpuLoad.push(current_cpu_usage)
            }
            else {
                state.cpuLoad.push(current_cpu_usage)
            }
            if(state.ramLoad.length > 20) {
                state.ramLoad.shift()
                state.ramLoad.push(current_ram_usage)
            }
            else {
                state.ramLoad.push(current_ram_usage)
            }
        },
        clearStorage (state) {
            state.accessToken = null
            state.loggedIn = false
            state.userDevices = []
            state.userId = null
            state.username = null
            state.ramLoad = []
            state.cpuLoad = []
            state.deleteDevice = null
            state.nearbyDevices = []
            state.deviceServices = []
        },
        updateNearbyDevices (state, {nearbyDevices}) {
            state.nearbyDevices = JSON.parse(nearbyDevices)
        },
        updateDeviceServices (state, {deviceServices}) {
            state.deviceServices = JSON.parse(deviceServices)
        }
    },
    actions: {
        register (context, credentials) {
            return new Promise((resolve) => {
                noAuthApi.post('/register', {
                    username: credentials.username,
                    password: credentials.password
                })
                    .then(response => {
                        context.commit('updateStorage', {access: response.data.access_token, userId: response.data.user_id, username:response.data.username})
                        if(credentials.remember === true) {
                            VueCookie.set('refresh_token', response.data.refresh_token)
                        }
                        resolve()
                    })
            })
        },
        login (context, credentials) {
            //return new Promise((resolve, reject) => {
                return new Promise((resolve) => {
                noAuthApi.post('/login', {
                    username: credentials.username,
                    password: credentials.password,
                })
                    .then(response => {
                        context.commit('updateStorage', {access: response.data.access_token, userId: response.data.user_id, username: response.data.username})
                        if(credentials.remember === true) {
                            VueCookie.set('refresh_token', response.data.refresh_token)
                        }
                        resolve()
                    })
                    .catch(error => {
                        // if (error.response.status === 401) {
                        //     util.toastError(error.response.data.message)
                        // }
                        console.log(error)
                    })
            })
        },
        loadTokensFromCookies (context) {
            context.commit("updateStorage", {access: VueCookie.get('access_token'), refresh: VueCookie.get('refresh_token')})
        },
        refreshAuthToken (context) {
            let refresh_token = VueCookie.get('refresh_token')
            return new Promise(resolve => {
                noAuthApi.post('/token_refresh', refresh_token,{headers: {Authorization: 'Bearer ' + refresh_token}
                })
                    .then(response =>{
                        context.commit('updateStorage', {access: response.data.access_token, username: response.data.username, userId: response.data.user_id})
                        resolve()
                        console.log(response.data)
                    })
                    .catch(error => {
                        context.commit('clearStorage')
                        console.log(error)
                        router.push('/login')
                    })
            })
        },
        getServerStats(context) {
            return new Promise((resolve) => {
                authApi.get('/get_stats')
                    .then(response => {
                        context.commit('updateServerStats', {current_ram_usage: response.data.ram_usage, current_cpu_usage: response.data.cpu_usage})
                        resolve()
                    })
                    .catch(error => {
                        util.toastError("Couldn't get server stats")
                        console.log(error)
                    })
            })
        },
        getUserDevices(context) {
            return new Promise((resolve) => {
                authApi.get('/get_devices')
                    .then(response => {
                        context.commit('updateUserDevices', { devices: response.data.devices });
                        resolve();
                        console.log("got devices");
                    })
                    .catch(error => {
                        util.toastError("Error getting devices")
                        console.log(error)
                    });
            });
        },
        logout(context) {
            context.commit('clearStorage')
            VueCookie.delete('refresh_token')
        },
        deleteDevice(context, device_id) {
            return new Promise((resolve) => {
                authApi.post('/delete_device', {uid: device_id})
                    .then(() => {
                        resolve();
                    })
                    .catch(error => {
                        util.toastError("Error deleting device")
                        console.log(error)
                    });
            })
        },
        addDevice(context, device) {
            return new Promise((resolve) => {
                authApi.post('/add_device', {
                    name: device.name,
                    bluetooth_address: device.bluetooth_address,
                    user_id: context.state.userId,
                    description: device.description
                })
                    .then(() => {
                        resolve()
                    })
                    .catch(error => {
                        util.toastError("Error adding device")
                        console.log(error)
                    });
            })
        },
        sendCommand(context, data) {
            return new Promise((resolve) => {
                authApi.post('/send_command', {
                    address: data.address,
                    command: data.command
                })
                    .then(() => {
                        resolve()
                    })
                    .catch(error => {
                        util.toastError("Command failed")
                        console.log(error)
                    })
            })
        },
        sendCustomCommand(context, data) {
            return new Promise((resolve) => {
                authApi.post('/send_command', {
                    address: data.address,
                    uuid: data.uuid,
                    command: data.command
                })
                    .then(() => {
                        resolve()
                    })
                    .catch(error => {
                        util.toastError("Command failed")
                        console.log(error)
                    })
            })
        },
        updateState(context, data) {
          return new Promise((resolve) => {
            authApi.post('/update_device', {
                  uid: data.uid,
                  brightness: data.brightness,
                  color: data.color,
                  power: data.power
              })
                  .then(() => {
                    resolve()
              })
                  .catch(error => {
                      util.toastError("Couldn't update device")
                      console.log(error)
                  })
          })
        },
        getNearbyDevices(context) {
            return new Promise((resolve) => {
                authApi.get('/get_nearby_devices')
                    .then(response => {
                        context.commit('updateNearbyDevices', {nearbyDevices: response.data.nearby_devices})
                        resolve();
                    })
                    .catch(error => {
                        util.toastError("Can't find devices")
                        console.log(error)
                    });
            })
        },
        getDeviceServices(context, data) {
            return new Promise((resolve) => {
                authApi.post('/get_device_services', {
                      address: data.address,
                  })
                      .then((response) => {
                        context.commit('updateDeviceServices', {deviceServices: response.data.services})
                        resolve()
                  })
                      .catch(error => {
                          util.toastError("No services found!")
                          console.log(error)
                      })
            })
        }
    }
})