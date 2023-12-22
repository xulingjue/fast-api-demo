<script>
import Menu from './components/Menu.vue'
import Sidebar from './components/Sidebar.vue'
export default {
  components: {Sidebar, Menu}
}

</script>

<template>
  <div id="app">
    <el-container>
      <el-header><Menu></Menu></el-header>
      <el-container>
        <el-aside width="200px">
          <Sidebar></Sidebar>
        </el-aside>

        <el-main>
          <router-view></router-view>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>


<style scoped>
.el-container {
  height: 100%;
}

.el-header,
.el-footer {
  background-color: #b3c0d1;
  color: #333;
  text-align: center;
  line-height: 60px;
}

.el-aside {
  background-color: #d3dce6;
  color: #333;
  text-align: center;
  line-height: 200px;
}

.el-main {
  background-color: #e9eef3;
  color: #333;
  text-align: center;
  line-height: 160px;
}

.el-header {
  --el-header-padding: 0;
}
</style>