<template>
  <div>
    <div class="row center-align">
      <h3>Clase №{{ currentClass + 1 }}:</h3>
      <iframe
        :src="currentVideo"
        title="YouTube video player"
        width="1280"
        height="720"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        allowfullscreen
      ></iframe>
    </div>
    <div class="center-align" v-if="claseActual < 0">
      <button
        class="waves-effect waves-light center-align btn-large red"
        @click="loadNextClass"
      >
        Siguiente clase<i class="material-icons right">arrow_forward</i>
      </button>
    </div>
    <div class="center-align">
      <router-link to="/quiz-matematicas" v-if="claseActual === 0">
        <a class="waves-effect waves-light btn-large red">
          Inicie el Quiz<i class="material-icons right">send</i>
        </a>
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      currentClass: 0, // Índice de la clase actual
      videos: ["https://www.youtube.com/embed/xm4rnvzC05M?si=TBiD8n-XxLTbfXw"],
      claseActual: 0,
    };
  },
  computed: {
    currentVideo() {
      return this.videos[this.currentClass];
    },
  },
  methods: {
    loadNextClass() {
      // Incrementa el índice de la clase actual
      this.currentClass++;
      this.claseActual++;

      // Si quieres hacer un bucle a la primera clase después de la última, puedes usar lo siguiente:
      // this.currentClass = (this.currentClass + 1) % this.videos.length;

      // Puedes agregar lógica adicional aquí según tus necesidades
    },
  },
};
</script>
