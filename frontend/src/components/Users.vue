<template>
  <div>
    <div class="container section">
      <div class="row card-panel">
        <h4>
          <center>Registrarse</center>
        </h4>
        <form @submit.prevent="PublicarUsuario">
          <div class="row">
            <div class="input-field col s12">
              <i class="material-icons prefix">person</i>
              <input
                v-model="user.username"
                type="text"
                class="validate"
                required
              />
              <label for="Nombre de usuario">Nombre de usuario</label>
            </div>
          </div>

          <div class="row">
            <div class="input-field col s12">
              <i class="material-icons prefix">lock</i>
              <input
                v-model="user.password"
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
            name="enviar"
          >
            Enviar
            <i class="material-icons right">send</i>
          </button>
        </form>
      </div>
    </div>
    <div class="container section">
      <div class="col s12 m8 offset-m2 l6 offset-l3">
        <div class="row card-panel low-opacity">
          <h4>
            <center>Usuarios registrados</center>
          </h4>
        </div>
        <div class="row-b">
          <div
            v-for="user in users"
            :key="user.id"
            class="card-b card sticky-action large"
          >
            <div class="card-image waves-effect waves-block waves-green">
              <img class="activator" src="https://i.imgur.com/RfXVXzq.jpg" />
            </div>
            <div class="card-content">
              <center>
                <p style="font-size: x-large">
                  Usuario:
                  <span
                    class="activator text-darken-1"
                    style="color: green; font-weight: bold"
                    >{{ user.username }}</span
                  >
                </p>
              </center>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Services from "@/services/Services";
import M from "materialize-css";

export default {
  name: "User-manager",

  data() {
    return {
      user: {
        username: "",
        password: "",
      },
      users: [],
    };
  },

  mounted() {
    M.AutoInit();
    let elems = document.querySelectorAll("select");
    this.select_instances = M.FormSelect.init(elems, null);
  },

  created() {
    this.getUsers();
  },
  methods: {
    getUsers() {
      Services.getUsers().then((response) => {
        this.users = response.data.users;
      });
    },
    PublicarUsuario() {
      const user = { ...this.user };
      Services.postUser(user).then((response) => {
        this.users = response.data.users;
      });
    },
  },
};
</script>

<style>
.card-b {
  display: inline-block;
  margin: 1rem;
  width: 30rem;
  height: 20rem;
  position: relative;
  overflow: hidden;
}

.row-b {
  overflow-x: auto;
  white-space: nowrap;
}

.row.card-panel.low-opacity {
  background-color: rgba(255, 255, 255, 0.8);
}
</style>
