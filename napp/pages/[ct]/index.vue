<script setup>
  const localePath = useLocalePath()
  const config = useRuntimeConfig()
  const route = useRoute()
  const { locale, setLocale } = useI18n()
  const router = useRouter()

  const { data: slides } = await useFetch(`${ config.public.baseURL }${locale.value}/d/slides/`)
  const { data: categories } = await useFetch(`${ config.public.baseURL }${locale.value}/c/categories/`)
  const { data: subcategories } = await useFetch(`${ config.public.baseURL }${locale.value}/c/subcategories/`)

  /// route.params.ct возвращает хрень бывает
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

  const truncateTextByWords = (text,) => {
    return text.split(' ').slice(0, 30).join(' ')
  }

</script>


<template>
  <div class="">

    <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8 pt-4">
      <MainSlider :slides="slides" />
    </div>


    <!-- <div class="container mx-auto lg:max-w-7xl lg:px-8">
      <div class="bg-white pt-4">
        <div class="flex items-center justify-end">
          <div class="flex items-center justify-end gap-8 py-2 px-24 bg-sky-800 bg-slice-left">
            <div class="">
              <a style="font-family: Play;" href="mailto:info@railwelding.com" target="_blank" class="text-white text-lg font-semibold">info@weldingrail.com</a>
            </div>
          </div>
        </div>
      </div>
    </div> -->

    
    <div v-if="category" class="">

      <div class="">
        <div class="container mx-auto px-8 lg:max-w-7xl lg:px-8 ">
          <div class="py-4 bg-white">
            <div class="bg-sky-800 px-8">
              <div class="flex items-center justify-start min-h-20">
                <div class="flex gap-1 text-base font-semibold text-white text-center">
                  <nuxt-link :to="localePath({ name: 'index' })" class="uppercase">{{ $t('main') }}</nuxt-link>
                </div>
                <div v-if="category" class="flex gap-1 text-base font-semibold text-white text-center mdi mdi-chevron-right">
                  <p class="uppercase">{{ category.name }}</p>
                </div>
              </div>            
            </div>            
          </div>
        </div>
      </div>

      <div class="container mx-auto lg:max-w-7xl lg:px-8 ">
        <div class="flex bg-white border-b border-sky-800">
          <div class="bg-sky-800 bg-slice-right px-8">
            <p class="text-2xl text-white font-bold uppercase italic py-2 px-8">{{ category.name }}</p>
          </div>
        </div>
        
      </div>

      <div class="container mx-auto lg:max-w-7xl lg:px-8">

        <div v-if="products.length > 0" class="py-8 px-8 bg-white">

          <div class="grid grid-cols-1 gap-16 py-12">
            <div class="" v-for="product in products" :key="product.id">
              
              <div class="flex gap-20">
                <div class="grid grid-cols-1 gap-4">
                  <img :src="product.image" class="w-[240px]" />
                </div>

                <div class="flex flex-col items-start justify-center gap-8">
                  <div class="py-2">
                    <nuxt-link :to="localePath({ name: 'ct-id', params: { ct: category.url, id: product.id } })" class="text-4xl text-sky-800 font-semibold italic">{{ product.name }}</nuxt-link>
                  </div>                  
                  <div class="flex items-center justify-start gap-4">
                    <button class="min-w-[180px] bg-gradient-to-tr from-sky-800 via-sky-700 to-sky-800 font-semibold text-white text-base py-2 px-4 button-polygon ">{{ $t('requestPrice') }}</button>
                    <nuxt-link :to="localePath({ name: 'ct-id', params: { ct: category.url, id: product.id } })" class="text-base text-sky-800 font-semibold">{{ $t('learnMore') }}</nuxt-link>
                  </div>                  
                </div>

              </div>




              <!-- <div class="">
                <div class="">
                  <div class="">
                    <div class="">
                      <div class="flex items-center justify-center">
                        <img :src="product.image" class="w-[240px]" />
                      </div>
                      <div class="grid grid-cols-1 gap-4 items-center">
                        <div class="flex items-center justify-center">
                          <nuxt-link :to="localePath({ name: 'ct-id', params: { ct: category.url, id: product.id } })" class="text-base text-center text-sky-800 font-bold">{{ product.name }}</nuxt-link>
                        </div>
                        <div class="flex items-center justify-start gap-4">
                          <button class="min-w-[180px] bg-gradient-to-tr from-sky-800 via-sky-700 to-sky-800 font-semibold text-white text-base py-2 px-4 shadow-xl shadow-gray-900/10  ">{{ $t('requestPrice') }}</button>
                          <nuxt-link :to="localePath({ name: 'ct-id', params: { ct: category.url, id: product.id } })" class="text-base text-sky-800 font-semibold">{{ $t('learnMore') }}</nuxt-link>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div> -->



            </div>
          </div>          

        </div>


        <div v-else class="py-8 px-8 bg-white">
          <div class="min-h-[24vh] flex items-center justify-center">
            <div class="flex items-center justify-center py-8">
              <p class="text-sky-900/70">{{ $t('noData') }}</p>
            </div>
          </div>
        </div>

      </div>

      <div class="container mx-auto lg:max-w-7xl lg:px-8">
        
        <div class="bg-white py-8">

          <div class="flex border-b border-sky-800">
            <div class="bg-sky-800 px-20 py-2 bg-slice-right">
              <p class="text-2xl text-white font-semibold uppercase italic">{{ $t('desription') }}</p>
            </div>            
          </div>

          <div v-if="category.description">
            <div v-html="category.description" class="text-sky-800 text-base px-8  py-4"></div>
          </div>
          <div v-else class="">
            <div class="flex items-center justify-center py-8">
              <p class="text-sky-900/70">{{ $t('noDescription') }}</p>
            </div>
          </div>
          
        </div>
        
      </div>


    </div>

    <AppFooter :categories="categories" :subcategories="subcategories" />
  </div>
</template>