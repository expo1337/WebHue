<script>

import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";
import {collapsed, toggleSidebar, sidebarWidth} from "@/components/sidebar/state";
import SidebarLink from "@/components/sidebar/SidebarLink.vue";

export default {
  components: {FontAwesomeIcon, SidebarLink},
  props: {},
  setup() {
    return {collapsed, toggleSidebar, sidebarWidth}
  },
  methods: {
    logout() {
      this.$store.dispatch('logout')
      this.$router.push('/login')
    }
  }
}
</script>


<template>
  <section>
  <div class="sidebar" :style="{ width: sidebarWidth}">
    <h1 class="heading">
      <span v-if="collapsed" class="heading">
        🌟
        <!--<img src="@/assets/logo.png" alt="" width="100">-->
      </span>
      <span v-else class="heading">WebHue</span>
    </h1>
    <!--<p v-if="!collapsed" class="welcome-user">{{this.$store.state.username}}</p>-->
    <hr class="mt-1">
    <SidebarLink icon="house" to="/">Home</SidebarLink>
    <SidebarLink icon="plus" to="/devices">Devices</SidebarLink>
    <SidebarLink icon="server" to="/server">Server</SidebarLink>
    <SidebarLink icon="circle-info" to="/help">Help</SidebarLink>
    <SidebarLink icon="fa-brands fa-bluetooth" to="/utils">Utils</SidebarLink>
    <div class="bottom-controls">
    </div>
    <span class="logout-button" @click="logout()">
        <font-awesome-icon icon="right-from-bracket" class="logout-icon"/>
        <transition name="fade">
          <span v-if="!collapsed" class="logout-text">
          Logout
          </span>
        </transition>
      </span>
    <span class="collapse-icon" :class="{'rotate-180': collapsed}" @click="toggleSidebar">
      <font-awesome-icon icon="angles-left" />
    </span>
    </div>
  </section>
</template>

<style>
:root {
  --sidebar-bg-color: #1a1d20;
  --sidebar-item-hover: #A954DD;
  --sidebar-item-active: #A933DD;
}
</style>
<style scoped>
  .sidebar {
    color: white;
    background-color: var(--sidebar-bg-color);
    float: left;
    position: fixed;
    z-index: 1;
    top: 0;
    left: 0;
    bottom: 0;
    padding: 0.5em;
    transition: 0.3s ease;
    display: flex;
    flex-direction: column;
  }
  .heading {
    transition: 0.3s ease;
    margin-top: 0.25em;
    font-weight: 100 !important;
    font-size: 1.2em;
  }
  .collapse-icon {
    position: absolute;
    bottom: 0;
    padding: 0.75em;
    color: white;
    transition: 0.3s linear;
  }
  .rotate-180 {
    transform: rotate(180deg);
    transition: 0.3s linear;
  }
  .welcome-user {
    transition: 0.3s ease;
  }
  .bottom-controls {
    bottom: 25px;
    position: absolute;
    align-items: center;
    justify-content: center;
  }
  .logout-button {
    display: flex;
    align-items: center;
    cursor: pointer;
    position: relative;
    font-weight: bold;
    user-select: none;
    margin: 0.1em;
    padding: 0.6em;
    border-radius: 0.25em;
    color: white;
    text-decoration: none;
    transition: 0.3s linear;
  }
  .logout-button:hover {
    background-color: var(--sidebar-item-hover);
  }
  .logout-icon {
    flex-shrink: 0;
    width: 27px;
    height: 27px;
    margin-right: 10px;
    transition: 0.3s linear;}
  .logout-text {
    transition: 0.3s ease;
  }
  .fade-enter-active,
  .fade-leave-active {
    transition: opacity 0.1s;
  }
  .fade-enter
  .fade-leave-to {
    opacity: 0;
  }


</style>