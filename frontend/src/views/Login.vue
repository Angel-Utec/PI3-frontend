<template>
  <div class="Login">
    <h1></h1>
    <Logins />
  </div>
</template>

<script>
// @ is an alias to /src
import Logins from "@/components/Logins.vue";

export default {
  name: "Login",
  components: {
    Logins,
  },
};
</script>
