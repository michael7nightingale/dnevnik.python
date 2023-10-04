<script>
import {getMarks} from "@/services/Marks";
import {getUser} from "@/services/Auth";

export default{
  name: "MarksView",
  data(){
    return {
      marks: null
    }
  },

  mounted() {
    let user = getUser();
    if (!user){
      window.location = this.$router.resolve({name: "login"}).fullPath;
    }
    getMarks()
        .then((response) => {
            this.lessons = response.data;
        })

  }

}
</script>

<template>
<div v-if="marks">
  <p>{{ marks }}</p>
</div>
</template>

<style scoped>

</style>
