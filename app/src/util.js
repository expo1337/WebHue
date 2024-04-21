import {toast} from 'vue3-toastify'
import store from './store'

export default{
    // LED CONTROLS - COMMAND CREATION
     generateColorCommand(color) {
        return "7e070503" + color + "10ef"
    },
    generateBrightnessCommand(brightness) {
         brightness = Number(brightness)
         let brightnessHex = brightness.toString(16)
         if (brightnessHex.length % 2 !== 0) {
            brightnessHex = '0' + brightnessHex;
        }
         return "7e0401" + brightnessHex + "01ffff00ef"
    },
    generatePowerCommand(power) {
         if(power) {
             return "7e0004f00001ff00ef"
         }
         else {
             return "7e0004000000ff00ef"
         }
    },
    //
    // TOAST UTILS
    toastError(message) {
        toast.error(message, {
            autoClose: 2000,
            position: toast.POSITION.BOTTOM_RIGHT,
            transition: toast.TRANSITIONS.SLIDE,
            theme: 'dark'
          });
    },
    toastSuccess(message) {
        toast.success(message, {
            autoClose: 2000,
            position: toast.POSITION.BOTTOM_RIGHT,
            transition: toast.TRANSITIONS.SLIDE,
            theme: 'dark'
        })
    },
    // JWT UTILS!
    async checkToken(token) {
        let isValid = true
        if(token) {
            const tokenParts = token.split('.')
            const encodedPayload = tokenParts[1];
            const decodedPayload = atob(encodedPayload);
            const payloadObj = JSON.parse(decodedPayload);
            const expireTimestamp = payloadObj.exp * 1000
            const currentTimestamp = Date.now()
            
            if(currentTimestamp + 2000 >= expireTimestamp) {
                isValid = false
            }
            else {
                isValid = true
            }
        }
        else {
            isValid = false
        }
        
        if(isValid) {
            return true
        }
        else {
            try {
                await store.dispatch('refreshAuthToken')
                return this.checkToken(store.state.accessToken)
            } catch (error) {
                this.toastError(error.message)
                return false
            }
        }
    }
}