<script>
import {loginUser} from "@/services/UserService";
import {setUser} from "@/services/Auth";

export default {
  name: "LogiView",
  data(){
    return {
      login: null,
      password: null,
      error: null,

    }
  },

  methods: {
    loginOnInput(value){
      this.login = value;
    },
    passwordOnInput(value){
      this.password = value;
    },

    onSubmit(){
      let data = {
        login: this.login,
        password: this.password
      }
      console.log(123)
      console.log(2222222, localStorage.userData)
      loginUser(data)
          .then((response) => {
              setUser(response.data['access-token'])
              window.location = this.$router.resolve({name: "homepage"}).fullPath;
          })
          .catch((error) => {
              this.error = error.response.data.detail;
          });
    }

  }

}
</script>

<template>
<form style="max-width: 320px; margin: auto">
  <!-- Email input -->
  <h3 style="text-align: center; margin: 14px">Вход в систему</h3>
  <div class="form-outline mb-4">
    <label class="form-label" for="form2Example1">Имя пользователя или почта</label>
    <input type="text" id="form2Example1" class="form-control" :value="login" @input="loginOnInput($event.currentTarget.value)"/>
  </div>

  <!-- Password input -->
  <div class="form-outline mb-4">
    <label class="form-label" for="form2Example2">Пароль</label>
    <input type="password" id="form2Example2" class="form-control" :value="password" @input="passwordOnInput($event.currentTarget.value)"/>
  </div>

  <!-- 2 column grid layout for inline styling -->
  <div class="row mb-4">
    <div class="col d-flex justify-content-center">
      <!-- Checkbox -->
      <div class="form-check">
        <input class="form-check-input" type="checkbox" value="" id="form2Example31" checked />
        <label class="form-check-label" for="form2Example31"> Запомнить меня </label>
      </div>
    </div>

    <div class="col">
      <!-- Simple link -->
      <a href="#!">Забыли пороль?</a>
    </div>
  </div>

  <p class="text-danger" style="margin: 10px">{{ error }}</p>
  <!-- Submit button -->
  <button type="button" class="btn btn-primary btn-block mb-4" @click="onSubmit">Войти</button>

  <!-- Register buttons -->
  <div class="text-center">
    <p>Не зарегистрированы? <a href="#!">Оситавить заявку</a></p>
    <p>войти с помощью:</p>
    <button type="button" class="btn btn-link btn-floating mx-1">
      <i class="fab fa-facebook-f"></i>
    </button>

    <button type="button" class="btn btn-link btn-floating mx-1">
      <i class="fab fa-google"></i>
    </button>

    <button type="button" class="btn btn-link btn-floating mx-1">
      <i class="fab fa-twitter"></i>
    </button>

    <button type="button" class="btn btn-link btn-floating mx-1">
      <i class="fab fa-github"></i>
    </button>
  </div>
</form>

</template>

<style scoped>

</style>