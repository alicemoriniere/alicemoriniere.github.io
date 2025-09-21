<template>
  <div class="flex flex-col lg:flex-row">
    <div class="w-full lg:w-5/7">
      <img
        src="./assets/moi.jpg"
        class="w-[40vw] h-[40vw] lg:w-[19vw] lg:h-[18vw] float-left mr-5 mt-3"
      />
      <span class="text-sm lg:text-base mt-0 text-justify">
        <span class="text-base lg:text-3xl underline font-bold lg:font-normal">
          Alice Morinière
        </span>
        <div class="mb-1 lg:mb-5" />
        Bienvenue sur mon site ! Je suis actuellement doctorante à l'Université de Rennes, sous la
        supervision de
        <a
          class="underline"
          target="_blank"
          href="https://jcbreton.pages.math.cnrs.fr/jcb/"
          _target="blank"
        >
          Jean-Christophe Breton,</a
        >
        sur le sujet "Théorèmes limite pour des modèles de boules aléatoires avec interaction". ce
        site, vous pourrez notamment trouver des documents relatifs à mes enseignements à
        l'Université de Rennes, en particulier pour les TP de prépa agreg en option A, des documents
        en lien avec l'agrégation (que j'ai passé en 2024) et divers mémoires de stages rédigés au
        cours de ma scolarité.
        <div class="mb-1" />
        Mon CV peut être trouvé
        <a class="underline" href="/CV.pdf" target="_blank"> ici. </a>
      </span>
    </div>
    <div class="flex flex-col mt-2 lg:mt-0 lg:ml-10">
      <span class="text-base font-bold lg:text-3xl underline mb-1 lg:font-normal lg:mb-5">
        Contact :
      </span>
      <span class="mb-1 text-sm lg:text-base">
        Bureau 212, Bâtiment 22, Campus de Beaulieu, Rennes
      </span>
      <span class="text-sm lg:text-base"> alice[dot]moriniere[at]univ-rennes[dot]fr </span>
    </div>
  </div>
</template>
