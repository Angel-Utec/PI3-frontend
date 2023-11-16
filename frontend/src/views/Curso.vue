<template>
  <div class="Curso">
    <h1></h1>
    <Cursos />
  </div>
</template>

<script>
// @ is an alias to /src
import Cursos from "@/components/Cursos.vue";

export default {
  name: "Curso",
  components: {
    Cursos,
  },
};
</script>
