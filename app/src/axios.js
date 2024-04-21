import axios from 'axios'
import util from './util';
import store from './store';
import router from './router';

const noAuthApi = axios.create({
    baseURL: 'http://127.0.0.1:5000',
    //baseURL: 'http://10.10.40.229:5000',
    timeout: 30000,
})

const authApi = axios.create({
    baseURL: 'http://127.0.0.1:5000',
    timeout: 30000,
});

authApi.interceptors.request.use(
    async (config) => {
      const isTokenValid = await util.checkToken(store.state.accessToken)
      if(isTokenValid) {
        console.log("authAPI found invalid token")
        config.headers.Authorization = `Bearer ${store.state.accessToken}`;
        return config;
      }
      else {
        console.log("authAPI got invalid token")
        store.dispatch('logout')
        router.push('/login')
      }
    }
);

export { noAuthApi, authApi}