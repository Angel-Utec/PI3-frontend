<template>
  <div class="login-container">
    <div class="photo-section">
      <div class="left">
        <!-- Agregado: Imagen al lado izquierdo -->
        <img
          src="https://pathwayport.com/saasland/images/login@4x.png"
          alt="Nuva Image"
        />
      </div>
      <div class="form-section">
        <h1>Ingrese a su cuenta</h1>
        <form @submit.prevent="login">
          <div class="row">
            <div class="input-field col s12">
              <i class="material-icons prefix">email</i>
              <input v-model="username" type="text" class="validate" required />
              <label for="email">Nombre de usuario:</label>
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
              <label for="password">Contraseña:</label>
            </div>
          </div>

          <button
            class="btn waves-effect waves-yellow right"
            type="submit"
            name="login"
          >
            Log in
            <i class="material-icons right">send</i>
          </button>
        </form>
      </div>
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
      const path = "http://54.89.201.63:5000/login";
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
        const name = data["profile"]["username"];
        localStorage.setItem("user_id", userID);
        localStorage.setItem("user_name", name);
        this.$router.push({
          name: "guide",
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

.container {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
}

.card-panel {
  display: flex;
  align-items: center;
}

.left {
  margin-left: 40px;
  margin-right: 20px;
}

.left img {
  width: 600px; /* Ajusta el tamaño según sea necesario */
  height: auto;
}

.right {
  flex-grow: 1;
}

h1 {
  font-size: 48px;
  font-weight: 600;
  color: #000000;
  opacity: 0.85;
  margin-bottom: 20px;
}

label {
  font-size: 12.5px;
  color: #000;
  opacity: 0.8;
  font-weight: 400;
}

input {
  font-size: 16px;
  padding: 20px 0px;
  height: 56px;
  border: none;
  border-bottom: solid 1px rgba(0, 0, 0, 0.1);
  background: #fff;
  width: 280px;
  box-sizing: border-box;
  transition: all 0.3s linear;
  color: #000;
  font-weight: 400;
  -webkit-appearance: none;
}

input:focus {
  border-bottom: solid 1px rgb(182, 157, 230);
  outline: 0;
  box-shadow: 0 2px 6px -8px rgba(182, 157, 230, 0.45);
}

button {
  -webkit-appearance: none;
  width: auto;
  min-width: 100px;
  border-radius: 24px;
  text-align: center;
  padding: 15px 40px;
  margin-top: 5px;
  background-color: rgb(182, 157, 230);
  color: #fff;
  font-size: 14px;
  margin-left: auto;
  font-weight: 500;
  box-shadow: 0px 2px 6px -1px rgba(0, 0, 0, 0.13);
  border: none;
  transition: all 0.3s ease;
  outline: 0;
}

button:hover {
  transform: translateY(-3px);
  box-shadow: 0 2px 6px -1px rgba(182, 157, 230, 0.65);
}

button:active {
  transform: scale(0.99);
}

button:focus {
  outline: none;
}

.material-icons {
  color: rgba(0, 0, 0, 0.26);
  font-size: 24px;
  display: inline-block;
  font-family: "Material Icons";
  font-weight: normal;
  font-style: normal;
  line-height: 1;
  text-transform: none;
  letter-spacing: normal;
  word-wrap: normal;
  white-space: nowrap;
  direction: ltr;
  -webkit-font-feature-settings: "liga";
  -webkit-font-smoothing: antialiased;
}

.material-icons.prefix {
  margin-right: 10px;
  margin-top: 20px;
}

.material-icons.prefix ~ input {
  margin-left: 40px;
}

.material-icons.right {
  margin-left: 10px;
  margin-top: 5px;
}

.material-icons.right ~ span {
  margin-right: 10px;
}

@media only screen and (max-width: 600px) {
  .card-panel {
    width: 100%;
    margin: auto;
    margin-top: 50px;
  }
}
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.photo-section {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #f3f2f2;
}

.photo-section img {
  max-width: 100%;
  max-height: 100%;
}

.form-section {
  flex: 1;
  padding: 80px; /* Ajusta el padding según sea necesario */
  background: #fefefe;
  border-radius: 4px;
  box-shadow: 0px 2px 6px -1px rgba(0, 0, 0, 0.12);
  box-sizing: border-box;
}
</style>
