import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '@/views/main/HomeView.vue';
import LoginView from "@/views/users/LoginView.vue";
import CabinetView from "@/views/users/CabinetView.vue";
import LessonsView from "@/views/lessons/LessonsView.vue";
import MarksView from "@/views/lessons/MarksView.vue";
import MyClassView from "@/views/classes/MyClassView.vue";


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
    path: "/my-lessons",
    name: "my-lessons",
    component: LessonsView
  },
  {
    path: "/my-marks",
    name: "my-marks",
    component: MarksView
  },
  {
    path: "/my-class",
    name: "my-class",
    component: MyClassView
  }


]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
