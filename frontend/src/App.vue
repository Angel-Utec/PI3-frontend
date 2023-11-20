<template>
  <div id="background-container">
    <HeaderBar>
      <link rel="preconnect" href="https://fonts.googleapis.com" />
      <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
      <link
        href="https://fonts.googleapis.com/css2?family=Young+Serif&display=swap"
        rel="stylesheet"
      />
      <nav class="custom-navbar">
        <div class="nav-wrapper">
          <a
            href="/"
            class="brand-logo black-text"
            style="
              font-family: 'Young Serif', serif;
              padding-left: 60px;
              padding-top: 5px;
            "
            >EducaTEC</a
          >
          <ul
            class="right hide-on-med-and-down center-align"
            style="margin-right: 40px"
          >
            <li style="margin-right: 40px">
              <router-link to="/quienes-somos">
                <a class="black-text">¿Quienes somos?</a>
              </router-link>
            </li>
            <li style="margin-right: 40px" v-if="showGuideSection">
              <router-link to="/guide">
                <a class="black-text">Guía</a>
              </router-link>
            </li>

            <li style="margin-right: 40px">
              <router-link to="/ayuda">
                <a class="black-text">Apóyanos</a>
              </router-link>
            </li>
            <!-- Verifica si el usuario está logeado y muestra su nombre -->
            <li v-if="isLoggedIn">
              <a class="black-text">{{ userName }}</a>
            </li>
            <!-- Verifica si el usuario NO está logeado y muestra el botón de inicio de sesión -->
            <li v-else>
              <router-link to="/login">
                <a
                  class="waves-effect waves-light btn-large black"
                  href="/login"
                >
                  LOG IN<i class="material-icons right">account_box</i>
                </a>
              </router-link>
            </li>
          </ul>
        </div>
      </nav>
    </HeaderBar>
    <div id="content-container">
      <div class="content">
        <router-view></router-view>
      </div>
    </div>
  </div>
</template>

<style>
body {
  overflow: hidden;
  margin: 0;
}

#background-container {
  position: relative;
  overflow: auto;
  height: 100vh;
}

#content-container {
  position: relative;
  z-index: 1;
  height: 100%;
}

#background-gif {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: -1; /* Asegura que el GIF esté en el fondo */
  pointer-events: none; /* Evita que el GIF interfiera con los elementos de primer plano */
}

.custom-navbar {
  height: 75px;
  padding: 0px;
  background-color: white;
}

.collection-item.avatar img.circle {
  max-width: 100px; /* Ajusta el tamaño máximo de la imagen */
  max-height: 100px; /* Ajusta el tamaño máximo de la imagen */
}

.collection-item.avatar img.circle {
  max-width: 100px; /* Ajusta el tamaño máximo de la imagen */
  max-height: 100px; /* Ajusta el tamaño máximo de la imagen */
}
#content-container {
  position: relative;
  z-index: 1;
  height: calc(100% - 75px);
}

footer.page-footer.black {
  position: fixed;
  bottom: 0;
  width: 100%;
}
</style>

<script>
import M from "materialize-css";

export default {
  data() {
    return {
      showGuideSection: false,
      isLoggedIn: false, // Agrega una propiedad para verificar si el usuario está logeado
      userName: "", // Agrega una propiedad para almacenar el nombre del usuario
    };
  },

  mounted() {
    // Verificar la presencia de un usuario en el LocalStorage
    const userId = localStorage.getItem("user_id");
    const name = localStorage.getItem("user_name");

    // Actualizar la propiedad showGuideSection según la presencia del usuario
    this.showGuideSection = !!userId;
    if (userId) {
      this.isLoggedIn = true;
      // Recupera el nombre del usuario desde donde lo tengas almacenado
      // Puedes ajustar esta lógica según cómo manejes la autenticación en tu aplicación
      this.userName = name; // Reemplaza con la lógica real
    }

    M.AutoInit();
    document.addEventListener("DOMContentLoaded", function () {
      var elems = document.querySelectorAll(".sidenav");
      M.Sidenav.init(elems);

      var carousel = document.querySelector(".carousel");
      M.Carousel.init(carousel, {
        fullWidth: true,
        indicators: true,
      });
    });
  },
};
</script>
