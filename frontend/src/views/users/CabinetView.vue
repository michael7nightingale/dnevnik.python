<script>
import {getUser} from "@/services/Auth";

export default {
  name: "CabinetView",
  data(){
    return {
      user: null,
      school: null,
      type_: null

    }
  },

  mounted() {
    let user = getUser();
    if (!user){
      window.location = this.$router.resolve({name: "login"}).fullPath;
    }
    this.user = user.user;
    this.type_ = this.user["type"]

  }

}
</script>

<template>
  <div v-if="user">
    <p>{{ user.first_name }}</p>
  </div>
</template>

<style scoped>

</style>