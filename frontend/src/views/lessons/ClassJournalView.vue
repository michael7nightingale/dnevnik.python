<script>
import {getUser, isTeacher} from "@/services/Auth";
import {createMark, getTeachingClass, updateMark} from "@/services/Lessons";
import {fullUserName, groupId} from "@/services/Data";


export default{
  name: "ClassJournalView",
  data(){
    return {
      studyGroupSubject: null,
      lessons: null,
      marks: null,
      pupilsFirst: null,
      pupils: null,
      user: null,

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
    this.user = user;
    const classId = this.$route.params.classId;
    getTeachingClass(classId)
        .then((response) => {
          let studyGroupSubject = response.data;
          this.studyGroupSubject = studyGroupSubject;
          if (studyGroupSubject.teacher_id !== user.id){
            window.location = this.$router.resolve({name: "permissions-error"}).fullPath;
          }
          this.lessons = groupId( studyGroupSubject.lessons);
          let pupils = groupId(studyGroupSubject.pupils);
          this.marks = groupId(studyGroupSubject.marks);

          for (const pupildId in pupils){
            pupils[pupildId].marks = {};
            for (const markId in this.marks){
              for (const lessonId in this.lessons){
                if (this.marks[markId].pupil_id === pupildId){
                    pupils[pupildId].marks[lessonId] = this.marks[markId];
                }
              }
            }
          }

          this.pupils = pupils;
          this.pupilsFirst = JSON.parse(JSON.stringify(this.pupils));

        })
        .then(() => {
           document.getElementById("loader").className = document.getElementById("loader").className.replace("show", "hide")
           document.getElementById("main").className = document.getElementById("main").className.replace("hide", "show")
        });

  },

  methods: {
    fullUserName,
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
       id;
       window.location = this.$router.resolve({name: "homepage"}).fullPath;
    },
    showDate(dateString){
      let date = new Date(Date.parse(dateString));
      let day = date.getDay().toString();
      if (day.length < 2) day = "0" + day;
      let month = date.getMonth().toString();
      if (month.length < 2) month = "0" + month;
      return `${day}.${month}`;
    },
    countAverage(marks){
      let sum = 0;
      let count = 0;
      for (const lessonId in marks){
        sum += marks[lessonId].mark;
        count += 1;
      }
      if (sum === 0) return "-"
      let result = (sum / count)
      return result ? result : "-";
    },
    markOnInput(pupilId, lessonId, event){
      let value = event.currentTarget.value;
      const abc = new Set(["2", "3", "4", "5", "Н", "У", "Б", ""])
      if (abc.has(value.toUpperCase())){
        let proxyPupils = this.pupils;
        if (proxyPupils[pupilId].marks[lessonId]){
          proxyPupils[pupilId].marks[lessonId].mark = value;
        }
        else{
          proxyPupils[pupilId].marks[lessonId] = {id: 0, mark: value};
        }
        if (this.pupilsFirst[pupilId].marks[lessonId]){
          if (parseInt(value) === this.pupilsFirst[pupilId].marks[lessonId].mark){
          event.currentTarget.style.backgroundColor = "white"
          }
          else{
            event.currentTarget.style.backgroundColor = "#caced0"
          }
        }
        else{
          event.currentTarget.style.backgroundColor = "#caced0"
        }
        this.pupils = proxyPupils;
        return
      }
      event.currentTarget.value = this.pupils[pupilId].marks[lessonId].mark

    },
    markEnterClick(pupilId, lessonId, event){
      if (event.keyCode === 13){
        event.currentTarget.style.backgroundColor = "white";
        let markId = this.pupils[pupilId].marks[lessonId].id;
        if (markId === 0){
           createMark(lessonId, pupilId, this.pupils[pupilId].marks[lessonId].mark)
        }
        else{
          updateMark(this.pupils[pupilId].marks[lessonId].id, this.pupils[pupilId].marks[lessonId].mark)
        }
      }
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
    <div v-if="pupils ">
    <section class="w-100 p-4 justify-content-center">
    <table class="table">
      <thead>
          <tr>
            <th>Ученик</th>
            <th v-for="(lessonData, lessonId) in lessons" :key="lessonId">
              {{ showDate(lessonData.date) }}
            </th>
            <th>Средний балл</th>
          </tr>
      </thead>
      <tbody>
        <tr v-for="(pupilData, pupilId) in pupils" :key="pupilId">
          <td>{{ fullUserName(pupilData.user) }}</td>
          <td v-for="(lessonData, lessonId) in lessons" :key="lessonId" :data-bs-target="lessonData">
             <div v-if="pupilData.marks[lessonId]">
               <input
                   class="form-control cells-input"
                   :value="pupilData.marks[lessonId].mark"
                   :id="`${pupilId}-${lessonId}`"
                   @input="markOnInput(pupilId, lessonId, $event)"
                   @keydown="markEnterClick(pupilId, lessonId, $event)"
               />
             </div>
            <div v-else>
              <input
                   class="form-control cells-input"
                   value=""
                   :id="`${pupilId}-${lessonId}`"
                   @input="markOnInput(pupilId, lessonId, $event)"
                   @keydown="markEnterClick(pupilId, lessonId, $event)"
               />
            </div>
          </td>
          <td> {{ countAverage(pupilData.marks) }} </td>
        </tr>
      </tbody>
    </table>

    </section>
    </div>
  </div>

</template>

<style scoped>
@import "../../assets/css/lessons.css";
</style>
