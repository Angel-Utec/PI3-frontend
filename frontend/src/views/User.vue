<template>
  <div>
    <h1></h1>
    <Users />
  </div>
</template>

<script>
// @ is an alias to /src
import Users from "@/components/Users.vue";

export default {
  name: "User",
  components: {
    Users,
  },
};
</script>
