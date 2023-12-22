<template>
    <el-menu
      :default-active="activeIndex2"
      :router="true"
      class="el-menu-demo"
      mode="horizontal"
      @select="handleSelect"
    >
      <el-menu-item index="1" route="/">Home</el-menu-item>
      <el-sub-menu index="2">
        <template #title>Page</template>
        <el-menu-item index="2-1" route="/about">Page one</el-menu-item>
      </el-sub-menu>
      <el-menu-item index="3" disabled>Info</el-menu-item>
    </el-menu>
  </template>
  
  <script lang="ts" setup>
  import { ref } from 'vue'
  
  const activeIndex2 = ref('1')
  const handleSelect = (key: string, keyPath: string[]) => {
    console.log(key, keyPath)
  }
  </script>
  