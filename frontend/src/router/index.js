import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: Home,
  },
  {
    path: "/login",
    name: "login",
    component: () =>
      import(/* webpackChunkName: "Category" */ "../components/Logins.vue"),
  },
  {
    path: "/quienes-somos",
    name: "quienes-somos",
    component: () =>
      import(/* webpackChunkName: "Category" */ "../components/Somos.vue"),
  },
  {
    path: "/FAQ",
    name: "FAQ",
    component: () =>
      import(/* webpackChunkName: "Category" */ "../components/Faqs.vue"),
  },
  {
    path: "/guide",
    name: "guide",
    component: () =>
      import(/* webpackChunkName: "Category" */ "../components/Guides.vue"),
  },
  {
    path: "/ayuda",
    name: "ayuda",
    component: () =>
      import(/* webpackChunkName: "Category" */ "../components/Ayudas.vue"),
  },
  {
    path: "/cursos",
    name: "cursos",
    component: () =>
      import(/* webpackChunkName: "Category" */ "../components/Cursos.vue"),
  },
  {
    path: "/curso-social",
    name: "historia",
    component: () =>
      import(
        /* webpackChunkName: "Category" */ "../components/Cursos-historia.vue"
      ),
  },
  {
    path: "/quiz",
    name: "Quiz1",
    component: () =>
      import(/* webpackChunkName: "Category" */ "../components/Quiz_1.vue"),
  },
  {
    path: "/register",
    name: "register",
    component: () =>
      import(/* webpackChunkName: "Category" */ "../components/Users.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
