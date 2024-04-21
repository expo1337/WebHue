<template>
  <nav id="sidebar" class="bg-dark position-fixed">
    <div class="sidebar-header">
      <h4 class="mt-2 mb-4 text-light">⚡️ Smart Controls</h4>
    </div>

    <ul class="list-unstyled components">
      <li class="mb-2 ">
        <router-link to="/">Home</router-link>
      </li>
      <li class="mb-2">
        <router-link class="text-light" to="/devices">Devices</router-link>
      </li>
      <li class="mb-2">
        <a class="text-light" data-bs-toggle="collapse" href="#collapseExample" role="button" aria-expanded="false" aria-controls="collapseExample">
            Connected Devices
        </a>
      </li>
        <div class="collapse" id="collapseExample">
            Some placeholder content for the collapse component. This panel is hidden by default but revealed when the user activates the relevant trigger.
        </div>
      <li class="mb-2">
        <router-link class="text-light" to="/contact">Contact</router-link>
      </li>
      <li class="mb-2">
        <router-link class="text-light" to="/contact">Unsupported Devices</router-link>
      </li>
    </ul>
    <ul class="nav nav-pills flex-column mb-auto">
      <li class="nav-item">
        <router-link to="/devices" class="nav-link" exact>
          <svg class="bi me-2" width="16" height="16"><use xlink:href="#home"/></svg>
          Devices
        </router-link>
      </li>

      <li class="nav-item">
        <a href="/" class="nav-link active" aria-current="page">
          <svg class="bi me-2" width="16" height="16"><use xlink:href="#home"/></svg>
          Home
        </a>
      </li>
      <li>
        <a href="/devices" class="nav-link text-white">
          <svg class="bi me-2" width="16" height="16"><use xlink:href="#devices"/></svg>
          Dashboard
        </a>
      </li>
      <li>
        <a href="#" class="nav-link text-white">
          <svg class="bi me-2" width="16" height="16"><use xlink:href="#table"/></svg>
          Orders
        </a>
      </li>
      <li>
        <a href="#" class="nav-link text-white">
          <svg class="bi me-2" width="16" height="16"><use xlink:href="#grid"/></svg>
          Products
        </a>
      </li>
      <li>
        <a href="#" class="nav-link text-white">
          <svg class="bi me-2" width="16" height="16"><use xlink:href="#people-circle"/></svg>
          Customers
        </a>
      </li>
    </ul>
    <button class="btn btn-danger" @click="logout()">Logout</button>
  </nav>
</template>

<script>
export default {
  name: 'SideBar',
  props: {
  },
  methods: {
    async logout() {
      await this.$store.dispatch('logout')
      this.$router.push('/login')
    }
  }
}

</script>

<style scoped lang="scss">
/* Adjust the position and width of the sidebar */
#sidebar {
  width: 300px; /* Adjust the width as needed */
  position: fixed;
  top: 0;
  left: 0;
  height: 100%;
  z-index: 9999;
  padding-top: 20px; /* Add padding to the top if needed */
}

/* Style the sidebar header and list items */
.sidebar-header {
  text-align: center;
}




</style>
