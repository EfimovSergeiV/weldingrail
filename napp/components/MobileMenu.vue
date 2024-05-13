<script setup>
  const mainStore = useMainStore()


</script>


<template>
  <div class="fixed z-50">
    <div class=" bg-white h-screen w-screen">

      <div class=" ">
        <div id="" class="bg-sky-900 w-full">
          <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8 flex items-center justify-between gap-12 h-full relative">
            <div class="py-4 ">
              <nuxt-link :to="localePath('index')">
                <img src="/logo-white.webp" class="h-6 md:h-12 invisible" />
              </nuxt-link>                
            </div>
          </div>
        </div>
      </div>


      <div class="py-4 px-4">
        <p class="text-2xl text-sky-900 font-bold">Привет мир </p>
              
      </div>

    </div>
  </div>

</template>