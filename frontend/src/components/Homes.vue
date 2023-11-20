<template>
  <div class="carousel carousel-slider custom-carousel">
    <router-link to="/login">
      <a class="carousel-item"
        ><img
          src="https://i.imgur.com/TJOfkXv.png"
          style="max-width: 100%; max-height: 100%"
      /></a>
    </router-link>
    <router-link to="/ayuda">
      <a class="carousel-item"
        ><img
          src="https://i.imgur.com/tnhrUBu.png"
          style="max-width: 100%; max-height: 100%"
      /></a>
    </router-link>
  </div>
  <div class="center-align">
    <h4>¿Cómo funciona?</h4>
    <div class="center-align">
      <p>
        Esta es un medio en donde los estudiantes pueden complementar sus
        conocimientos y aprender a su ritmo.<br />
        Además, los profesores podrán monitorear a sus alumnos y mejorar su
        método de enseñanza.
      </p>
    </div>
  </div>
  <div class="center-align">
    <h4>¿Que ofrecemos?</h4>
  </div>
  <div class="row">
    <div class="center-align col s4">
      <img
        src="https://static.vecteezy.com/system/resources/previews/002/131/148/non_2x/virtual-classroom-rgb-color-icon-vector.jpg"
        alt=""
        style="max-width: 100px; max-height: 100px"
      />
      <h4>Campus virtual</h4>
      <p>
        Participa de nuestros cursos virtuales y programas <br />formativos para
        fortalecer tus capacidades
      </p>
    </div>
    <div class="center-align col s4">
      <img
        src="https://cdn-icons-png.flaticon.com/512/4862/4862723.png"
        alt=""
        style="max-width: 100px; max-height: 100px"
      />
      <h4>Perfil personal</h4>
      <p>
        Gestiona tu información personal y visualiza las <br />actividades que
        desarrollas.
      </p>
    </div>
    <div class="center-align col s4">
      <img
        src="https://cdn-icons-png.flaticon.com/512/747/747062.png"
        alt=""
        style="max-width: 100px; max-height: 100px"
      />
      <h4>Material educativo</h4>
      <p>
        Encuentra y utiliza materiales educativos digitales <br />para
        fortalecer tu aprendizaje.
      </p>
    </div>
  </div>
  <div class="row">
    <div class="center-align col s6">
      <img
        src="https://cdn-icons-png.flaticon.com/512/2170/2170765.png"
        alt=""
        style="max-width: 100px; max-height: 100px"
      />
      <h4>Comunidad</h4>
      <p>
        Accede a nuestra comunidad en línea con otros <br />alumnos dentro de
        nuestra plataforma
      </p>
    </div>
    <div class="center-align col s6">
      <img
        src="https://cdn-icons-png.flaticon.com/512/3044/3044095.png"
        alt=""
        style="max-width: 100px; max-height: 100px"
      />
      <h4>Grabacion de clases</h4>
      <p>Accede a clases virtuales y revisa las grabaciones.</p>
    </div>
  </div>
  <div class="row">
    <div class="center-align col s12 red darken-1">
      <div class="center-align white-text">
        <h4>Apóyanos</h4>
        <img
          src="https://img.freepik.com/iconos-gratis/plan_318-922549.jpg?w=2000"
          alt=""
          style="max-width: 100px; max-height: 100px"
        />
        <p>
          Juntos, estamos construyendo un futuro más brillante para los
          estudiantes. Tu apoyo es la clave para hacer que sus sueños se hagan
          realidad
        </p>
        <router-link to="/ayuda"
          ><a class="waves-effect waves-light btn-large amber darken-3"
            >Apoyanos<i class="material-icons right">attach_money</i></a
          ></router-link
        >
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
.custom-carousel {
  max-width: 100%; /* Cambia este valor según tus necesidades */
  min-height: 600px;
  margin: auto; /* Centra el carrusel en la página */
}
</style>

<script>
import M from "materialize-css";

export default {
  mounted() {
    M.AutoInit();

    document.addEventListener("DOMContentLoaded", () => {
      const elems = document.querySelectorAll(".sidenav");
      M.Sidenav.init(elems);

      const carousel = document.querySelector(".carousel");
      M.Carousel.init(carousel, {
        fullWidth: true,
        indicators: true,
      });

      setInterval(() => {
        const instance = M.Carousel.getInstance(carousel);
        instance.next();
      }, 5000);
    });
  },
};
</script>
