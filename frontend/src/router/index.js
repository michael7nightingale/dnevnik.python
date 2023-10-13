import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '@/views/main/HomeView.vue';
import LoginView from "@/views/users/LoginView.vue";
import CabinetView from "@/views/users/CabinetView.vue";
import LessonsView from "@/views/lessons/LessonsView.vue";
import MarksView from "@/views/lessons/MarksView.vue";
import MyClassView from "@/views/classes/MyClassView.vue";
import PermissionsView from "@/views/error/PermissionsView.vue";
import JournalView from "@/views/lessons/JournalView.vue";


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
    path: "/my-journal",
    name: "my-journal",
    component: JournalView
  },
  {
    path: "/my-class",
    name: "my-class",
    component: MyClassView
  },
  {
    path: "/error/permissions",
    name: "permissions-error",
    component: PermissionsView
  }


]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
