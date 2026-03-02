<template>
  <main class="page">
    <h1>我在</h1>
    <p>记录一生，留给未来。</p>
    <section>
      <h2>V1 原型已初始化</h2>
      <ul>
        <li>前端：Vite + Vue3 + TypeScript</li>
        <li>后端：FastAPI</li>
        <li>文档：产品、安全、API、路线图</li>
      </ul>
    </section>
    <p class="hint">API Base URL: {{ apiBaseUrl }}</p>
  </main>
</template>

<script setup lang="ts">
const apiBaseUrl = import.meta.env.VITE_API_BASE_URL ?? 'http://127.0.0.1:8000'
</script>

<style scoped>
.page {
  margin: 0 auto;
  max-width: 760px;
  padding: 3rem 1.25rem;
  font-family: "Noto Sans SC", "PingFang SC", "Microsoft YaHei", sans-serif;
  line-height: 1.6;
}

h1 {
  margin: 0;
  font-size: 2.2rem;
}

.hint {
  color: #666;
  font-size: 0.92rem;
}
</style>
