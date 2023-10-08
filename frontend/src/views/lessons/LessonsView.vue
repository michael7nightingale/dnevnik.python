<script>
import {getLessons} from "@/services/Lessons";
import {getUser} from "@/services/Auth";

export default{
  name: "LessonsView",
  data(){
    return {
      lessons: null,
      schedule: {},

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
        .then(() => {
          let scheduleProxy = {};
          let options = {
            month: "long",
            day: "numeric",

          }
          let daysOfWeek = ["Воскресенье", 'Понедельник', "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]
          for (let lesson of this.lessons){
            let date = new Date(Date.parse(lesson.date))
            let dayOfWeekIndex = date.getDay();
            date = `${daysOfWeek[dayOfWeekIndex]}, ` + date.toLocaleString("ru", options);
            if (scheduleProxy[date]){
              scheduleProxy[date].push(lesson);
            }
            else{
              scheduleProxy[date] = [lesson];
            }
          }
          this.schedule = scheduleProxy;
        });

  },

  methods: {
    parseTime(timeString){
      timeString = timeString.split(".")[0]
      let datetime = new Date("1970-01-01T" + timeString);
      return `${datetime.getHours()}:${datetime.getMinutes()}`
    },
    parseHomework(homework){
      if (!homework) return "Ничего не задано";
      let limit = 50;
      if (homework.length > limit){
        return homework.slice(0, limit - 3) + "...";
      }
      return homework;
    }
  }

}
</script>

<template>
<div v-if="schedule && lessons">
  <div v-for="(data, dayOfWeek) in schedule" :key="data">
    <h2>{{dayOfWeek}}</h2>
    <div class="row">
      <div class="col-3 lesson-list-container-detail" v-for="lesson of data" :key="lesson">
        <h4>{{ lesson.study_group_subject.subject.name }}</h4>
        <h5>Тема: {{ lesson.theme }}</h5>
        <p>{{ parseTime(lesson.start_at)}} - {{ parseTime(lesson.finish_at) }}</p>
        <p v-if="lesson.homework">Домашнее задание: {{ parseHomework(lesson.homework) }}</p>
        <p v-else>Ничего не задано</p>
      </div>
    </div>
    <hr>
  </div>
</div>
</template>

<style>
@import "../../assets/css/lessons.css";
</style>
