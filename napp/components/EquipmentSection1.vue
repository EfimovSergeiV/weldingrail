<script setup>

  const props = defineProps(['categories',])

</script>



<template>
  <div class="">
    <!-- ПЕРВАЯ ВЕРСИЯ RAILWELDING EQUIPMENT (которая квадратиками)-->
    
    
    <div class="grid grid-cols-2 gap-0.5">
      <div class="" v-for="ct in props.categories" :key="ct.id">
        <div class="relative">
          <img :src="`/backgrounds/10.jpg`" class="h-[180px] w-full" />
          <div class="absolute bg-sky-800/80 hover:bg-sky-800/90 transition-all duration-300 h-full w-full top-0 left-0">
            <div class="flex items-center justify-center h-full">
              <nuxt-link :to="localePath({ name: 'ct', params: { ct: ct.url } })" class="">
                <p class="text-white text-2xl font-bold uppercase italic cursor-pointer">{{ ct.name }}</p>
              </nuxt-link>
            </div>
          </div>
        </div>
      </div>
    </div>


  </div>
</template>