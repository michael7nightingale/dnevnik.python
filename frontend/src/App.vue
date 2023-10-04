<script>
import {getUser, logoutUser} from "@/services/Auth";


export default {
  name: 'App',

  methods: {
    logoutOnClick(){
      logoutUser();
      window.location = this.$router.resolve({name: "homepage"}).fullPath;
    }
  },


  computed: {
    user(){
      console.log(22, getUser())
      return getUser()
    },

  }


}
</script>


<template>
    <nav class="navbar navbar-expand-sm navbar-toggleable-sm navbar-light bg-white border-bottom box-shadow mb-3">
        <div class="container-fluid">
            <router-link class="navbar-brand" :to="{name: 'homepage'}">FFF</router-link>
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
              <ul v-if="user" class="navbar-nav">
                <li>
                  <router-link class="nav-link" :to="{name: 'cabinet'}">Кабинет</router-link>
                </li>
                <li>
                  <router-link class="nav-link" :to="{name: 'lessons'}">Уроки</router-link>
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
              <ul v-else class="navbar-nav">
                <li>
                  <router-link :to="{name: 'login'}" class="nav-link">Войти</router-link>
                </li>
              </ul>
            </div>
        </div>
    </nav>
  <div class="container">
    <router-view/>
  </div>
</template>

<style>
</style>
