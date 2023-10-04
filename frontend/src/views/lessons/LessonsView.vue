<script>
import {getLessons} from "@/services/Lessons";
import {getUser} from "@/services/Auth";

export default{
  name: "LessonsView",
  data(){
    return {
      lessons: null
    }
  },

  mounted() {
    let user = getUser();
    if (!user){
      window.location = this.$router.resolve({name: "login"}).fullPath;
    }
    getLessons()
        .then((response) => {
            this.lessons = response.data;
        })

  }

}
</script>

<template>
<div v-if="lessons">
  <p>{{ lessons }}</p>
</div>
</template>

<style scoped>

</style>
