<script setup lang="ts">
import katex from 'katex'
import 'katex/dist/katex.min.css'

const title = (name: string) => {
  return katex.renderToString(name, {
    throwOnError: false,
    output: 'html',
  })
}
</script>

<template>
<img src="./assets/dahliasccc.jpg" class="bannerimg" />
  <div class="flex m-10 flex-col">
    <a
      target="_blank"
      href="/cours/main.pdf"
      v-html="
        title(String.raw`E = mc^2\text{ hello
      }x^2`)
      "
      class="underline"
    />
  </div>
</template>

<style scoped>
.img-photo {
  width: 19vw;
}
.text-block {
  width: 40vw;
}
.bannerimg {
  width: 100%;
  height: 35vh;
  object-fit: cover;
}
</style>
