<script>
import {getUser, isPupilOrTeacher} from "@/services/Auth";
import {getMySchool} from "@/services/Schools";
import {getMyClass} from "@/services/Classes";

export default {
  name: "CabinetView",
  data(){
    return {
      user: null,
      school: null,
      type_: null,
      class_: null,

    }
  },

  computed: {
    fullUserName(){
      return `${this.user.last_name} ${this.user.first_name} ${this.user.father_name}`
    },
    fullSchoolName(){
      return this.school.name;
    },
    classLabel(){
      if (this.class_.class_){
          if (this.class_.subclass){
            return `${this.class_.class.label} класс (${this.class_.subclass.label})`
          }
          else {
            return `${this.class_.class.label} класс`
          }
      }
      return `${this.class_.subclass.label} класс`
    },

    userTypeSign(){
      let typeMatches = {
        pupil: "Ученик",
        teacher: "Учитель",
        administrator: "Администратор"
      }
      return typeMatches[this.user.type];
    }

  },

  mounted() {
    let user = getUser();
    if (!user){
      window.location = this.$router.resolve({name: "login"}).fullPath;
    }
    this.user = user.user;
    this.type_ = this.user["type"];
    getMySchool()
        .then((response) => {
          this.school = response.data;
        })
        .then(() => {
           if (isPupilOrTeacher(this.user)) {
             getMyClass()
                 .then((response) => {
                   this.class_ = response.data;
                 });
           }
        })
        .then(() => {
          document.getElementById("loader").className = document.getElementById("loader").className.replace("show", "hide")
          document.getElementById("main").className = document.getElementById("main").className.replace("hide", "show")
        })
  },

  methods: {
    isPupilOrTeacher,
    imageInputOnChange(event){
      const avatarFileUpload = document.getElementById('AvatarFileUpload')
      const imageViewer = avatarFileUpload.querySelector('.selected-image-holder>img')
      let reader = new FileReader();
      console.log(reader)
        reader.onload = function(){
            imageViewer.src = reader.result;
        };
        reader.readAsDataURL(event.target.files[0]);
    },
    imageInputOnClick(event){
      const avatarFileUpload = document.getElementById('AvatarFileUpload')
      const imageInput = avatarFileUpload.querySelector('input[name="avatar"]')
      event.preventDefault()
      imageInput.click()
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
    <div v-if="user && school">
  <section style="background-color: #eee;">
  <div class="container py-5">
    <div class="row">
      <div class="col-lg-4">
        <div class="card mb-4">
          <div class="card-body text-center">
            <div class="card-body rounded-0">
                    <div id="AvatarFileUpload">
                        <div class="selected-image-holder">
                            <img :src="user.avatar ? user.avatar : `default-avatar.png`" alt="AvatarInput">
                        </div>
                        <div class="avatar-selector">
                            <a href="#" class="avatar-selector-btn">
                                <img :src="`camera.svg`" alt="cam" @click="imageInputOnClick($event)">
                            </a>
                            <input
                                @change="imageInputOnChange($event)"
                                type="file" accept="images/jpg, images/png" name="avatar"
                            >
                        </div>
                    </div>
            </div>
            <h5 class="my-3">{{ fullUserName }}</h5>
            <p class="text-muted mb-1">{{ userTypeSign }}</p>
            <p class="text-muted mb-4">{{ fullSchoolName }}</p>
            <div class="d-flex justify-content-center mb-2">
              <button type="button" class="btn btn-primary">Подписаться</button>
              <button type="button" class="btn btn-outline-primary ms-1">Сообщение</button>
            </div>
          </div>
        </div>
         <div class="d-flex justify-content-center mb-2">
           <button type="button" class="btn btn-outline-primary ms-1">Сохранить изменения</button>
         </div>
      </div>
      <div class="col-lg-8">
        <div class="card mb-4">
          <div class="card-body">
            <div class="row">
              <div class="col-sm-3">
                <p class="mb-0">Ф.И.О.</p>
              </div>
              <div class="col-sm-9">
                <p class="text-muted mb-0">{{ fullUserName }}</p>
              </div>
            </div>
            <hr>
            <div class="row">
              <div class="col-sm-3">
                <p class="mb-0">Имя пользователя</p>
              </div>
              <div class="col-sm-9">
                <input class="text-muted mb-0" :value="user.username"/>
              </div>
            </div>
             <hr>
            <div class="row">
              <div class="col-sm-3">
                <p class="mb-0">Почта</p>
              </div>
              <div class="col-sm-9">
                <p class="text-muted mb-0">{{ this.user.email }}</p>
              </div>
            </div>
            <hr>
            <div v-if="isPupilOrTeacher(user) && class_">
              <div class="row">
                <div class="col-sm-3">
                  <p class="mb-0">Класс</p>
                </div>
                <div class="col-sm-9">
                  <p class="text-muted mb-0">{{ classLabel }}</p>
                </div>
              </div>
              <hr>
            </div>
            <div class="row">
              <div class="col-sm-3">
                <p class="mb-0">Школа</p>
              </div>
              <div class="col-sm-9">
                <p class="text-muted mb-0">{{ fullSchoolName }}</p>
              </div>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col-md-6">
            <div class="card mb-4 mb-md-0">
              <div class="card-body">
                <p class="mb-4"><span class="text-primary font-italic me-1">assigment</span> Project Status
                </p>
                <p class="mb-1" style="font-size: .77rem;">Web Design</p>
                <div class="progress rounded" style="height: 5px;">
                  <div class="progress-bar" role="progressbar" style="width: 80%" aria-valuenow="80"
                    aria-valuemin="0" aria-valuemax="100"></div>
                </div>
                <p class="mt-4 mb-1" style="font-size: .77rem;">Website Markup</p>
                <div class="progress rounded" style="height: 5px;">
                  <div class="progress-bar" role="progressbar" style="width: 72%" aria-valuenow="72"
                    aria-valuemin="0" aria-valuemax="100"></div>
                </div>
                <p class="mt-4 mb-1" style="font-size: .77rem;">One Page</p>
                <div class="progress rounded" style="height: 5px;">
                  <div class="progress-bar" role="progressbar" style="width: 89%" aria-valuenow="89"
                    aria-valuemin="0" aria-valuemax="100"></div>
                </div>
                <p class="mt-4 mb-1" style="font-size: .77rem;">Mobile Template</p>
                <div class="progress rounded" style="height: 5px;">
                  <div class="progress-bar" role="progressbar" style="width: 55%" aria-valuenow="55"
                    aria-valuemin="0" aria-valuemax="100"></div>
                </div>
                <p class="mt-4 mb-1" style="font-size: .77rem;">Backend API</p>
                <div class="progress rounded mb-2" style="height: 5px;">
                  <div class="progress-bar" role="progressbar" style="width: 66%" aria-valuenow="66"
                    aria-valuemin="0" aria-valuemax="100"></div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-md-6">
            <div class="card mb-4 mb-md-0">
              <div class="card-body">
                <p class="mb-4"><span class="text-primary font-italic me-1">assigment</span> Project Status
                </p>
                <p class="mb-1" style="font-size: .77rem;">Web Design</p>
                <div class="progress rounded" style="height: 5px;">
                  <div class="progress-bar" role="progressbar" style="width: 80%" aria-valuenow="80"
                    aria-valuemin="0" aria-valuemax="100"></div>
                </div>
                <p class="mt-4 mb-1" style="font-size: .77rem;">Website Markup</p>
                <div class="progress rounded" style="height: 5px;">
                  <div class="progress-bar" role="progressbar" style="width: 72%" aria-valuenow="72"
                    aria-valuemin="0" aria-valuemax="100"></div>
                </div>
                <p class="mt-4 mb-1" style="font-size: .77rem;">One Page</p>
                <div class="progress rounded" style="height: 5px;">
                  <div class="progress-bar" role="progressbar" style="width: 89%" aria-valuenow="89"
                    aria-valuemin="0" aria-valuemax="100"></div>
                </div>
                <p class="mt-4 mb-1" style="font-size: .77rem;">Mobile Template</p>
                <div class="progress rounded" style="height: 5px;">
                  <div class="progress-bar" role="progressbar" style="width: 55%" aria-valuenow="55"
                    aria-valuemin="0" aria-valuemax="100"></div>
                </div>
                <p class="mt-4 mb-1" style="font-size: .77rem;">Backend API</p>
                <div class="progress rounded mb-2" style="height: 5px;">
                  <div class="progress-bar" role="progressbar" style="width: 66%" aria-valuenow="66"
                    aria-valuemin="0" aria-valuemax="100"></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
  </div>
  </div>

</template>


<style scoped>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@200&family=Space+Mono&display=swap" rel="stylesheet');
:root{
    --space-mono-font: 'Space Mono', monospace;
    --border-dark-subtle: #373838;
}
*{
    box-sizing: border-box;
}
body *{
    font-family: var(--space-mono-font);
}
/**
Page Design
*/
body,
html{
    height: 100%;
    width: 100%;
    margin: 0;
    padding: 0;
}
body{
    background-color: #282A3A;
}
.page-title{
    font-size: 2.5rem;
    font-weight: 500;
    color: #fff;
    letter-spacing: 3px;
    font-family: var(--secular-font);
    text-align: center;
    text-shadow: 0px 0px 3px #2020208c;
}
.border-dark-subtle{
    border-color: var(--border-dark-subtle) !important;
}
/* Avatar File Input Wrapper */
div#AvatarFileUpload {
    position: relative;
    width: 150px;
    height: 150px;
    background: #f9f9f9;
    border: 3px solid #bbb;
    border-radius: 50% 50%;
    margin: auto;
}
/* Image Preview Wrapper and Container */
div#AvatarFileUpload > .selected-image-holder{
    width: 100%;
    height: 100%;
    border-radius: 50% 50%;

}
div#AvatarFileUpload > .selected-image-holder{
    width: 100%;
    overflow: hidden;
}
div#AvatarFileUpload > .selected-image-holder>img{
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-fit: center center;
}

/* Image Selector to Browse Image to Upload */
div#AvatarFileUpload > .avatar-selector{
    position: absolute;
    bottom: 8px;
    right: 19%;
    width: 20px;
    height: 20px;
}
div#AvatarFileUpload > .avatar-selector input[type="file"]{
    display: none;
}
div#AvatarFileUpload > .avatar-selector > .avatar-selector-btn{
    width: 100%;
    height: 100%;
    background: #f5f5f59e;
    padding: 5px 7px;
    border-radius: 50% 50%;
}
div#AvatarFileUpload > .avatar-selector > .avatar-selector-btn>img{
    width: 100%;
    height: 100%;
    object-fit: scale-down;
    object-position: center center;
    z-index: 2;
}
</style>
