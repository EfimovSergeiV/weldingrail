<script setup>

  const config = useRuntimeConfig()
  const route = useRoute()
  const router = useRouter()
  const localePath = useLocalePath()
  const { locale, setLocale } = useI18n()

  console.log(route.params)

  const { data: categories } = await useFetch(`${ config.public.baseURL }${locale.value}/c/categories/`)
  const { data: product } = await useFetch(`${ config.public.baseURL }${locale.value}/c/product/${route.params.id}/`)


  const materials = ref([
    { "id": 1, 'title': "Видеообзор 1", "link": "#", },
    { "id": 2, 'title': "Видеообзор 2", "link": "#", },
    { "id": 2, 'title': "Видеообзор 3", "link": "#", },
    { "id": 2, 'title': "Видеообзор 4", "link": "#", },
    { "id": 3, 'title': "Инструкция по эксплуатации", "link": "#", },
    { "id": 4, 'title': "Сертификат", "link": "#", },
  ])

</script>


<template>
  <div class="">
    <div class="min-h-screen grid grid-cols-1 content-between">
      <div></div>

      <div class="absolute h-screen -z-10">
        <img src="/backgrounds/bg-5.webp" class="h-screen object-cover" />
      </div>

      <div class="">

        <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8">
          <div class="flex">
            <div class="bg-white/50 backdrop-blur-sm px-16 py-4 border-l-8 border-sky-800/90">
              <p class="font-sans font-extrabold text-transparent text-8xl bg-clip-text bg-gradient-to-br from-sky-950 to-sky-800 text-[40px] md:text-[72px] uppercase se lect-none">{{ $t('title-1') }}</p>
                <p class="font-sans font-extrabold text-transparent text-8xl bg-clip-text bg-gradient-to-br from-sky-950 to-sky-600 text-[40px] md:text-[68px] uppercase se lect-none">{{ $t('title-2') }}</p>             
              <div class="py-4">
                <p class="text-2xl md:text-lg text-sky-800 se lect-none font-sans font-extrabold">{{ $t('slogan') }}</p>
              </div>          
            </div>
          </div>
        </div>

      </div>


      <div class="">
        <div class="">

          <div class="bg-gradient-to-br from-sky-950/95 to-sky-800/95 backdrop-blur-sm border-t border-sky-950/40 py- 2">
            <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8 py-4">
              <div class="flex items-end justify-between">
                <div class="">
                  <p class="text-white font-black text-xl my-4">{{ $t('pages.index.chooseUs-title') }}</p>
                  <div class="grid grid-cols-3 gap-4 text-gray-100">
                    <div class="flex items-center gap-1 mdi mdi-brightness-1"><p class="text-sm text-gray-200 font-semibold ">{{ $t('pages.index.chooseUs-1') }}</p></div>
                    <div class="flex items-center gap-1 mdi mdi-brightness-1"><p class="text-sm text-gray-200 font-semibold ">{{ $t('pages.index.chooseUs-2') }}</p></div>
                    <div class="flex items-center gap-1 mdi mdi-brightness-1"><p class="text-sm text-gray-200 font-semibold ">{{ $t('pages.index.chooseUs-3') }}</p></div>
                    <div class="flex items-center gap-1 mdi mdi-brightness-1"><p class="text-sm text-gray-200 font-semibold ">{{ $t('pages.index.chooseUs-4') }}</p></div>
                    <div class="flex items-center gap-1 mdi mdi-brightness-1"><p class="text-sm text-gray-200 font-semibold ">{{ $t('pages.index.chooseUs-5') }}</p></div>
                    <div class="flex items-center gap-1 mdi mdi-brightness-1"><p class="text-sm text-gray-200 font-semibold "> {{ $t('pages.index.chooseUs-6') }}</p></div>
                  </div>                  
                </div>
                <div class="grid grid-cols-1 gap-2 text-right">
                  <div class="grid grid-cols-1 gap-1">
                    <p class="text-white text-xl font-semibold">info@weldingrail.com</p>
                  </div>
                  <div class=" shadow-xl shadow-gray-900/10">
                    <button class="bg-gradient-to-tr from-white via-gray-200 to-gray-200 font-semibold text-main-secondary w-60 py-2 mt-2 cut-corners">{{ $t('requestCall') }}</button>
                  </div>
                </div>
              </div>
            </div>
          </div>


          <div class=" bg-sky-950 border-t border-sky-950/20 border-white">
            <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8">
              <div class="flex items-center h-20 justify-between">
                <div class="flex items-center gap-2"><span class="font-bold text-gray-100 text-[36px]">+150</span><p class="text-gray-100 text-base font-semibold"> {{ $t('pages.index.employees') }}</p></div>
                <div class="flex items-center gap-2"><span class="font-bold text-gray-100 text-[36px]">+3500</span><p class="text-gray-100 text-base font-semibold"> {{ $t('pages.index.complProjects') }}</p></div>
                <div class="flex items-center gap-2"><span class="font-bold text-gray-100 text-[36px]">+560Ha</span><p class="text-gray-100 text-base font-semibold"> {{ $t('pages.index.prodArea') }}</p></div>
                <div class="flex items-center gap-2"><span class="font-bold text-gray-100 text-[36px]">+200</span><p class="text-gray-100 text-base font-semibold">Клиентов</p></div>
              </div>
            </div>
          </div>

        </div>

      </div>
    </div>


    <div id="breadcrumbs" class="bg-gray-300 grid grid-cols-1 content-center ">
      <div class="container mx-auto lg:max-w-7xl lg:px-8">
        <div class="my-4">
            <div class="flex items-center justify-start">
              <div class="flex gap-1 text-sm font-semibold text-sky-950 text-center"><nuxt-link :to="localePath({ name: 'index' })" class="uppercase">Главная</nuxt-link></div>
              <div class="flex gap-1 text-sm font-semibold text-sky-950 text-center mdi mdi-chevron-double-right"><nuxt-link :to="localePath({ name: 'c', hash: '#products' })" class="uppercase">Оборудование для сварки рельсов</nuxt-link></div>
              <div v-if="product" class="flex gap-1 text-sm font-semibold text-sky-950 text-center mdi mdi-chevron-double-right"><p class="uppercase">{{ product.name }}</p></div>
            </div>
          </div>
      </div>
    </div>




    <div v-if="product" class="">
      <div class="bg-white py-2 grid grid-cols-1 content-center">
        <div class="container mx-auto lg:max-w-7xl lg:px-8">

          <div class="">

            <div class="flex items-center gap-8 py-2">
              <div class="flex gap-2">
                <div class="bg-white w-[400px] flex items-center justify-center">
                  <img :src="product.image" class=" py-4" />
                </div>


                <!-- <div class="">
                  <Swiper
                    class="rounded-md relative h-[28rem] flex items-center justify-center"
                    :modules="[]"
                    :direction="'vertical'"
                    :slides-per-view="4"
                    :loop="true"
                    :effect="'fade'"
                    >
                    <SwiperSlide v-for="slide in 9" :key="slide" class="bg-white">
                      <img
                        src="/prod/fbm-140.png"
                        class="w-12"
                      />             
                    </SwiperSlide>
                    <div class="absolute bottom-0 right-0 z-40 p-3">
                      <SwiperControls class="bg-gray-100/80 rounded-full border border-gray-200/50 hover:border-gray-300 dark:border-gray-600/50 dark:hover:border-gray-500 dark:bg-gray-700/80 transition-all duration-500 px-1" />
                    </div>
                  </Swiper>
                </div> -->

              </div>               
              <div class="grid grid-cols-1 content-between py-20">
                <div class="flex items-center justify-start">
                  <!-- <p class="text-lg font-semibold text-sky-950 text-center">{{ $t('pages.index.prod-name-1') }}</p> -->
                  <p class="text-xl font-semibold text-sky-950 text-center">{{ product.name }}</p>
                </div>

                <div class="py-4 text-lg text-sky-950">
                  <div v-if="product.description.length > 1" class="" v-html="product.description"></div>
                  <div v-else class="">
                    <div v-for="category in categories" :key="category.id">
                      <div v-if="category.id === product.category" class="" v-html="category.description"></div>
                    </div>
                  </div>
                </div>

                <div class="flex items-end justify-between gap-4 py-4">
                  <div class="">
                    <!-- <div class="">
                      <div class="">
                        <p class="text-sky-900 text-sm font-semibold">Вариант исполнения:</p>
                        <div class="flex gap-1 my-2">
                          <div class="bg-gray-100 px-1 py-1 rounded-2xl flex items-center justify-center border border-sky-950/10">
                            <input id="var"  type="radio" value="archive" name="default-radio" class="text-xs text-sky-800 bg-gray-100 border-gray-300 focus:ring-sky-500/0  focus:ring-0">
                            <label for="var" class="text-xs mx-2 font-semibold text-sky-800 cursor-pointer"> Грузовой автомобиль</label>
                          </div>
                          <div class="bg-gray-100 px-1 py-1 rounded-2xl flex items-center justify-center border border-sky-950/10">
                            <input id="var"  type="radio" value="file" name="default-radio" class="text-xs text-sky-800 bg-gray-100 border-gray-300 focus:ring-sky-500/0 focus:ring-0">
                            <label for="var" class="text-xs mx-2 font-semibold text-sky-800 cursor-pointer"> ЖД платформа</label>
                          </div>
                        </div>
                      </div>
                    </div> -->
                    <!-- <div class="">
                      <div class="bg-white flex items-center gap-2 cursor-pointer">
                        <img src="/pngegg.webp" class="w-10 opacity-95" />
                        <div class="grid grid-cols-1 items-center gap-0.5">
                          <p class="text-sky-900 text-sm font-semibold uppercase"> FBM-140 RAIL WELDING MACHINE</p>
                          <p class="text-sky-950 text-sm">.PDF</p>
                        </div>
                      </div>                    
                    </div> -->
                  </div>

                  <button class="text-sm shadow-md shadow-black/50 bg-sky-800 text-gray-100 px-4 py-2 font-semibold uppercase cut-corners">Запросить стоимость</button>
                </div>
              </div>
            </div>



          </div>
        </div>


        <!-- <div class=" bg-white py-4">
          <div class="">

            <div class="container mx-auto lg:max-w-7xl lg:px-8 py-4 ">
              <div class="flex items-center justify-start py-4">
                <p class="text-lg font-semibold text-sky-950 uppercase">Преимущества:</p>
              </div>
              <div class=" columns-2 gap-4">

                <div class="my-2 break-inside-avoid-column" v-for="(advantage, pk) in advantages" :key="pk">
                  <div class="px-2 py-4 bg-gradient-to-br from-gray-100/95 to-gray-50/90 border-l-8 border-sky-800/90 shadow-lg shadow-black/10">
                    <p class="text-sm font-semibold text-sky-900">{{ advantage.text }}</p>
                  </div>
                </div>                

              </div>            
            </div>

          </div>
        </div> -->
      </div>




      <div class=" bg-white grid grid-cols-1 content-center py-2">
        <div id="product-property" class="container mx-auto lg:max-w-7xl lg:px-8">
          <div class=" flex gap-8 py-8">
            <div class=" w-1/3">
              <div class="my-2">
                <p class="text-xl text-sky-950 se lect-none font-sans font-semibold">Материалы:</p>
              </div>
              
              <div class="py-2 ">
                <div class="grid grid-cols-1 gap-2 text-sky-950">
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
                <p class="text-xl text-sky-950 se lect-none font-sans font-semibold">Технические параметры:</p>
              </div>
              <div class=" grid grid-cols-1 gap-2 py-4">
                <div v-for="propdata in product.product_properties" :key="propdata.id" class="">
                  <div v-if="propdata.value" class="">
                    <div class="flex items-center justify-between text-base border-b border-sky-950/30 hover:border-sky-950/50 transition-all duration-300">
                      <p class="text-sky-950 se lect-none font-sans">{{ propdata.name }}</p>
                      <p class="text-sky-950 se lect-none font-sans font-semibold">{{ propdata.value }}</p>
                    </div>                
                  </div>
                  <div v-else class="">
                    <div class="flex items-center justify-start text-base mt-6">
                      <p class="text-sky-950 se lect-none font-sans font-semibold">{{ propdata.name }}</p>
                    </div>
                  </div>

                </div>
              </div>            
            </div>
          </div>
        </div>
      </div>



      <div v-if="product.product_advantages.length > 0" class=" bg-sky-950 grid grid-cols-1 content-center py-4 border-t border-black/10">
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


    <div class="container mx-auto lg:max-w-7xl lg:px-8">
      <div class="py-4">
        <p class="text-sky-950 text-base font-sans font-semibold">Комплектующие МРКК-001:</p>

      </div>
      <div class="">

      </div>

      <div class="grid grid-cols-1 gap-4">
        <div class="">
          <div class="py-2">
            <p class="text-sky-950 text-base font-sans font-semibold">FBM-140</p>
          </div>

          <p class="text-base text-sky-950">
            The machine is designed for flash butt welding of rails with cross-sectional area of from 6,500 mm to 10,000 mm in field conditions, through continuous or pulsating flashing, and removes flash immediately after welding. Due to the increased upsetting force of 140 tons, the welding machine is capable of welding long rail strings into tracks and tightening the strings.
          </p>
        </div>
        <div class="">
          <div class="my-4 flex items-center gap-4 py-1">
            <button class="text-sm shadow-md shadow-black/50 bg-sky-800 text-gray-100 px-4 py-2 font-semibold uppercase cut-corners">Запросить стоимость</button>
            <nuxt-link :to="localePath({ name: 'c-name', hash: '#product-description', params: { name: 'fbm-140'} })" class="text-sm text-sky-800 font-semibold">Предыдущий</nuxt-link>
            <nuxt-link :to="localePath({ name: 'c-name', hash: '#product-description', params: { name: 'fbm-140'} })" class="text-sm text-sky-800 font-semibold">Следующий</nuxt-link>
          </div>
        </div>

      </div>
    </div>


  </div>
</template>