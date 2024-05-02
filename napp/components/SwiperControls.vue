<script setup lang="ts">
	const swiper = useSwiper()
  const props = defineProps(['slides'])

  watch(swiper, () => {
    console.log('Active index changed:', swiper.value.activeIndex)
  })



</script>


<template>
  <div class="flex gap-1">
    {{ swiper.activeIndex }}
    <div v-for="slide in props.slides" :key="slide" class="">
      <button v-if="slide-1 === swiper.activeIndex" @click="swiper.slideTo(slide-1)" class=" bg-green-500 w-6 h-6 rounded-full duration-500 transition-all">{{ slide }}</button>		
      <button v-else @click="swiper.slideTo(slide-1)" class=" bg-green-500/50 w-6 h-6 rounded-full duration-500 transition-all">{{ slide }}</button>		
    </div>
  </div>
</template>