<template>
  <img src="./assets/roses.jpeg" class="bannerimg" />
  <div class="flex m-10">
    <img src="./assets/moi.jpg" class="img-photo" />
    <div class="flex flex-col w-5/8 px-5">
      <span class="text-3xl underline mb-5"> Alice Morinière </span>
      <span>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
        labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco
        laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in
        voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat
        cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</span
      >
      <div class="mt-1 flex items-center">
        <span class="mt-1">
          Mon CV peut être trouvé
          <a class="underline" href="/main.pdf" target="_blank"> ici </a></span
        >
      </div>
    </div>
    <div class="flex flex-col px-5 w-1/4">
      <span class="text-3xl underline mb-5"> Contact: </span>
      <span class="mb-1"> Bureau 212 Batiement 22 blabla </span>
      <span> alice.moriniere@adressemail.com </span>
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
