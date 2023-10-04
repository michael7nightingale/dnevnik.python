import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '@/views/main/HomeView.vue';
import LoginView from "@/views/users/LoginView.vue";
import CabinetView from "@/views/users/CabinetView.vue";
import LessonsView from "@/views/lessons/LessonsView.vue";


const routes = [
  {
    path: '/',
    name: 'homepage',
    component: HomeView
  },
  {
    path: "/auth/login",
    name: "login",
    component: LoginView
  },
  {
    path: "/cabinet",
    name: "cabinet",
    component: CabinetView
  },
  {
    path: "/lessons",
    name: "lessons",
    component: LessonsView
  }


]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
