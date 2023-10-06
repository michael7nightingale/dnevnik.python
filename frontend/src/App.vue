<script>
import Header from "@/components/Header.vue";


export default {
  name: 'App',
  components: {
    Header
  },

}
</script>


<template>
  <Header/>
  <div class="container">
    <router-view/>
  </div>
</template>


<style>
@import "assets/css/main.css";
@import "assets/css/loader.css";
</style>
