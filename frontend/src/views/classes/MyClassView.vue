<script>
import {getUser, isPupilOrTeacher} from "@/services/Auth";
import {getMySchool} from "@/services/Schools";
import {getMyClass} from "@/services/Classes";

export default {
  name: "MyClassView",
  data(){
    return {
      pupils: null,
      class_: null,
      user: null
    }
  },
  methods: {
    fullUserName(user) {
      return `${user.last_name} ${user.first_name} ${user.father_name}`
    },
  },
  computed: {
    classLabel(){
      if (this.class_.class_){
          if (this.class_.subclass){
            return `${this.class_.class_.label} класс (${this.class_.subclass.label})`
          }
          else {
            return `${this.class_.class_.label} класс`
          }
      }
      return `${this.class_.subclass.label} класс`
    },

  },

  mounted() {
    let user = getUser();
    if (!user){
      window.location = this.$router.resolve({name: "login"}).fullPath;
    }
    if (!isPupilOrTeacher(user.user)){
      window.location = this.$router.resolve({name: "permissions-error"}).fullPath
    }
    this.user = user.user;
    this.type_ = this.user["type"];
    getMySchool()
        .then((response) => {
          this.school = response.data;

        })
        .then(() => {
          getMyClass()
            .then((response) => {
              this.class_ = response.data;
              this.pupils = response.data.pupils;
            });
        })
        .then(() => {
           document.getElementById("loader").className = document.getElementById("loader").className.replace("show", "hide")
           document.getElementById("main").className = document.getElementById("main").className.replace("hide", "show")
        });
  }
}
</script>

<template>
<div class="centered show" id="loader">
    <h4 style="">Загрузка...</h4>
    <span class="loader"></span>
  </div>
  <div id="main" class="hide">
    <div v-if="user && pupils && class_">
      <h2 class="text-center">{{ classLabel }}</h2>
      <div class="card mb-4">
        <div class="card-body">
          <div class="row">
            <div class="col-sm-3">
              <p class="mb-0">Классный Руководитель</p>
            </div>
            <div class="col-sm-9">
              <p class="text-muted mb-0">{{ fullUserName(this.class_.main_teacher.user) }}</p>
            </div>
          </div>
          <hr>
          <div class="row">
            <div class="col-sm-3">
              <p class="mb-0">Кол-во учеников</p>
            </div>
            <div class="col-sm-9">
              <p class="text-muted mb-0">{{ pupils.length }}</p>
            </div>
          </div>
        </div>
      </div>
      <h4 class="text-center">Ученики</h4>
      <section style="background-color: #eee; padding: 20px">
        <ol>
          <li v-for="pupil in pupils" :key="pupil">
              {{ fullUserName(pupil.user) }}
            <hr>
          </li>
        </ol>
      </section>
    </div>
  </div>
</template>

<style scoped>

</style>
