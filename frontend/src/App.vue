<template>
  <div id="background-container">
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Young+Serif&display=swap"
      rel="stylesheet"
    />
    <HeaderBar>
      <nav class="custom-navbar">
        <div class="nav-wrapper">
          <a
            href="#!"
            class="brand-logo black-text"
            style="font-family: 'Young Serif', serif; padding-left: 60px"
            >EducaTEC</a
          >
          <ul
            class="right hide-on-med-and-down center-align"
            style="margin-right: 40px"
          >
            <li style="margin-right: 40px">
              <a class="black-text">¿Quienes somos?</a>
            </li>
            <li style="margin-right: 40px"><a class="black-text">Guía</a></li>
            <li style="margin-right: 40px">
              <a class="black-text">Cursos</a>
            </li>
            <li style="margin-right: 40px">
              <a class="black-text">Apóyanos</a>
            </li>
            <li>
              <a class="waves-effect waves-light btn-large black"
                >LOG IN<i class="material-icons right">account_box</i></a
              >
            </li>
          </ul>
        </div>
      </nav>
    </HeaderBar>
    <div class="carousel carousel-slider">
      <a class="carousel-item" href=""
        ><img src="https://i.imgur.com/TJOfkXv.png"
      /></a>
      <a class="carousel-item" href=""
        ><img src="https://i.imgur.com/tnhrUBu.png"
      /></a>
    </div>
    <div class="center-align">
      <h4>¿Cómo funciona?</h4>
      <p>
        Esta es un medio en donde los estudiantes pueden complementar sus
        conocimientos y aprender a su ritmo. Además, los profesores podrán
        monitorear a sus alumnos y mejorar su método de enseñanza.
      </p>
    </div>
    <div class="center-align">
      <h4>¿Que ofrecemos?</h4>
    </div>
    <div
      class="center-align"
      style="
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100%;
        overflow-y: auto;
      "
    >
      <ul class="collection">
        <li class="collection-item avatar">
          <img
            src="https://static.vecteezy.com/system/resources/previews/002/131/148/non_2x/virtual-classroom-rgb-color-icon-vector.jpg"
            alt=""
            class="circle"
            style="max-width: 60px; max-height: 60px"
          />
          <span class="title">Campus virtual</span>
          <p>
            Participa de nuestros cursos virtuales y programas formativos para
            fortalecer tus capacidades
          </p>
        </li>
        <li class="collection-item avatar">
          <img
            src="https://cdn-icons-png.flaticon.com/512/4862/4862723.png"
            alt=""
            class="circle"
            style="max-width: 60px; max-height: 60px"
          />
          <span class="title">Perfil personal</span>
          <p>
            Gestiona tu información personal y visualiza las actividades que
            desarrollas.
          </p>
        </li>
        <li class="collection-item avatar">
          <img
            src="https://cdn-icons-png.flaticon.com/512/747/747062.png"
            alt=""
            class="circle"
            style="max-width: 60px; max-height: 60px"
          />
          <span class="title">Material educativo</span>
          <p>
            Encuentra y utiliza materiales educativos digitales para fortalecer
            tu aprendizaje.
          </p>
        </li>
        <li class="collection-item avatar">
          <img
            src="https://cdn-icons-png.flaticon.com/512/3044/3044095.png"
            alt=""
            class="circle"
            style="max-width: 60px; max-height: 60px"
          />
          <span class="title">Grabacion de clases</span>
          <p>Accede a clases virtuales y revisa las grabaciones.</p>
        </li>
        <li class="collection-item avatar">
          <img
            src="https://cdn-icons-png.flaticon.com/512/2170/2170765.png"
            alt=""
            class="circle"
            style="max-width: 60px; max-height: 60px"
          />
          <span class="title">Comunidad</span>
          <p>
            Accede a nuestra comunidad en línea con otros alumnos dentro de
            nuestra plataforma
          </p>
        </li>
      </ul>
    </div>
    <div
      class="center-align"
      style="
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100%;
      "
    >
      <div class="card" style="width: 400px; height: 400px">
        <div class="card-image waves-effect waves-block waves-light">
          <img
            class="activator"
            src="https://static.vecteezy.com/system/resources/previews/007/776/528/non_2x/donation-rgb-color-icon-financial-support-and-grant-sponsoring-and-funding-support-with-cash-isolated-illustration-simple-filled-line-drawing-editable-stroke-vector.jpg"
          />
        </div>
        <div class="card-content">
          <span class="card-title activator grey-text text-darken-4"
            >Se parte de nuestro proyecto<i class="material-icons right"
              >more_vert</i
            ></span
          >
          <p><a href="#">Apóyanos</a></p>
        </div>
        <div class="card-reveal">
          <span class="card-title grey-text text-darken-4"
            >Apóyanos<i class="material-icons right">close</i></span
          >
          <p>
            Juntos, estamos construyendo un futuro más brillante para los
            estudiantes. Tu apoyo es la clave para hacer que sus sueños se hagan
            realidad
          </p>
        </div>
      </div>
    </div>
    <footer class="page-footer">
      <div class="container">
        <div class="row">
          <div class="col s12">
            <p class="grey-text text-lighten-4">© 2023 EducaTEC</p>
          </div>
        </div>
      </div>
    </footer>
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
</style>

<script>
import M from "materialize-css";

export default {
  mounted() {
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
