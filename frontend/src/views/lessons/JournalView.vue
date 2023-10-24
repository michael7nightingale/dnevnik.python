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

  methods: {
    getClassLabel(class_){
      if (class_.class_){
          if (class_.subclass){
            return `${class_.class_.label} класс (${class_.subclass.label})`
          }
          else {
            return `${class_.class_.label} класс`
          }
      }
      return `${class_.subclass.label} класс`
    },
    goToStudyGroupSubjectView(studyGroupSubject){
       let id = studyGroupSubject.id;
       id
       window.location = this.$router.resolve({
         name: "my-journal-detail",
         params: {classId: studyGroupSubject.id}
       }).fullPath;
    }

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
          <h2 class="accordion-header" :id="`${subjectName}-header`">
            <button class="accordion-button" type="button" data-bs-toggle="collapse" :data-bs-target="`#${subjectName}-collapse`" aria-expanded="true" :aria-controls="`${subjectName}-collapse`">
              {{ subjectName }}
            </button>
          </h2>
          <div :id="`${subjectName}-collapse`" class="accordion-collapse collapse show" :aria-labelledby="`${subjectName}-header`">
            <div class="accordion-body">
              <div
                  class="col-4 study-group-subject-card"
                  v-for="studyGroupSubject of data"
                  :key="studyGroupSubject"
                  @clic="goToStudyGroupSubjectView(studyGroupSubject)"
              >
                 <a @click="goToStudyGroupSubjectView(studyGroupSubject)">
                   <h5 class="text-center prevent-select" style="text-align: center">{{ getClassLabel(studyGroupSubject.study_group) }}</h5>
                 </a>
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
@import "../../assets/css/lessons.css";
</style>
