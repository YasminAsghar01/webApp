import { createApp } from "vue";
import "./style.css";
import App from "./App.vue";
import Home from "./components/Home.vue";
import About from "./components/About.vue";
import Profile from "./components/Profile.vue";
import AddItem from "./components/AddItem.vue";
import GetItem from "./components/GetItem.vue";
import Product from "./components/Product.vue";
import UpdateProfile from "./components/UpdateProfile.vue"
import { createWebHistory, createRouter } from "vue-router";
import '../node_modules/bootstrap/dist/css/bootstrap.css';
import '../node_modules/bootstrap-vue/dist/bootstrap-vue.css';
import BootstrapVue3 from 'bootstrap-vue-3';
import 'bootstrap/dist/css/bootstrap.css'


const routes = [
  { path: "/", component: Home },
  { path: "/profile", component: Profile },
  { path: "/items/add", component: AddItem },
  { path: "/items/", component: GetItem },
  { path: "/profile/", component: UpdateProfile},
  { name: "test" , path: "/item/:id/:user", component: Product, props:true},
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

createApp(App).use(router,BootstrapVue3).mount("#app");
