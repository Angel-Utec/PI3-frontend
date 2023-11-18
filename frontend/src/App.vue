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
            style="font-family: 'Young Serif', serif; padding-left: 60px"
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
            <li>
              <router-link to="/login"
                ><a
                  class="waves-effect waves-light btn-large black"
                  href="/login"
                  >LOG IN<i class="material-icons right">account_box</i></a
                ></router-link
              >
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
    };
  },

  mounted() {
    // Verificar la presencia de un usuario en el LocalStorage
    const userId = localStorage.getItem("user_id");

    // Actualizar la propiedad showGuideSection según la presencia del usuario
    this.showGuideSection = !!userId;
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
