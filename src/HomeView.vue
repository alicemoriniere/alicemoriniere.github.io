<template>
  <div class="flex m-10">
    <img src="./assets/moi.jpg" class="img-photo" />
    <div class="flex flex-col w-5/8 px-5">
      <span class="text-3xl underline mb-5"> Alice Morinière </span>
      <span>
        Bienvenue sur mon site ! Je suis actuellement doctorante à l'Université de Rennes, sous la
        supervision de
        <a class="underline" target="_blank" href="https://jcbreton.pages.math.cnrs.fr/jcb/" _target="blank">
          Jean-Christophe Breton,</a
        >
        sur le sujet "Théorèmes limite pour des modèles de boules aléatoires avec interaction".
      </span>
      <span>
        Sur ce site, vous pourrez notamment trouver des documents relatifs à mes enseignements à
        l'Université de Rennes, en particulier pour les TP de prépa agreg en option A, des documents
        en lien avec l'agrégation (que j'ai passé en 2024) et divers mémoires de stages rédigés au
        cours de ma scolarité.
      </span>
      <div class="mt-1 flex items-center">
        <span class="mt-1">
          Mon CV peut être trouvé
          <a class="underline" href="/CV.pdf" target="_blank"> ici. </a>
        </span>
      </div>
    </div>
    <div class="flex flex-col px-5 w-1/3">
      <span class="text-3xl underline mb-5"> Contact : </span>
      <span class="mb-1"> Bureau 212, Bâtiment 22, Campus de Beaulieu, Rennes </span>
      <span> alice[dot]moriniere[at]univ-rennes[dot]fr </span>
    </div>
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
