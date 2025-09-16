<script setup lang="ts"></script>

<template>
  <nav class="flex justify-between py-4 px-8">
    <RouterLink to="/" class="nav-router">Accueil</RouterLink>
    <RouterLink to="/enseignements" class="nav-router">Enseignements</RouterLink>
    <RouterLink to="/recherche" class="nav-router">Recherche</RouterLink>
    <RouterLink to="/agreg" class="nav-router">Agrégation</RouterLink>
    <RouterLink to="/divers" class="nav-router">Divers</RouterLink>
  </nav>

  <main>
<img src="./assets/dahliasccc.jpg" class="bannerimg" />

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
/*Couleur de la barre */
nav {
  background-color: #552f3c;
}
/* Couleur quand la souris passe sur la case*/
.nav-router:hover {
  background-color: #d921af;
}
</style>


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

