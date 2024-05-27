<script setup>
  const localePath = useLocalePath()
  const config = useRuntimeConfig()
  const route = useRoute()
  const { locale, setLocale } = useI18n()




  const { data: categories } = await useFetch(`${ config.public.baseURL }${locale.value}/c/categories/`)
  const { data: products } = await useFetch(`${ config.public.baseURL }${locale.value}/c/products/`)

  const slides = [
    {
      "id": 1,
      "image": "/slides/blue-1.webp",
      "title": "СТАЦИОНАРНЫЕ МАШИНЫ",
      "texts": [
        "Машины могут объединяться с другим оборудованием для сварки рельсов ",
        "в единый производственный комплекс на сварочных производствах"
      ],
      "url": "ru/stationary-machines/",
    },
    {
      "id": 2,
      "image": "/slides/blue-2.webp",
      "title": "МОБИЛЬНЫЕ МАШИНЫ",
      "texts": [
        "Предназначены для контактной стыковой сварки в стационарных или полевых условиях",
        "Процесс сварки стыка осуществляется автоматически по заданной программе."
      ],
      "url": "ru/mobile-machines/",
    },
    {
      "id": 3,
      "image": "/slides/blue-3.webp",
      "title": "МОБИЛЬНЫЕ РЕЛЬСОСВАРОЧНЫЕ КОМПЛЕКСЫ",
      "texts": [
        "Предназначены для контактной стыковой сварки в полевых условиях",
        "Оборудование компактно размещается в небольшом 20-футовом контейнере."
      ],
      "url": "ru/railwelding-complexes/",
    },
    {
      "id": 4,
      "image": "/slides/blue-4.webp",
      "title": "ИСПЫТАТЕЛЬНОЕ ОБОРУДОВАНИЕ",
      "texts": [
        "Компактные размеры и масса пресса позволяют использовать",
        "как стационарно, так и в составе переносных рельсосварочных машин."
      ],
      "url": "ru/testing-equipment/",
    }
  ]

  /// Перемешиваем слайды в случайном порядке
  const shuffle = (array) => {
    let currentIndex = array.length, randomIndex;
    while (currentIndex != 0) {
      randomIndex = Math.floor(Math.random() * currentIndex);
      currentIndex--;
      [array[currentIndex], array[randomIndex]] = [
        array[randomIndex], array[currentIndex]];
    }
    return array;
  }

</script>


<template>
  <div>

    <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8 pt-4">
      <MainSlider :slides="shuffle(slides)" />
    </div>


    <div class="">
      <div class="">
        <div class="bg-gray-white">
          <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8 py-8">
            <div class="grid grid-cols-1 lg:flex items-end justify-between">
              <div class="">
                <p class="text-2xl text-sky-900 font-bold uppercase italic my-4">{{ $t('pages.index.chooseUs-title') }}</p>
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 text-sm md:text-base font-semibold">
                  <div class="flex items-center gap-1 mdi mdi-brightness-1 text-sky-900/80 uppercase"><p class="text-sm text-sky-900">{{ $t('pages.index.chooseUs-1') }}</p></div>
                  <div class="flex items-center gap-1 mdi mdi-brightness-1 text-sky-900/80 uppercase"><p class="text-sm text-sky-900">{{ $t('pages.index.chooseUs-2') }}</p></div>
                  <div class="flex items-center gap-1 mdi mdi-brightness-1 text-sky-900/80 uppercase"><p class="text-sm text-sky-900">{{ $t('pages.index.chooseUs-3') }}</p></div>
                  <div class="flex items-center gap-1 mdi mdi-brightness-1 text-sky-900/80 uppercase"><p class="text-sm text-sky-900">{{ $t('pages.index.chooseUs-4') }}</p></div>
                  <div class="flex items-center gap-1 mdi mdi-brightness-1 text-sky-900/80 uppercase"><p class="text-sm text-sky-900">{{ $t('pages.index.chooseUs-5') }}</p></div>
                  <div class="flex items-center gap-1 mdi mdi-brightness-1 text-sky-900/80 uppercase"><p class="text-sm text-sky-900"> {{ $t('pages.index.chooseUs-6') }}</p></div>
                </div>                  
              </div>
              <div class="grid grid-cols-1 gap-2 text-right">
                <div class="">
                  <a href="mailto:info@railwelding.com" target="_blank" class="text-sky-900 text-xl font-semibold">info@weldingrail.com</a>
                </div>
                <div class=" shadow-xl shadow-gray-900/10">
                  <button class="bg-gradient-to-tr from-sky-900 via-sky-800 to-sky-900 font-semibold text-white text-base w-60 py-2 shadow-xl shadow-gray-900/10 rounded-md">{{ $t('requestCall') }}</button>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="">
          <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8">
            <div class="grid grid-cols-1 md:grid-cols-2 lg:flex items-center min-h-20 justify-between bg-sky-900 rounded-md px-8">
              <div class="flex items-center gap-2"><span class="font-bold text-white text-[36px]">+250</span><p class="text-white text-base font-semibold"> {{ $t('pages.index.employees') }}</p></div>
              <div class="flex items-center gap-2"><span class="font-bold text-white text-[36px]">+300</span><p class="text-white text-base font-semibold"> {{ $t('pages.index.complProjects') }}</p></div>
              <div class="flex items-center gap-2"><span class="font-bold text-white text-[36px]">+460Ha</span><p class="text-white text-base font-semibold"> {{ $t('pages.index.prodArea') }}</p></div>
              <div class="flex items-center gap-2"><span class="font-bold text-white text-[36px]">+150</span><p class="text-white text-base font-semibold">Клиентов</p></div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="min-h-[60vh] flex items-center justify-center">
      <div class="grid grid-cols-1 gap-2">
        
        <p class="text-center text-4xl text-sky-900 font-bold uppercase italic my-4">Страница не найдена</p>
        <nuxt-link :to="localePath('index')" class="text-center text-2xl text-sky-900">Вернуться на главную</nuxt-link>


      </div>

    </div>

  </div>

  <!-- <div class="h-screen flex items-center justify-center">
    <div class="">
      
      <p class="text-center text-red-800 text-2xl">
        ERROR 404: Page not found
      </p>

      <p class="text-center text-red-800 text-2xl">
        {{ route }}
      </p>      
    </div>

  </div> -->
</template>