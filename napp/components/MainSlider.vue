<script setup>
	const swiper = useSwiper()


  const onSwiper = (swiper) => {
    console.log(swiper.activeIndex);
  };
  const onSlideChange = (swiper) => {
    console.log('slide change', swiper.activeIndex);
  };


</script>



<template>
    <div class="relative">
      <Swiper
        class=""
        :modules="[SwiperEffectFade, SwiperAutoplay, SwiperPagination]"
        @swiper="onSwiper"
        @slideChange="onSlideChange"
        :slides-per-view="1"
        :loop="true"
        :effect="'fade'"
        :pagination="{
          clickable: true,
        }"
        :autoplay="{
          delay: 16000,
          disableOnInteraction: true
        }"
      >
      
        <SwiperSlide v-for="slide, pk in ['/slides/1.webp','/slides/2.webp','/slides/3.webp','/slides/4.webp',]" :key="pk">
          <div class="">
            <img :src="slide" class="" />
          </div>
        </SwiperSlide>

        <!-- <div class="absolute bottom-0 right-0 z-40 p-3">
          <SwiperControls :slides="4" class="" />
        </div> -->

        
        <div class="fixed bottom-0 z-50">
          <div class="mx-8 px-2 bg-red-500">
            <div class="">
              
              <SwiperPagination class="" />
            </div>
          </div>
        </div>
        

      </Swiper>

    </div>
</template>