<template>
  <title>Auction App</title>
  <form>
    <label for="exampleFormControlInput1" class="form-label">Title</label>
    <input v-model="title" class="form-control" />
    <div class="mb-3">
      <label for="exampleFormControlInput1" class="form-label"
        >Starting Price(£)</label
      >
      <input v-model="startingPrice" class="form-control" />
    </div>
    <div class="form-group">
      <label for="exampleFormControlTextarea1">Description</label>
      <textarea
        v-model="description"
        class="form-control"
        id="exampleFormControlTextarea1"
      ></textarea>
    </div>
    <div class="form-group">
      <label for="image">picture</label>
      <input
        type="file"
        accept="image/*"
        class="fileInput fileUpload"

        id="image"
      />
    </div>
    <label>End date</label>
    <input
      v-model="finishDate"
      type="date"
      name="begin"
      placeholder="dd-mm-yyyy"
      min="1997-01-01"
      max="2030-12-31"
    />
  </form>
  <button @click="submit()" class="btn btn-dark">Submit</button>
</template>

<script lang="ts">
export default {
  data() {
    return {
      items: [
        {
          title: "",
          description: "",
          finishDate: "",
          startingPrice: "",
        },
      ],
      id: 0,
      image: "",
      url: "",
      title: "",
      description: "",
      finishDate: "",
      startingPrice: "",
      user : 0,
      fileField: File,
      formData: FormData,
    };
  },
  methods: {

    async submit() {
      const formData = new FormData();
      formData.append("title", this.title);
      formData.append("startingPrice", this.startingPrice);
      formData.append("description", this.description);
      formData.append("finishDate", this.finishDate);
      formData.append("owner", this.user);

      const fileField = (<HTMLInputElement>document.getElementById("image"))
        .files![0].name;
      const pictureUrl = "/images/" + String(fileField)
      formData.append("image", pictureUrl);


      let response = await fetch("http://127.0.0.1:8000/items/", {
        method: "POST",
        body: formData
      });
      if (response.status == 200) {
        alert("This item has been created!")
        window.location.reload();
      } else {
        alert("This item could not be created!")
      }
    },
  },
  async mounted() {
    let response = await fetch("http://localhost:8000/items/",{credentials:"include",});
    let data = await response.json();
    this.user = data.user;
  },
};
</script>

