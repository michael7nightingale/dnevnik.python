<script>
import {getUser, isPupil, isTeacher, logoutUser} from "@/services/Auth";


export default {
  name: 'HeaderComponent',
  computed: {
    user(){
      return getUser()
    },

  },

  methods: {
    logoutOnClick(){
      logoutUser();
      window.location = this.$router.resolve({name: "homepage"}).fullPath;
    },
    isPupil, isTeacher,

  },

}
</script>


<template>
<nav class="navbar navbar-expand-sm navbar-toggleable-sm navbar-light bg-white border-bottom box-shadow mb-3">
        <div class="container-fluid">
            <router-link class="navbar-brand" :to="{name: 'homepage'}">
              <svg height="32" aria-hidden="true" viewBox="0 0 16 16" version="1.1" width="32" data-view-component="true" class="octicon octicon-mark-github v-align-middle color-fg-default">
                <path d="M8 0c4.42 0 8 3.58 8 8a8.013 8.013 0 0 1-5.45 7.59c-.4.08-.55-.17-.55-.38 0-.27.01-1.13.01-2.2 0-.75-.25-1.23-.54-1.48 1.78-.2 3.65-.88 3.65-3.95 0-.88-.31-1.59-.82-2.15.08-.2.36-1.02-.08-2.12 0 0-.67-.22-2.2.82-.64-.18-1.32-.27-2-.27-.68 0-1.36.09-2 .27-1.53-1.03-2.2-.82-2.2-.82-.44 1.1-.16 1.92-.08 2.12-.51.56-.82 1.28-.82 2.15 0 3.06 1.86 3.75 3.64 3.95-.23.2-.44.55-.51 1.07-.46.21-1.61.55-2.33-.66-.15-.24-.6-.83-1.23-.82-.67.01-.27.38.01.53.34.19.73.9.82 1.13.16.45.68 1.31 2.69.94 0 .67.01 1.3.01 1.49 0 .21-.15.45-.55.38A7.995 7.995 0 0 1 0 8c0-4.42 3.58-8 8-8Z"></path>
            </svg>
            </router-link>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target=".navbar-collapse" aria-controls="navbarSupportedContent"
                    aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="navbar-collapse collapse d-sm-inline-flex justify-content-between">
                <ul class="navbar-nav flex-grow-1">
                    <li class="nav-item">
                        <router-link class="nav-link text-dark" :to="{name: 'homepage'}">Дневник</router-link>
                    </li>
                </ul>
               <div v-if="user">
                <ul v-if="isPupil(user.user)" class="navbar-nav">
                  <li>
                    <router-link class="nav-link" :to="{name: 'my-marks'}">Оценки</router-link>
                  </li>
                  <li>
                    <router-link class="nav-link" :to="{name: 'my-lessons'}">Уроки</router-link>
                  </li>
                  <li>
                    <router-link class="nav-link" :to="{name: 'my-class'}">Класс</router-link>
                  </li>
                  <li>
                    <router-link class="nav-link" :to="{name: 'cabinet'}">Кабинет</router-link>
                  </li>
                  <li>
                    <a class="nav-link" @click="logoutOnClick">
                      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-box-arrow-left" viewBox="0 0 16 16">
                        <path fill-rule="evenodd" d="M6 12.5a.5.5 0 0 0 .5.5h8a.5.5 0 0 0 .5-.5v-9a.5.5 0 0 0-.5-.5h-8a.5.5 0 0 0-.5.5v2a.5.5 0 0 1-1 0v-2A1.5 1.5 0 0 1 6.5 2h8A1.5 1.5 0 0 1 16 3.5v9a1.5 1.5 0 0 1-1.5 1.5h-8A1.5 1.5 0 0 1 5 12.5v-2a.5.5 0 0 1 1 0v2z"/>
                        <path fill-rule="evenodd" d="M.146 8.354a.5.5 0 0 1 0-.708l3-3a.5.5 0 1 1 .708.708L1.707 7.5H10.5a.5.5 0 0 1 0 1H1.707l2.147 2.146a.5.5 0 0 1-.708.708l-3-3z"/>
                      </svg>
                    </a>
                  </li>
                </ul>

                <ul v-if="isTeacher(user.user)" class="navbar-nav">
                  <li>
                    <router-link class="nav-link" :to="{name: 'my-marks'}">Журнал</router-link>
                  </li>
                  <li>
                    <router-link class="nav-link" :to="{name: 'my-lessons'}">Уроки</router-link>
                  </li>
                  <li>
                    <router-link class="nav-link" :to="{name: 'my-class'}">Мой класс</router-link>
                  </li>
                  <li>
                    <router-link class="nav-link" :to="{name: 'cabinet'}">Кабинет</router-link>
                  </li>
                  <li>
                    <a class="nav-link" @click="logoutOnClick">
                      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-box-arrow-left" viewBox="0 0 16 16">
                        <path fill-rule="evenodd" d="M6 12.5a.5.5 0 0 0 .5.5h8a.5.5 0 0 0 .5-.5v-9a.5.5 0 0 0-.5-.5h-8a.5.5 0 0 0-.5.5v2a.5.5 0 0 1-1 0v-2A1.5 1.5 0 0 1 6.5 2h8A1.5 1.5 0 0 1 16 3.5v9a1.5 1.5 0 0 1-1.5 1.5h-8A1.5 1.5 0 0 1 5 12.5v-2a.5.5 0 0 1 1 0v2z"/>
                        <path fill-rule="evenodd" d="M.146 8.354a.5.5 0 0 1 0-.708l3-3a.5.5 0 1 1 .708.708L1.707 7.5H10.5a.5.5 0 0 1 0 1H1.707l2.147 2.146a.5.5 0 0 1-.708.708l-3-3z"/>
                      </svg>
                    </a>
                  </li>
                </ul>
              </div>
              <div v-else>
                <ul class="navbar-nav">
                  <li>
                    <router-link :to="{name: 'login'}" class="nav-link">Войти</router-link>
                  </li>
                </ul>
              </div>
            </div>
        </div>
    </nav>

</template>


<style scoped>

</style>