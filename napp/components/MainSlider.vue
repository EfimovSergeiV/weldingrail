<script setup>

  const slides = [
    {
      "id": 1,
      "image": "/slides/1.webp",
      "title": "СТАЦИОНАРНЫЕ МАШИНЫ",
      "texts": [
        "Применяются для изготовления рельсовых путей на заводах.",
        "Сварка рельсов с площадью поперечного сечения до 18000 мм."
      ],
      "url": "/stationary-machines/",
    },
    {
      "id": 2,
      "image": "/slides/2.webp",
      "title": "МОБИЛЬНЫЕ МАШИНЫ",
      "texts": [
        "Предназначены для контактной стыковой сварки в стационарных или полевых условиях",
        "Процесс сварки стыка осуществляется автоматически по заданной программе."
      ],
      "url": "/mobile-machines/",
    },
    {
      "id": 3,
      "image": "/slides/5.webp",
      "title": "МОБИЛЬНЫЕ РЕЛЬСОСВАРОЧНЫЕ КОМПЛЕКСЫ",
      "texts": [
        "Предназначены для контактной стыковой сварки в полевых условиях",
        "Оборудование компактно размещается в небольшом 20-футовом контейнере."
      ],
      "url": "/railwelding-complexes/",
    },
    {
      "id": 4,
      "image": "/slides/4.webp",
      "title": "ИСПЫТАТЕЛЬНОЕ ОБОРУДОВАНИЕ",
      "texts": [
        "Компактные размеры и масса пресса позволяют использовать его как в условиях стационарной установки",
        "так и в составе переносных рельсосварочных машин."
      ],
      "url": "/testing-equipment/",
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
      "title": null,
      "texts": [

      ],
      "url": null,
    }

    setTimeout(() => {
      showSlideData.value.title = data.title
    }, 500)

    data.texts.forEach((text) => {
      setTimeout(() => {
        showSlideData.value.texts.push(text)
      }, 500 * data.texts.indexOf(text))
    })
    setTimeout(() => {
      showSlideData.value.url = data.url
    }, 1000)
  })


  const pagination = {
    "clickable": true,
    renderBullet: function (index, className) {
      return '<span class="p-2 ' + className + '">' + '</span>';
    },
  }


</script>



<template>
    <div class="relative">
      <Swiper
        class=""
        :modules="[SwiperEffectFade, SwiperAutoplay, SwiperPagination]"
        @swiper="onSwiper"
        @slideChange="onSlideChange"
        :pagination="pagination"
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

      
      <div class="absolute left-0 bottom-8 h-full w-full z-40 py-2 ">

        
        <div class="h-full content-end bg-red-500/0">


          <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8">
            <div class="">
              <transition name="right">
                <div v-if="showSlideData.title" class="py-2">
                  <p class="text-white text-4xl font-semibold">{{ showSlideData.title }}</p>
                </div>
              </transition>
              <div class=" md:h-36">
                <div class="hidden md:block">
                  <div class="flex">
                    <transition-group tag="div" name="list">
                      <div v-for="text, pk in showSlideData.texts" :key="pk" class="flex" >
                        <div :id="pk" class="bg-white/60 p-2 my-0.5">
                          <p class="text-sky-900 font-semibold text-base">{{ text }}</p>
                        </div>
                      </div>
                    </transition-group>
                  </div>                  
                </div>
                <div class="py-4">
                  <transition name="list">
                    <div v-if="showSlideData.url" class="">
                      <nuxt-link :to="showSlideData.url" class="bg-sky-700 text-white text-base px-6 py-2 my-2">Узнать больше</nuxt-link>
                    </div>          
                  </transition>          
                </div>
              </div>
            </div>
          </div>


        </div>




      </div>


    </div>
</template>


<style>
  .swiper-pagination {
    position: absolute;
    text-align: center;
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
    background: #fff;
    background: var(--swiper-pagination-bullet-inactive-color, #fff);
    opacity: 0.5;
    opacity: var(--swiper-pagination-bullet-inactive-opacity, 0.5);
  }
  .swiper-pagination-bullet-active {
    opacity: 1;
    opacity: var(--swiper-pagination-bullet-opacity, 1);
    background: #fff;
  }
</style>