<template>
  <div>
    <div class="row center-align">
      <h5>Clase {{ currentClass + 1 }}:</h5>
      <iframe
        :src="currentVideo"
        title="YouTube video player"
        width="560"
        height="315"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        allowfullscreen
      ></iframe>
    </div>
    <div class="center-align" v-if="claseActual < 1">
      <button
        class="waves-effect waves-light center-align btn-large blue"
        @click="loadNextClass"
      >
        Siguiente clase<i class="material-icons right">arrow_forward</i>
      </button>
    </div>
    <div class="center-align">
      <router-link to="/quiz" v-if="claseActual === 1">
        <a class="waves-effect waves-light btn-large blue">
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
      videos: [
        "https://www.youtube.com/embed/ycWu_zxgOXM?si=yJHAI2yj7LKSdSH3",
        "https://www.youtube.com/embed/Igr6jQJEoNs?si=CJlaz9ah0ry-KmMM",
      ],
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
