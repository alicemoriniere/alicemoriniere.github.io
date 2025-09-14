<script setup lang="ts">
import katex from 'katex'
import 'katex/dist/katex.min.css'

const title = (name) => {
  return katex.renderToString(name, {
    throwOnError: false,
    output: 'html',
  })
}
</script>

<template>
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
