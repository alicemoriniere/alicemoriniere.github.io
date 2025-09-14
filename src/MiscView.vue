<script setup lang="ts">
import katex from 'katex'
import 'katex/dist/katex.min.css'

const equation = () => {
  return katex.renderToString(String.raw`\int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}`, {
    throwOnError: false,
    output: 'html',
  })
}
</script>

<template>
  <div class="flex m-10 flex-col">
    <span> Latex </span>
    <span v-html="equation()" class="text-xl" />
  </div>
</template>
