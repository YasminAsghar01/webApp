<template>
  <div>
    <br><br><br>
    <div class="d-flex justify-content-center">
      <form class="border border-5 p-5" action="POST" @submit.prevent>
        <h2>REGISTER</h2><br>
        <div class="form-group row">
          <div>
            <input type="text" class="form-control" name= "userName" v-model= "userName"
            placeholder="Username"><br>
          </div>
        </div>

        <div class="form-group row">
          <div>
            <input type="text" class="form-control" name= "firstName" v-model= "firstName"
            placeholder="First Name"><br>
          </div>
        </div>

        <div class="form-group row">
          <div>
            <input type="text" class="form-control" name= "lastName"  v-model= "lastName"
            placeholder="Last Name"><br>
          </div>
        </div>

        <div class="form-group row">
          <div>
            <label class="custom-control-label" for="duration">Date of Birth: </label>
            <input type="text" class="form-control" id= "dob" name= "dob"
            v-model= "dob" placeholder="YYYY-MM-DD"><br>
          </div>
        </div>

        <div class="form-group row">
          <div>
            <input type="email" class="form-control" placeholder="email"
            name= "email" v-model= "email"><br>
          </div>
        </div>

        <div class="form-group row">
          <div>
            <input type="password" class="form-control" name= "password"  v-model= "password"
            placeholder="Password"><br>
          </div>
        </div>

        <div class="form-group row">
          <div>
            <button type="submit" class="btn btn-success" @click="createUser">Submit Registration</button>
          </div>
        </div>
      </form>
    </div> <br>
  </div>
</template>


<script>
export default{
  data() {
    return {
      users: [],
      userName:"",
      firstName: "",
      lastName: "",
      dob: "",
      email: "",
      password:"",
    }
  },

  async mounted(){
    // mounted fetches the users
    let response= await fetch("http://localhost:8000/api/users/")
    let data= await response.json()
    this.users= data.users
  },

  methods:{

    async createUser() {
    // POST request using fetch with async/await
    // sending requests to json
    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      // stringify objects
      body: JSON.stringify({
          userName: this.userName,
          firstName: this.firstName,
          lastName: this.lastName,
          dob: this.dob,
          email: this.email,
          password: this.password,
      })
    };
    // clears input fields after submitting form
    this.userName= "";
    this.firstName= "";
    this.lastName= "";
    this.dob= "";
    this.email= "";
    this.password= "";
    // fetches using GET method from users api
    let response = await fetch("http://127.0.0.1:8000/api/users/", requestOptions);
    let data = await response.json();
    this.users = data.users;
  },
  }
}
</script>
