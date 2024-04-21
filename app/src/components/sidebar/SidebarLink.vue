<script>
import {computed} from 'vue'
import {useRoute} from "vue-router"
import {collapsed} from "@/components/sidebar/state"

export default {
  props: {
    to: { type: String, required: true},
    icon: { type: String, required: true}
  },
  setup(props) {
    const route = useRoute()
    const reqPath = props.to
    const isActive = computed(() => route.path === props.to)
    if(isActive.value) {console.log(isActive.value)}
    return {isActive, collapsed, route, reqPath  }
  }
}


</script>

<template>
  <router-link :to="to" class="link" :class="{ active: reqPath === route.path }">
    <font-awesome-icon :icon="icon" class="icon" />
    <transition name="fade">
      <span v-if="!collapsed" class="link-text" :class="{ 'collapsed': collapsed }" >
        <slot/>
      </span>
    </transition>
  </router-link>
</template>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.1s;
}
.fade-enter
.fade-leave-to {
  opacity: 0;
}
.link {
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
.link-text {
  margin-top: 2px;
}
.link:hover {
  background-color: var(--sidebar-item-hover);
}
.router-link-active {
  background-color: var(--sidebar-item-active);
}
.link .icon {
  flex-shrink: 0;
  width: 27px;
  height: 27px;
  margin-right: 10px;
  transition: 0.3s linear;
}
.collapsed {
  opacity: 0;
}
</style>