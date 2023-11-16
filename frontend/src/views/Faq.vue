<template>
  <div class="FAQ">
    <h1></h1>
    <FAQs />
  </div>
</template>

<script>
// @ is an alias to /src
import FAQs from "@/components/Faqs.vue";

export default {
  name: "FAQ",
  components: {
    FAQs,
  },
};
</script>
