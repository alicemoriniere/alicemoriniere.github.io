<script setup lang="ts"></script>

<template>
  <nav class="flex justify-between">
    <RouterLink to="/" class="nav-router">Accueil</RouterLink>
    <RouterLink to="/enseignements" class="nav-router">Enseignements</RouterLink>
    <RouterLink to="/recherche" class="nav-router">Recherche</RouterLink>
    <RouterLink to="/agreg" class="nav-router">Agrégation</RouterLink>
    <RouterLink to="/divers" class="nav-router">Divers</RouterLink>
  </nav>
  <main>
    <img src="./assets/dahliasccc.jpg" class="bannerimg" />
    <RouterView class="m-5 lg:m-10" />
  </main>
</template>

<style lang="scss" scoped>
/*Couleur de la barre */
nav {
  background-color: #552f3c;
  padding: 20px 30px 20px 30px;
}

.nav-router {
  color: white;
  padding: 5px 10px 5px 10px;
  border: 2px solid white;
  border-radius: 15px;
  font-size: 20px;
}
/* Couleur quand la souris passe sur la case*/
.nav-router:hover {
  background-color: #d921af;
}
.bannerimg {
  width: 100%;
  height: 35vh;
  object-fit: cover;
}

@media (max-width: 1000px) {
  nav {
    padding: 5px;
  }

  .nav-router {
    font-size: 11px;
    padding: 2px 5px 2px 5px;
    border-width: 1px;
  }

  .bannerimg {
    height: 23vh;
  }
}
</style>
