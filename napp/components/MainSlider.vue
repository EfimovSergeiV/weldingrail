<script setup>
  // import { TransitionGroup } from 'vue';



  const currentSlide = ref(0)


  const onSlideChange = (swiper) => {
    currentSlide.value = swiper.realIndex
  };


  const slides = [
    {
      "id": 1,
      "image": "/slides/1.webp",
      "title": "RAIL WELDING",
      "texts": [
        "All types of high quality plastic materials which are used in the worlds most modern fastest",
        "paper machines are manufactured on our Jäger weaving machines."
      ],
      "url": "/stationary-machines/1",
    },
    {
      "id": 2,
      "image": "/slides/2.webp",
      "title": "RAIL WELDING",
      "texts": [
        "All types of high quality plastic materials which are used in the worlds most modern fastest",
        "paper machines are manufactured on our Jäger weaving machines."
      ],
      "url": "/stationary-machines/2",
    },
    {
      "id": 3,
      "image": "/slides/3.webp",
      "title": "RAIL WELDING",
      "texts": [
        "All types of high quality plastic materials which are used in the worlds most modern fastest",
        "paper machines are manufactured on our Jäger weaving machines."
      ],
      "url": "/stationary-machines/3",
    },
    {
      "id": 4,
      "image": "/slides/4.webp",
      "title": "RAIL WELDING",
      "texts": [
        "All types of high quality plastic materials which are used in the worlds most modern fastest",
        "paper machines are manufactured on our Jäger weaving machines."
      ],
      "url": "/stationary-machines/4",
    }
  ]


  const showSlideData = ref({
    "id": null,
    "image": null,
    "title": null,
    "texts": [],
    "url": null,
  })

  const onSwiper = (swiper) => {
    /// при загрузке страницы показываем первый слайд
    let data = slides[0]
    showSlideData.value = []

    showSlideData.value = {
      "id": 1,
      "image": "/slides/1.webp",
      "title": "RAIL WELDING",
      "texts": [

      ],
      "url": null,
    }

    data.texts.forEach((text) => {
      setTimeout(() => {
        showSlideData.value.texts.push(text)
      }, 500 * data.texts.indexOf(text))
    })
    setTimeout(() => {
      showSlideData.value.url = data.url
    }, 2000)

  };

  watch(currentSlide, (newVal) => {

    let data = slides[newVal]
    showSlideData.value = []

    showSlideData.value = {
      "id": 1,
      "image": "/slides/1.webp",
      "title": "RAIL WELDING",
      "texts": [

      ],
      "url": null,
    }

    data.texts.forEach((text) => {
      setTimeout(() => {
        showSlideData.value.texts.push(text)
      }, 500 * data.texts.indexOf(text))
    })
    setTimeout(() => {
      showSlideData.value.url = data.url
    }, 2000)
  })


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
          delay: 48000,
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

      <div class="absolute left-0 bottom-6 h-full z-40 p-3">
        
        <div class="grid grid-cols-1 content-between bg-red-500 h-2/3">
          
          <div class="">
            <p class="text-white text-4xl font-semibold">{{ showSlideData.title }}</p>
          </div>
          
          <div class="">
            <transition-group tag="div" name="list">
              <div v-for="text, pk in showSlideData.texts" :key="pk" >
                <div :id="pk" class="bg-white p-2 my-2">
                  <p>{{ text }}</p>
                </div>
              </div>
            </transition-group>            
          </div>


          <div class="py-2">
            <transition name="list">
              <div v-if="showSlideData.url" class="">
                <nuxt-link :to="showSlideData.url" class="bg-white p-2 my-2">Learn more</nuxt-link>
              </div>          
            </transition>          
          </div>

        </div>

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