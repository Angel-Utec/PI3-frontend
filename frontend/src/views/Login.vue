<template>
  <div>
    <h1></h1>
    <Login />
  </div>
</template>

<script>
// @ is an alias to /src
import Login from "@/components/Logins.vue";

export default {
  name: "login",
  components: {
    Login,
  },
};
</script>
