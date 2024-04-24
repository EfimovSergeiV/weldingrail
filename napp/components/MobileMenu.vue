<script setup>
  const mainStore = useMainStore()


</script>


<template>
  <div class="fixed z-50">
    <div class=" bg-white h-screen w-screen">

      <div class=" py-20 px-4">
        {{ mainStore.mobileMenu }}        
      </div>

    </div>
  </div>

</template>