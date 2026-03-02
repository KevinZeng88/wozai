<template>
  <div class="shell">
    <header class="topbar">
      <a href="#" class="brand">
        <span class="brand-mark">我在</span>
        <span class="brand-sub">wozai.org</span>
      </a>
      <nav class="nav">
        <a href="#concept">理念</a>
        <a href="#security">安全</a>
        <a href="#features">功能</a>
        <a href="#qingming">清明</a>
      </nav>
    </header>

    <main>
      <section class="hero">
        <p class="eyebrow">V1 原型站点</p>
        <h1>把一生写给世界，也留给所爱之人。</h1>
        <p class="hero-text">
          “我在”致力于帮助每个人记录生平、保存最终寄语，并在合适的时刻将记忆转化为有温度的纪念空间。
          从此后的人生叙事，到身后哀思的安放，都有一个可信、克制、体面的归处。
        </p>
        <div class="hero-actions">
          <a href="#features" class="btn btn-primary">查看产品原型</a>
          <a href="#security" class="btn btn-ghost">阅读安全承诺</a>
        </div>
      </section>

      <section id="concept" class="section">
        <div class="section-head">
          <p class="section-kicker">产品理念</p>
          <h2>记录不是为了停在过去，而是让存在被认真看见。</h2>
        </div>
        <div class="grid concept-grid">
          <article v-for="item in conceptCards" :key="item.title" class="card">
            <h3>{{ item.title }}</h3>
            <p>{{ item.description }}</p>
          </article>
        </div>
      </section>

      <section id="security" class="section">
        <div class="section-head">
          <p class="section-kicker">安全机制</p>
          <h2>默认零知识，未经授权，任何人都无法访问你的私密数据。</h2>
        </div>
        <div class="grid security-grid">
          <article v-for="item in securityCards" :key="item.title" class="card secure-card">
            <h3>{{ item.title }}</h3>
            <p>{{ item.description }}</p>
          </article>
        </div>
        <p class="api-hint">
          原型 API：
          <code>{{ apiBaseUrl }}</code>
        </p>
      </section>

      <section id="features" class="section">
        <div class="section-head">
          <p class="section-kicker">V1 功能</p>
          <h2>从个人记录到纪念页面，先完成最重要的一步。</h2>
        </div>
        <div class="timeline">
          <article v-for="item in featureTimeline" :key="item.title" class="timeline-item">
            <p class="timeline-tag">{{ item.tag }}</p>
            <h3>{{ item.title }}</h3>
            <p>{{ item.description }}</p>
          </article>
        </div>
      </section>

      <section id="qingming" class="section qingming">
        <div class="section-head">
          <p class="section-kicker">清明纪念</p>
          <h2>清明时节，在线上也可以安静献花、点灯、留言。</h2>
        </div>
        <div class="grid qingming-grid">
          <article class="card">
            <h3>线上追思墙</h3>
            <p>面向亲友与公众的纪念场域，保留体面、克制和秩序感。</p>
          </article>
          <article class="card">
            <h3>献花与点灯</h3>
            <p>用低打扰的交互传达思念，减少复杂操作，保留仪式感。</p>
          </article>
          <article class="card">
            <h3>留言纪念</h3>
            <p>留下想说的话，给逝者、给家人，也给未来的自己。</p>
          </article>
        </div>
      </section>
    </main>

    <footer class="footer">
      <p>我在 · 记录一生，留给未来。</p>
      <p>© 2026 wozai.org</p>
    </footer>
  </div>
</template>

<script setup lang="ts">
const apiBaseUrl = import.meta.env.VITE_API_BASE_URL ?? 'http://127.0.0.1:8000'

const conceptCards = [
  {
    title: '为自己记录',
    description:
      '把人生中真正重要的人、事、选择沉淀下来，形成完整可回看的人生档案。',
  },
  {
    title: '为家人留下',
    description:
      '去世后，亲友可在纪念页中看到被授权公开的生平与寄语，作为追忆和哀悼空间。',
  },
  {
    title: '为时代存证',
    description:
      '每个人都应拥有可被尊重的数字存在，形成跨代传递的个人记忆样本。',
  },
]

const securityCards = [
  {
    title: '用户端加密',
    description:
      '内容在浏览器端完成加密，服务端仅接收密文和必要元数据，不存明文。',
  },
  {
    title: '密钥归用户',
    description: '密钥由用户口令派生并由用户自行掌握，平台与管理员无权代持。',
  },
  {
    title: '默认不可恢复',
    description:
      '忘记密钥无法找回，这是零知识边界的一部分，确保未授权访问在技术上不可行。',
  },
]

const featureTimeline = [
  {
    tag: '01',
    title: '邮箱验证码登录',
    description: '以中文用户易理解的方式完成账号创建和基础身份验证。',
  },
  {
    tag: '02',
    title: '人生档案与最终寄语',
    description: '支持生平记录与“最终想说的话”写作，并按字段控制公开范围。',
  },
  {
    tag: '03',
    title: '执行人触发与审核',
    description: '由执行人提交申请，平台进行人工审核后开启纪念页面。',
  },
  {
    tag: '04',
    title: '公开纪念页与追思活动',
    description: '纪念页、清明追思墙、献花点灯与留言形成完整纪念闭环。',
  },
]
</script>
