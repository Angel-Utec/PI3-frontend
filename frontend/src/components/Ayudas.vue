<template>
  <div class="row">
    <div class="center-align col s12 blue with-background">
      <div class="center-align white-text">
        <h1>Contacta con nosotros</h1>
      </div>
    </div>
  </div>

  <div class="centered-container">
    <div class="centered-square">
      <div class="content-texto">
        <h5>A través de nuestro correo electrónico:</h5>
        <h6>educatec_oficial@gmail.com</h6>
        <h5>o de nuestro número telefónico:</h5>
        <h6>925369828</h6>
      </div>
    </div>
  </div>

  <div class="spacer"></div>

  <div class="row">
    <div class="center-align col s12 black">
      <div class="center-align white-text">
        <h4>¡Entérese de todo!</h4>
        <h6>
          Suscríbete para enterarte de todas las novedades de nuestro proyecto
        </h6>
        <div class="col s6 offset-s3">
          <div class="input-field center-align">
            <i class="material-icons prefix white-text">mail</i>
            <input id="icon_prefix" type="email" class="validate white-text" />
            <label for="icon_prefix" class="white-text"
              >Correo electrónico</label
            >
            <div class="button">
              <button
                class="btn waves-effect waves-light"
                type="submit"
                name="action"
              >
                Enviar
                <i class="material-icons right">send</i>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="fixed-action-btn">
    <a class="btn-floating pulse btn-large green">
      <i class="large material-icons">phone</i>
    </a>
    <ul>
      <li>
        <a
          href="https://chat.whatsapp.com/EUFw15B0gXhL3PjgQPMQtm"
          class="btn-floating red"
        >
          <i class="material-icons">phone_in_talk</i>
        </a>
      </li>
      <li>
        <a
          href="mailto:educatec_oficial@gmail.com?subject=Contacto&body=Hola, quisiera más información con respecto al proyecto."
          class="btn-floating yellow darken-1"
        >
          <i class="material-icons">contact_mail</i>
        </a>
      </li>
    </ul>
  </div>
</template>

<style>
.blue.with-background {
  background: url("https://semrex.co/wp-content/uploads/2018/07/banner4-833x317.png")
    center/cover;
  height: 200px;
}

.spacer {
  margin-top: 20px; /* Espaciado */
}

.centered-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 10vh; /* Ajusta la altura mínima de la página */
}

.centered-square {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 200px; /* Establece la altura que desees para el cuadrado */
  width: 500px; /* Establece el ancho que desees para el cuadrado */
  background-color: rgb(
    41,
    156,
    194
  ); /* Cambia el color de fondo a tu elección */
  border-radius: 20px; /* Aplica esquinas curvas ajustando el valor según tu preferencia */
}

.content-texto {
  text-align: center;
  padding: 20px;
  color: white;
}
</style>

<script>
import M from "materialize-css";

export default {
  mounted() {
    M.AutoInit();
    document.addEventListener("DOMContentLoaded", function () {
      var elems = document.querySelectorAll(".fixed-action-btn");
      M.FloatingActionButton.init(elems, {
        direction: "up",
        hoverEnabled: false,
      });
    });
  },
};
</script>
