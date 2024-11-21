<template>
  <nav id="vue">
    <div class="menu-item"><router-link to="/">Home</router-link></div>
    <DropDown title="Items" />
    <div class="menu-item"><router-link to="/profile/">Profile</router-link></div>
  </nav>
</template>

<script lang="ts">
import DropDown from "./DropDownItems.vue";

export default {
  name: "navbar",
  components: {
    DropDown,
  },
};
</script>
