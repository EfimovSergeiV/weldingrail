<script setup>
  const localePath = useLocalePath()
  const config = useRuntimeConfig()
  const route = useRoute()
  const { locale, setLocale } = useI18n()
  const router = useRouter()

  const { data: category } = await useFetch(`${ config.public.baseURL }${locale.value}/c/category/${route.params.ct}/`)
  const { data: products } = await useFetch(`${ config.public.baseURL }${locale.value}/c/products/${route.params.ct}/`)




</script>


<template>
  <div class="">

    <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8 pt-4">
      <MainSlider />
    </div>

    
    <div class="">


      <!-- <div class="relative">
        <img src="/slides/1.webp" alt="logo" class="" />
        <div class="absolute bottom-0 left-0 w-full h-full ">
          <div class="container mx-auto lg:max-w-7xl lg:px-8 h-full">
            <div class="h-full flex items-center justify-start">
              
              <div class="">
                <p class="text-white text-4xl font-semibold">СТАЦИОНАРНЫЕ МАШИНЫ</p>
                <div class="hidden md:block">
                  <div v-for="text, pk in ['Машины могут объединяться с другим оборудованием для сварки рельсов', 'в единый производственный комплекс на сварочных производствах.']" :key="pk" class="flex" >
                    <div :id="pk" class="bg-white/60 p-2 my-0.5">
                      <p class="text-sky-900 font-semibold text-base">{{ text }}</p>
                    </div>
                  </div>                  
                </div>
              </div>
            
            </div>

            
          </div>
          
        </div>
      </div> -->


      <div class="pb-4">
        <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8 py-4">
          <div class="bg-sky-900 rounded-md px-4">
            <div class="flex items-center justify-start min-h-20">
              <div class="flex gap-1 text-base font-semibold text-white text-center">
                <nuxt-link :to="localePath({ name: 'index' })" class="uppercase">Главная</nuxt-link>
              </div>
              <div v-if="category" class="flex gap-1 text-base font-semibold text-white text-center mdi mdi-chevron-right">
                <p class="uppercase">{{ category.name }}</p>
              </div>
            </div>            
          </div>
        </div>
      </div>

      <div class="container mx-auto lg:max-w-7xl lg:px-8">
        <p class="text-4xl text-sky-900 font-bold uppercase italic py-4">{{ category.name }}</p>
        <!-- <div v-html="category.description" class="text-sky-900 text-xl"></div> -->
      </div>



      <div class="container mx-auto lg:max-w-7xl lg:px-8">

        <div v-if="products" class="py-8">

          <div class="grid grid-cols-1 gap-14">
            <div class="" v-for="product in products" :key="product.id">
              <div class="">
                <div class="flex items-center gap-4">
                  <div class="flex-none w-[320px]">
                    <img :src="product.image" class="w-[240px]" />
                  </div>
                  <div class="grid grid-cols-1 gap-4">
                    <nuxt-link :to="localePath({ name: 'ct-id', params: { ct: 'category.url', id: product.id } })" class="text-xl text-sky-900 font-bold uppercase">{{ product.name }}</nuxt-link>
                    <div class="text-sky-900" v-html="product.description"></div>
                    <div class="flex items-center gap-4 py-1">
                      <button class="bg-gradient-to-tr from-sky-900 via-sky-900 to-sky-900 font-semibold text-white text-base w-60 py-2 rounded-md">Запросить стоимость</button>
                      <nuxt-link :to="localePath({ name: 'ct-id', params: { ct: 'category.url', id: product.id } })" class="text-base text-sky-900 font-semibold">Подробнее</nuxt-link>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>          

        </div>


        <div v-else class="min-h-[24vh]">
          <div class="flex items-center justify-center">
            <p class="text-4xl text-sky-900 py-8">Нет товаров для отображения</p>
          </div>
        </div>

      </div>

      <div class="container mx-auto lg:max-w-7xl lg:px-8 py-8">
        <!-- <p class="text-4xl text-sky-900 font-bold uppercase italic py-4">{{ category.name }}</p> -->
        <div v-html="category.description" class="text-sky-900 text-xl"></div>
      </div>


    </div>
  </div>
</template>