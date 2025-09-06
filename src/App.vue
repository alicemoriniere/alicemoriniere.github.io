<script setup lang="ts"></script>

<template>
  <nav class="flex justify-between py-4 px-8 bg-amber-900">
    <RouterLink to="/" class="nav-router">Accueil</RouterLink>
    <RouterLink to="/enseignements" class="nav-router">Enseignements</RouterLink>
    <RouterLink to="/recherche" class="nav-router">Recherche</RouterLink>
    <RouterLink to="/agreg" class="nav-router">Agrégation</RouterLink>
    <RouterLink to="/divers" class="nav-router">Divers</RouterLink>
  </nav>
  <main>
    <RouterView />
  </main>
</template>

<style scoped>
.nav-router {
  color: white;
  padding: 5px 10px 5px 10px;
  border: 2px solid white;
  border-radius: 15px;
  font-size: 20px;
}

.nav-router:hover {
  background-color: oklch(90.1% 0.058 230.902);
}
</style>
