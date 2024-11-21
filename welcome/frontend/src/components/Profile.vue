<template>
  <div class="menu-item" @click="isOpen = !isOpen">
    <a href="#">
      {{ title }}
    </a>
  </div>
</template>

<script lang="ts">
export default {
  name: "Profile",
  props: ["title"],
  data() {
    return {
      isOpen: false,
    };
  },
};
</script>
