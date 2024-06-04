<script setup>
  const localePath = useLocalePath()
  const config = useRuntimeConfig()
  const route = useRoute()
  const { locale, setLocale } = useI18n()
  const router = useRouter()

  const { data: slides } = await useFetch(`${ config.public.baseURL }${locale.value}/d/slides/`)
  const { data: category } = await useFetch(`${ config.public.baseURL }${locale.value}/c/category/${route.params.ct}/`)
  const { data: products } = await useFetch(`${ config.public.baseURL }${locale.value}/c/products/${route.params.ct}/`)


  /// Перемешиваем слайды в случайном порядке
  // const shuffle = (array) => {
  //   let currentIndex = array.length, randomIndex;
  //   while (currentIndex != 0) {
  //     randomIndex = Math.floor(Math.random() * currentIndex);
  //     currentIndex--;
  //     [array[currentIndex], array[randomIndex]] = [
  //       array[randomIndex], array[currentIndex]];
  //   }
  //   return array;
  // }


</script>


<template>
  <div class="">

    <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8 pt-4">
      <MainSlider :slides="slides" />
    </div>

    
    <div v-if="category" class="">

      <div class="">
        <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8 ">
          <div class="py-4 bg-white">
            <div class="bg-sky-900   px-4">
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
      </div>

      <div class="container mx-auto lg:max-w-7xl lg:px-8">
        <p class="text-4xl text-sky-900 font-bold uppercase italic py-4 bg-white px-4">{{ category.name }}</p>
      </div>

      <div class="container mx-auto lg:max-w-7xl lg:px-8">

        <div v-if="products" class="py-8 px-4 bg-white">

          <div class="grid grid-cols-1 gap-14">
            <div class="" v-for="product in products" :key="product.id">
              <div class="">
                <div class="flex items-center gap-4">
                  <div class="flex-none w-[320px]">
                    <img :src="product.image" class="w-[240px]" />
                  </div>
                  <div class="grid grid-cols-1 gap-4">
                    <nuxt-link :to="localePath({ name: 'ct-id', params: { ct: 'category.url', id: product.id } })" class="text-xl text-sky-900 font-bold">{{ product.name }}</nuxt-link>
                    <div class="text-sky-900" v-html="product.description"></div>
                    <div class="flex items-center gap-4 py-1">
                      <button class="bg-gradient-to-tr from-sky-900 via-sky-800 to-sky-900 font-semibold text-white text-base py-2 px-4 shadow-xl shadow-gray-900/10  ">Запросить стоимость</button>
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

      <div class="container mx-auto lg:max-w-7xl lg:px-8">
        <div class="bg-white py-8 px-4">
          <div v-html="category.description" class="text-sky-900 text-xl"></div>
        </div>
        
      </div>


    </div>
  </div>
</template>