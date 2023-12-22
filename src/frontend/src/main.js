import { createApp } from "vue";
import ElementPlus from "element-plus";
import App from "./App.vue";
import router from "./router"

// 引入 Element Plus 默认样式文件
import 'element-plus/dist/index.css'
import "./style.css";

const app = createApp(App);
app.use(ElementPlus);
app.use(router)
app.mount("#app");