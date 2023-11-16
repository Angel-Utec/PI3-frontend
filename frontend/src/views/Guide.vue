<template>
  <div class="Guide">
    <h1></h1>
    <Guides />
  </div>
</template>

<script>
// @ is an alias to /src
import Guides from "@/components/Guides.vue";

export default {
  name: "Guide",
  components: {
    Guides,
  },
};
</script>
