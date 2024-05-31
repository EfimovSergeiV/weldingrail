<script setup>

  const config = useRuntimeConfig()
  const route = useRoute()
  const router = useRouter()
  const localePath = useLocalePath()
  const { locale, setLocale } = useI18n()


  const { data: categories } = await useFetch(`${ config.public.baseURL }${locale.value}/c/categories/`)
  const { data: product } = await useFetch(`${ config.public.baseURL }${locale.value}/c/product/${route.params.id}/`)


  const currentCategory = ref(null)

  if (product.value) {
    currentCategory.value = categories.value.find(category => category.id === product.value.category)
  }

  const materials = ref([
    { "id": 1, 'title': "Видеообзор 1", "link": "#", },
    { "id": 2, 'title': "Видеообзор 2", "link": "#", },
    { "id": 2, 'title': "Видеообзор 3", "link": "#", },
    { "id": 2, 'title': "Видеообзор 4", "link": "#", },
    { "id": 3, 'title': "Инструкция по эксплуатации", "link": "#", },
    { "id": 4, 'title': "Сертификат", "link": "#", },
  ])

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
  <div class="">

    <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8 pt-4">
      <MainSlider :slides="shuffle(slides)" />
    </div>


    <div class="">
      <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8 ">
        <div class="py-4 bg-white">
          <div class="bg-sky-900   px-4">
            <div class="grid grid-cols-1 md:grid-cols-2 lg:flex items-center min-h-20 justify-between">
              <div class="flex items-center justify-start">
                <div class="flex items-center justify-start">
                  <div class="flex gap-1 text-base font-semibold text-white text-center"><nuxt-link :to="localePath({ name: 'index' })" class="uppercase">Главная</nuxt-link></div>
                  <div class="flex gap-1 text-base font-semibold text-white text-center mdi mdi-chevron-double-right"><nuxt-link :to="localePath({ name: 'ct', params: { ct: currentCategory.url } })" class="uppercase">{{ currentCategory.name }}</nuxt-link></div>
                  <div v-if="product" class="flex gap-1 text-base font-semibold text-white text-center mdi mdi-chevron-double-right"><p class="uppercase">{{ product.name }}</p></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>



    <div class="container mx-auto lg:max-w-7xl lg:px-8">
      <div class="flex items-center gap-8 bg-white pt-8 px-4">
        <div class=" flex-none">
          <img :src="product.image" class="w-[290px]" />
        </div>
        <div class="grid grid-cols-1 gap-4">
          <div class="">
            <p class="text-4xl text-sky-900 font-bold uppercase italic">{{ product.name }}</p>
          </div>
          <div class="">
            <div v-if="product.description.length > 1" v-html="product.description" class="text-sky-900 text-xl"></div>
            <div v-else class="">
            <div v-for="category in categories" :key="category.id" class="text-sky-900 text-base">
              <div v-if="category.id === product.category" class="" v-html="category.description"></div>
            </div>
          </div>
          
          <div class="py-6">
            <button class="bg-gradient-to-tr from-sky-900 via-sky-800 to-sky-900 font-semibold text-white text-base w-60 py-2 shadow-xl shadow-gray-900/10  ">Запросить стоимость</button>
          </div>

          </div>
        </div>
      </div>
    </div>


    <div v-if="true" class="">

      <div class=" grid grid-cols-1 content-center">
        <div id="product-property" class="container mx-auto lg:max-w-7xl lg:px-8">
          <div class=" bg-white flex gap-8 py-8 px-4">
            <div class=" w-1/3 invisible">
              <div class="my-2">
                <p class="text-xl text-sky-900 se lect-none font-sans font-semibold uppercase">Материалы:</p>
              </div>
              
              <div class="py-2 ">
                <div class="grid grid-cols-1 gap-2 text-sky-900">
                  <div v-for="material in materials" :key="material.id" class="">
                    <a :href="material.link">
                      <div class="flex items-center gap-1">
                        <div class="mdi mdi-open-in-new"></div>
                        <p class=" text-base">{{ material.title }}</p>
                      </div>
                      
                      
                    </a>
                  </div>
                </div>
              </div>
            </div>
            <div class="w-full text-sm">
              <div class="my-2">
                <p class="text-xl text-sky-900 se lect-none font-sans font-semibold uppercase">Технические параметры:</p>
              </div>
              <div class=" grid grid-cols-1 gap-2 py-4">
                <div v-for="propdata in product.product_properties" :key="propdata.id" class="">
                  <div v-if="propdata.value" class="">
                    <div class="flex items-center justify-between text-base border-b border-sky-900/30 hover:border-sky-900/50 transition-all duration-300">
                      <p class="text-sky-900 se lect-none font-sans">{{ propdata.name }}</p>
                      <p class="text-sky-900 se lect-none font-sans font-semibold">{{ propdata.value }}</p>
                    </div>                
                  </div>
                  <div v-else class="">
                    <div class="flex items-center justify-start text-base mt-6">
                      <p class="text-sky-900 se lect-none font-sans font-semibold">{{ propdata.name }}</p>
                    </div>
                  </div>

                </div>
              </div>            
            </div>
          </div>
        </div>
      </div>



      <div v-if="product.product_advantages.length > 0" class=" bg-sky-900 grid grid-cols-1 content-center py-4 border-t border-black/10">
        <div id="product-property" class="container mx-auto lg:max-w-7xl lg:px-8">
        

          <div class="flex items-center justify-start py-4">
            <p class="text-lg font-semibold text-gray-100 uppercase">Преимущества машины</p>
          </div>
          <div class=" columns-2 gap-4">

            <div class="my-2 break-inside-avoid-column" v-for="advantage in product.product_advantages" :key="advantage.id">
              <div class="py-1">
                <div class="flex items-center gap-4">
                  <div class="mdi mdi-16px mdi-circle text-gray-200/70"></div>
                  <p class="text-sm text-gray-200">{{ advantage.name }}</p>
                </div>
                
              </div>
            </div>                

          </div>            

        
        </div>
      </div>
    </div>

    <div v-else class="">
      <div class="flex items-center justify-center py-24">
        <p class="">Товар не найден</p>
      </div>
      
    </div>



  </div>
</template>