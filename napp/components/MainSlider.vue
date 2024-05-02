<script setup>
import { TransitionGroup } from 'vue';



  const currentSlide = ref(0)


  const onSlideChange = (swiper) => {
    console.log('onSlideChange')
    console.log(swiper)

    // currentSlide.value = swiper.activeIndex
    currentSlide.value = swiper.realIndex
  };


  const slides = [
    { "id": 1, "image": "/slides/1.webp", "toptext": "1 All types of high quality plastic materials which are used in the worlds most modern fastest", "bottomtext": "paper machines are manufactured on our Jäger weaving machines. " },
    { "id": 2, "image": "/slides/2.webp", "toptext": "2 All types of high quality plastic materials which are used in the worlds most modern fastest", "bottomtext": "paper machines are manufactured on our Jäger weaving machines. " },
    { "id": 3, "image": "/slides/3.webp", "toptext": "3 All types of high quality plastic materials which are used in the worlds most modern fastest", "bottomtext": "paper machines are manufactured on our Jäger weaving machines. " },
    { "id": 4, "image": "/slides/4.webp", "toptext": "4 All types of high quality plastic materials which are used in the worlds most modern fastest", "bottomtext": "paper machines are manufactured on our Jäger weaving machines. " },
  ]


  const showSlideData = ref([])

  const onSwiper = (swiper) => {
    console.log('onSwiper')
    let text = slides[0]
    showSlideData.value = []
    /// с задержкой в 500 мсек добавляем текст в массив
    setTimeout(() => {
      showSlideData.value.push(text.toptext)
    }, 500)
    setTimeout(() => {
      showSlideData.value.push(text.bottomtext)
    }, 1000)
  };

  watch(currentSlide, (newVal) => {
    console.log(newVal)
    let text = slides[newVal]
    showSlideData.value = []
    /// с задержкой в 500 мсек добавляем текст в массив
    setTimeout(() => {
      showSlideData.value.push(text.toptext)
    }, 500)
    setTimeout(() => {
      showSlideData.value.push(text.bottomtext)
    }, 1000)
    // showSlideData.value.push(text.toptext)
    // showSlideData.value.push(text.bottomtext)
  })


</script>



<template>
    <div class="relative">
      currentSlide: {{ currentSlide }}
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
          delay: 8000,
          disableOnInteraction: true
        }"
      >
      
        <SwiperSlide v-for="slide in slides" :key="slide.id">
          <div class="">
            <img :src="slide.image" class="" />
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

      <div class="absolute left-0 bottom-1/2 z-40 p-3">
        
        <transition-group tag="div" name="list">
          
          <div v-for="slide, pk in showSlideData" :key="pk" >
            <div :id="pk" class="bg-white p-2 my-2">
              <p>{{ slide }}</p>
            </div>
          </div>

        </transition-group>
        
      </div>

    </div>
</template>


<style>
  .swiper-pagination {
    position: absolute;
    text-align: left;
    margin-left: 6vw;
    transition: 300ms opacity;
    transform: translate3d(0, 0, 0);
    z-index: 10;
  }
  .swiper-pagination-bullet {
    width: 18px;
    width: var(--swiper-pagination-bullet-width, var(--swiper-pagination-bullet-size, 18px));
    height: 18px;
    height: var(--swiper-pagination-bullet-height, var(--swiper-pagination-bullet-size, 18px));
    display: inline-block;
    border-radius: 50%;
    border-radius: var(--swiper-pagination-bullet-border-radius, 50%);
    background: #0369a1;
    background: var(--swiper-pagination-bullet-inactive-color, #0369a1);
    opacity: 0.5;
    opacity: var(--swiper-pagination-bullet-inactive-opacity, 0.5);
  }
  .swiper-pagination-bullet-active {
    opacity: 1;
    opacity: var(--swiper-pagination-bullet-opacity, 1);
    background: #082f49;
  }
</style>