<template>
    <img
    style="height: 100px"
    :src= user.image
    class="rounded mx-auto d-block"
    alt="profile"
  />
  <input type="file" accept="image/*" class="fileInput fileUpload" id="image"
  />
  <input placeholder="user name" v-if="user.editing" v-model="username" />
  <h2 v-else>{{ user.username }}</h2>
  <input placeholder="first name" v-if="user.editing" v-model="first_name" />
  <h2 v-else>{{ user.first_name }}</h2>
  <input placeholder="last name" v-if="user.editing" v-model="last_name" />
  <h2 v-else>{{ user.last_name }}</h2>
  <input placeholder="email" v-if="user.editing" v-model="email" />
  <h2 v-else>{{ user.email }}</h2>
  <input placeholder="must be YYYY-MM-DD" v-if="user.editing" v-model="dob" />
  <h2 v-else>{{ user.dob }}</h2>
  <button v-if="!user.editing" @click="user.editing = true">edit</button>
  <button v-else @click="update(user)">save</button>
</template>

<script lang="ts">
export default {
  data() {
    return {
      user: {
        username: "",
        id: 1,
        first_name: "",
        last_name: "",
        dob: "",
        email: "",
        password: "",
        image: "",
        editing: false,
      },
      userId: 1,
      fileField: File,
      username: "",
      first_name: "",
      last_name: "",
      dob: "",
      email: "",
      image: "",
      password: "",
    };
  },
  methods: {


    async fetchUser() {
    let response1 = await fetch("http://localhost:8000/api/users/", {
        credentials: "include",
      });
      let data1 = await response1.json();
      const userId = data1.id;
      let response = await fetch(`http://localhost:8000/api/user/${userId}/`);
      let data = await response.json();
      this.user = data;
      this.user.image = 'http://localhost:8000' + data.image
    },

    async update(user) {
        const fileField = (<HTMLInputElement>document.getElementById("image"))
        .files![0].name;
      const pictureUrl = "/images/" + String(fileField)
      const fullPictureUrl = 'http://localhost:8000' + pictureUrl;
      this.image = fullPictureUrl;
      const pushUpdate = {
        method: "PUT",
        headers: { "Content-Type": "application/json" },

        body: JSON.stringify({
          username: this.username,
          first_name: this.first_name,
          last_name: this.last_name,
          dob: this.dob,
          password: this.password,
          email: this.email,
          image: pictureUrl
        }),
      };
      fetch(`http://localhost:8000/api/user/${user.id}/`, pushUpdate).then(
        (data) => this.updateValue(data, user)
      );
    },
    updateValue(data, user) {
      user.username = this.username;
      (user.first_name = this.first_name),
        (user.last_name = this.last_name),
        (user.dob = this.dob),
        (user.email = this.email);
        (user.image = this.image);
;      user.editing = false;
    },
  },

  mounted() {
    this.fetchUser();
  },
};
</script>
