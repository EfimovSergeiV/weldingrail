<script setup>

  const slides = [
    {
      "id": 1,
      "image": "/slides/1.webp",
      "title": "WIRE PRODUCTION",
      "texts": [
        "All types of high quality plastic materials which are used in the worlds most modern fastest",
        "paper machines are manufactured on our Jäger weaving machines."
      ],
      "url": "/stationary-machines/1",
    },
    {
      "id": 2,
      "image": "/slides/2.webp",
      "title": "A RELIABLE PARTNER",
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
      "title": "PMC WEAVING MACHINES",
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

  const currentSlide = ref(0)
  const onSlideChange = (swiper) => {
    showSlideData.value = {
      "id": null,
      "image": null,
      "title": null,
      "texts": [],
      "url": null,
    }
    currentSlide.value = swiper.realIndex
  };

  const onSwiper = (swiper) => {
    /// при загрузке страницы показываем первый слайд
    let data = slides[0]
    showSlideData.value = {
      "id": data.id,
      "image": data.image,
      "title": data.title,
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
    }, 1000)
  };

  watch(currentSlide, (newVal) => {
    let data = slides[newVal]
    showSlideData.value = {
      "id": data.id,
      "image": data.title,
      "title": data.title,
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
    }, 1000)
  })

  const slideNext = () => {
    swiper.realIndex = 4
  }


</script>



<template>
    <div class="relative">
      <Swiper
        class=""
        :modules="[SwiperEffectFade, SwiperAutoplay, SwiperPagination]"
        @swiper="onSwiper"
        @slideChange="onSlideChange"
        :pagination="{
          clickable: true,
        }"
        :slides-per-view="1"
        :loop="true"
        :effect="'fade'"
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

      </Swiper>

      
      <div class="absolute left-0 bottom-0 h-full w-full z-40 py-2 ">

        
        <div class="h-full content-end bg-red-500/0">


          <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8">
            <div class="">
              <transition name="right-emergence">
                <div v-if="showSlideData.title" class="py-2">
                  <p class="text-white text-4xl font-semibold">{{ showSlideData.title }}</p>
                </div>
              </transition>
              <div class=" md:h-36">
                <div class="hidden md:block">
                  <div class="flex">
                    <transition-group tag="div" name="list">
                      <div v-for="text, pk in showSlideData.texts" :key="pk" class="flex" >
                        <div :id="pk" class="bg-white p-2 my-0.5">
                          <p>{{ text }}</p>
                        </div>
                      </div>
                    </transition-group>
                  </div>                  
                </div>
                <div class="py-4">
                  <transition name="list">
                    <div v-if="showSlideData.url" class="">
                      <nuxt-link :to="showSlideData.url" class="bg-blue-500 text-white p-2 my-2">Learn more</nuxt-link>
                    </div>          
                  </transition>          
                </div>
              </div>
            </div>
          </div>


          <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8">
            <button @click="slideNext" class="bg-blue-500 text-white p-2 my-2">Next</button>
          </div>

        </div>




      </div>


    </div>
</template>

