<template>
  <div class="container section">
    <div class="row card-panel">
      <h1><center>Logeate</center></h1>
      <form @submit.prevent="login">
        <div class="row">
          <div class="input-field col s12">
            <i class="material-icons prefix">person</i>
            <input v-model="username" type="text" class="validate" required />
            <label for="Nombre de usuario">Nombre de usuario o Email</label>
          </div>
        </div>

        <div class="row">
          <div class="input-field col s12">
            <i class="material-icons prefix">lock</i>
            <input
              v-model="password"
              type="password"
              class="validate"
              required
            />
            <label for="Contraseña">Contraseña</label>
          </div>
        </div>

        <button
          class="btn waves-effect waves-yellow right"
          type="submit"
          name="login"
        >
          Logearte
          <i class="material-icons right">send</i>
        </button>
      </form>
    </div>
  </div>
</template>

<script>
import M from "materialize-css";

export default {
  name: "Login",
  data() {
    return {
      username: "",
      password: "",
    };
  },

  mounted() {
    M.AutoInit();
  },

  methods: {
    async login() {
      const path = "http://127.0.0.1:5000/login";
      const response = await fetch(path, {
        method: "POST",
        body: JSON.stringify({
          username: this.username,
          password: this.password,
        }),
        headers: {
          "Content-Type": "application/json",
        },
      });
      let data = await response.json();
      console.log("response: ", response);
      console.log("data: ", data);
      if (data["success"]) {
        const userID = data["profile"]["user_id"];
        localStorage.setItem("user_id", userID);
        this.$router.push({
          name: "posts",
          params: {
            username: data["profile"]["username"],
            user_id: parseInt(data["profile"]["user_id"]),
          },
        });
      } else {
        console.log("auth failed");
        document.getElementById("error").className = "";
      }
    },
  },
};
</script>

<style>
.hidden {
  display: none;
}
</style>
