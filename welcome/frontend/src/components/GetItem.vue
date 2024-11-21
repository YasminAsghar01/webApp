<template>
  <br /><br />
  <div class="row gx-4 gx-lg-5">
    <input type="text" v-model="search" placeholder="Search for an item..." />
    <ul v-if="items.length > 0" class="row gx-4 gx-lg-5">
      <div v-for="item in filteredPosts" :key="item.id" class="col-md-4 mb-5">
        <br /><br />
        <div class="card">
          <img
            class="card-img-top img-fluid"
            :src="'http://localhost:8000' + item.image"
            v-bind:alt="item.image"
          />
          <div class="card-block">
            <h4 class="card-title">{{ item.title }}</h4>
            <p class="card-text">
              Description:{{ item.description }} <br /><br />
              Starting Price:{{ item.startingPrice }} <br /><br />
              Date and Time auction finishes:{{ item.finishDate }}
            </p>
          </div>
          <button @click="openProduct(item.id)">View this item</button>
        </div>
      </div>
      <div class="item error" v-if="search && !filteredPosts.length">
        <p>No results found!</p>
      </div>
    </ul>
    <h4 v-else>There are no items in this auction at the moment</h4>
  </div>
</template>

<script lang="ts">
export default {
  data() {
    return {
      search: "",
      items: [],
      user: 0,
    };
  },
  computed: {
    filteredPosts() {
      return this.items.filter(
        (item) =>
          item.description.toLowerCase().includes(this.search.toLowerCase()) ||
          item.title.toLowerCase().includes(this.search.toLowerCase())
      );
    },
  },
  methods: {
    async openProduct(itemId) {
      this.$router.push({ name: "test", params: { id: itemId, user: this.user } });
    },
  },
  async mounted() {
    let response = await fetch("http://localhost:8000/items/",{credentials:"include",});
    let data = await response.json();
    this.user = data.user;
    this.items = data.items;
  },
};
</script>
