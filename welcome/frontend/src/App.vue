<template>
  <NavBarVue />
  <div>
    <router-view />
  </div>
</template>
<script lang="ts">

import NavBarVue from "./components/NavBar.vue";
export default {
  components: { NavBarVue}
};
</script>
