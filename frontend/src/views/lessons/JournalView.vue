<script>
import {getUser, isTeacher} from "@/services/Auth";
import {getTeachingClasses} from "@/services/Lessons";


export default{
  name: "JournalView",
  data(){
    return {
      studyGroupSubjects: null,
    }
  },

  mounted() {
    let user = getUser();
    if (!user){
      window.location = this.$router.resolve({name: "login"}).fullPath;
    }
    if (!isTeacher(user.user)){
      window.location = this.$router.resolve({name: "permissions-error"}).fullPath
    }
    getTeachingClasses()
        .then((response) => {
          let studyGroupSubjects = response.data;
          let studyGroupSubjectsProxy = {};
          for (const studyGroupSubject of studyGroupSubjects){
            if (studyGroupSubjectsProxy[studyGroupSubject.subject.name]){
              studyGroupSubjectsProxy[studyGroupSubject.subject.name].push(studyGroupSubject);
            }
            else{
              studyGroupSubjectsProxy[studyGroupSubject.subject.name] = [studyGroupSubject];
            }
          }
          this.studyGroupSubjects = studyGroupSubjectsProxy;
          console.log(this.studyGroupSubjects)
        })
        .then(() => {
           document.getElementById("loader").className = document.getElementById("loader").className.replace("show", "hide")
           document.getElementById("main").className = document.getElementById("main").className.replace("hide", "show")
        });

  },

}
</script>

<template>
  <div class="centered show" id="loader">
    <h4 style="">Загрузка...</h4>
    <span class="loader"></span>
  </div>
  <div id="main" class="hide">
    <div v-if="studyGroupSubjects">
      <div class="accordion" id="accordionPanelsStayOpenExample">
        <div class="accordion-item" v-for="(data, subjectName) in studyGroupSubjects" :key="data">
          <h2 class="accordion-header" :id="`panelsStayOpen-${subjectName}`">
            <button class="accordion-button" type="button" data-bs-toggle="collapse" :data-bs-target="`#panelsStayOpen-c${subjectName}`" aria-expanded="true" :aria-controls="`panelsStayOpen-c${subjectName}`">
             {{ subjectName }}
            </button>
          </h2>
          <div :id="`panelsStayOpen-c${subjectName}`" class="accordion-collapse collapse show" :aria-labelledby="`panelsStayOpen-${subjectName}`">
            <div class="accordion-body">
              <div class="row">
                <div class="col-lg-3" v-for="studySubjectGroup of data" :key="studySubjectGroup">
                  {{ studySubjectGroup }}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div v-else>
      <h3 style="text-align: center">Вы не ведёте уроки у классов.</h3>
    </div>
  </div>

</template>

<style scoped>

</style>
