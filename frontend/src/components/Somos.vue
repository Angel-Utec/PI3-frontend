<template>
  <div class="row">
    <div class="center-align col s12 lightblue with-background"></div>
  </div>
  <div class="center-align blue-text">
    <h1>¿Quienes somos?</h1>
  </div>
  <div class="center-align">
    <h5>¡Bienvenidos a EducaTEC!</h5>
    <p>
      En EducaTEC, creemos que la educación es el motor que impulsa el progreso
      y el cambio en una sociedad. Nuestra pasión radica en empoderar a la<br />
      juventud peruana y brindar oportunidades educativas de calidad para todos,
      sin importar dónde se encuentren.
    </p>
    <h5>Misión:</h5>
    <p>
      En EducaTEC, nuestra misión es habilitar la educación en Perú, extendiendo
      su alcance a los sectores rurales y reforzando<br />
      la calidad de la educación en todo el país. Nos dedicamos a empoderar a
      estudiantes de 4to y 5to de secundaria, brindándoles<br />
      acceso a clases grabadas por profesionales comprometidos y recursos
      educativos excepcionales.<br />
      Nuestra misión es preparar a los jóvenes peruanos para un futuro exitoso y
      lleno de oportunidades.
    </p>
    <h5>Visión:</h5>
    <p>
      Nuestra visión es liderar el cambio en el sistema educativo peruano.
      Soñamos con un país donde cada estudiante, sin importar su ubicación,<br />
      tenga igualdad de acceso a una educación de calidad. Buscamos inspirar a
      la próxima generación de líderes y creadores, transformando vidas y<br />
      comunidades a través del poder de la educación.
    </p>
  </div>
  <div class="center-align">
    <h3>Conócenos</h3>
    <h5>Nuestro Equipo</h5>
    <p>
      Nuestro equipo está formado por estudiantes apasionados que han dedicado
      tiempo y esfuerzo a este proyecto. Cada uno de nosotros aporta
      habilidades<br />
      y conocimientos únicos para garantizar que EducaTEC sea una plataforma de
      educación excepcional.
    </p>
    <div class="row">
      <div v-for="(member, index) in teamMembers" :key="index" class="col s3">
        <img class="responsive-img" src="../assets/users.png" />
        <h5>{{ member.name }}</h5>
      </div>
    </div>
  </div>
  <div class="center-align red darken-1">
    <h5 class="white-text">
      Tambien puedes consultar en nuestra sección de preguntas frecuentes:
    </h5>
    <router-link to="/FAQ"
      ><a class="waves-effect waves-light btn-large amber darken-3"
        >FAQ<i class="material-icons right">send</i></a
      ></router-link
    >
  </div>
  <div class="spacer"></div>
</template>

<style>
.responsive-img {
  height: 150px; /* Establece la altura que desees para el cuadrado */
  width: 150px; /* Establece el ancho que desees para el cuadrado */
}

.lightblue.with-background {
  background: url("../assets/estudiantes.png") center/cover;
  height: 500px;
}

.spacer {
  margin-top: 200px; /* Espaciado */
}
</style>

<script>
export default {
  data() {
    return {
      // Aquí puedes agregar la información de tu equipo
      teamMembers: [
        { name: "Angel Tito" },
        { name: "Ronaldo Flores" },
        { name: "Rodo Vilcaromero" },
        { name: "Mauricio Diaz" },
        // Puedes agregar más miembros según sea necesario
      ],
    };
  },
  // ... (métodos y otros detalles)
};
</script>
