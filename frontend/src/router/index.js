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
    path: "/curso-social",
    name: "historia",
    component: () =>
      import(
        /* webpackChunkName: "Category" */ "../components/Cursos-historia.vue"
      ),
  },
  {
    path: "/curso-matematicas",
    name: "matematicas",
    component: () =>
      import(
        /* webpackChunkName: "Category" */ "../components/Cursos-matematicas.vue"
      ),
  },
  {
    path: "/curso-ciencia",
    name: "ciencia",
    component: () =>
      import(
        /* webpackChunkName: "Category" */ "../components/Cursos-ciencias.vue"
      ),
  },
  {
    path: "/curso-trabajo",
    name: "trabajo",
    component: () =>
      import(
        /* webpackChunkName: "Category" */ "../components/Cursos-trabajo.vue"
      ),
  },
  {
    path: "/curso-comunicacion",
    name: "comunicacion",
    component: () =>
      import(
        /* webpackChunkName: "Category" */ "../components/Cursos-comunicacion.vue"
      ),
  },
  {
    path: "/quiz-historia",
    name: "quiz_historia",
    component: () =>
      import(
        /* webpackChunkName: "Category" */ "../components/Quiz_historia.vue"
      ),
  },
  {
    path: "/quiz-matematicas",
    name: "Quiz_historia",
    component: () =>
      import(
        /* webpackChunkName: "Category" */ "../components/Quiz_matematicas.vue"
      ),
  },
  {
    path: "/quiz-ciencias",
    name: "Quiz_ciencias",
    component: () =>
      import(
        /* webpackChunkName: "Category" */ "../components/Quiz_ciencias.vue"
      ),
  },
  {
    path: "/quiz-comunicacion",
    name: "Quiz_comunicacion",
    component: () =>
      import(
        /* webpackChunkName: "Category" */ "../components/Quiz_comunicacion.vue"
      ),
  },
  {
    path: "/quiz-trabajo",
    name: "Quiz_trabajo",
    component: () =>
      import(
        /* webpackChunkName: "Category" */ "../components/Quiz_trabajo.vue"
      ),
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
