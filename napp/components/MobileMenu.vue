<script setup>
  const mainStore = useMainStore()


</script>


<template>
  <div class="fixed z-50">
    <div class=" bg-slate-700 h-screen w-screen">

      <div @click="mainStore.mobileMenu = false" class="mdi mdi-24px mdi-menu-open"></div>


      {{ mainStore.mobileMenu }}


    </div>
  </div>

</template>