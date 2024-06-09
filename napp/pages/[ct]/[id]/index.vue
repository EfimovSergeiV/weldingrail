<script setup>

  const config = useRuntimeConfig()
  const route = useRoute()
  const router = useRouter()
  const localePath = useLocalePath()
  const { locale, setLocale } = useI18n()


  const { data: slides } = await useFetch(`${ config.public.baseURL }${locale.value}/d/slides/`)
  const { data: categories } = await useFetch(`${ config.public.baseURL }${locale.value}/c/categories/`)
  const { data: subcategories } = await useFetch(`${ config.public.baseURL }${locale.value}/c/subcategories/`)
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


    <div class="">
      <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8 ">
        <div class="py-4 bg-white">
          <div class="bg-sky-700 px-8">
            <div class="grid grid-cols-1 md:grid-cols-2 lg:flex items-center min-h-20 justify-between">
              <div class="flex items-center justify-start">
                <div class="flex items-center justify-start">
                  <div class="flex gap-1 text-base font-semibold text-white text-center"><nuxt-link :to="localePath({ name: 'index' })" class="uppercase">{{ $t('main') }}</nuxt-link></div>
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
      <div class="flex items-center gap-8 bg-white pt-8">
        <div class=" flex-none px-8">
          <img :src="product.image" class="w-[290px]" />
        </div>
        <div class="grid grid-cols-1 gap-6 w-full">
          <div class="">
            <p class="text-4xl text-sky-700 font-bold uppercase italic">{{ product.name }}</p>
          </div>


          <div class="bg-white py-2">

            <div class="flex items-center justify-end border-b border-sky-700">
              <div class="bg-slice-left bg-sky-700 py-2 px-32">
                <p class="text-lg text-white font-semibold uppercase italic">{{ $t('requestPrice') }}</p>
              </div>
            </div>

            <div class="px-8 ">

              <div class="grid grid-cols-2 gap-x-4 gap-y-2 py-8 ">
                <div class="">
                  <label for="text-1" class="text-sm text-sky-700">{{ $t('contactus.name-title') }}</label>
                  <div class="relative">
                    <!-- <p class="absolute px-2 py-1 mdi mdi-16px mdi-account-tie text-sky-700/90"></p> -->
                    <input type="text" id="text-1" class="bg-gray-50 shadow-lg shadow-black/10 border border-gray-300 focus:border-gray-300 text-gray-900 text-sm focus:ring-blue-500/0 focus:border-blue-500/0 block w-full pl-2 py-1.5 " :placeholder="$t('contactus.name')" />
                  </div>              
                </div>

                <div class="">
                  <label for="text-2" class="text-sm text-sky-700">{{ $t('contactus.company-title') }}</label>
                  <div class="relative">
                    <!-- <p class="absolute px-2 py-1 mdi mdi-16px mdi-account-tie text-sky-700/90"></p> -->
                    <input type="text" style="font-family: Play;" id="text-2" class="bg-gray-50 shadow-lg shadow-black/10 border border-gray-300 focus:border-gray-300 text-gray-900 text-sm focus:ring-blue-500/0 focus:border-blue-500/0 block w-full pl-2 py-1.5 " :placeholder="$t('contactus.company')" />
                  </div>              
                </div>

                <div style="font-family: Play;" class="">
                  <label for="text-4" class="text-sm text-sky-700">{{ $t('contactus.email-title') }}</label>
                  <div class="relative">
                    <!-- <p class="absolute px-2 py-1 mdi mdi-16px mdi-account-tie text-sky-700/90"></p> -->
                    <input type="text" id="text-4" class="bg-gray-50 shadow-lg shadow-black/10 border border-gray-300 focus:border-gray-300 text-gray-900 text-sm focus:ring-blue-500/0 focus:border-blue-500/0 block w-full pl-2 py-1.5 " :placeholder="$t('contactus.email')" />
                  </div>              
                </div>

                <div class="">
                  <label for="text-5" class="text-sm text-sky-700">{{ $t('contactus.land-title') }}</label>
                  <div class="relative">
                    <!-- <p class="absolute px-2 py-1 mdi mdi-16px mdi-account-tie text-sky-700/90"></p> -->
                    <input style="font-family: Play;" type="text" id="text-5" class="bg-gray-50 shadow-lg shadow-black/10 border border-gray-300 focus:border-gray-300 text-gray-900 text-sm focus:ring-blue-500/0 focus:border-blue-500/0 block w-full pl-2 py-1.5 " :placeholder="$t('contactus.land')" />
                  </div>              
                </div>

              </div>


              <div class="flex gap-4 items-center justify-end py-4">

                <div class="flex items-center gap-4 ">
                  <label for="privacy" class="text-xs text-sky-700 text-right">
                    {{ $t('privacy') }}
                  </label>              
                  <input 
                    id="privacy"
                    type="checkbox"
                    class="w-4 h-4 
                      rounded text-gray-700 focus:ring-0 
                      focus:ring-gray-300 ring-offset-gray-300 bg-gray-700 border-gray-300
                      dark:focus:ring-gray-700 dark:ring-offset-gray-800 dark:bg-gray-700 dark:border-gray-700" 
                    />
                </div>

                <div class="flex items-end justify-end">
                  <button class="bg-gradient-to-tr from-sky-700 via-sky-600 to-sky-700 font-semibold text-white text-base w-60 py-2 shadow-xl shadow-gray-900/10  ">{{ $t('send') }}</button>
                </div>
              </div>

            </div>
          </div>


        </div>
      </div>
    </div>


    <div class="container mx-auto lg:max-w-7xl lg:px-8">
      <div class="bg-white py-8">
        <div class="flex  border-b border-sky-700">
          <div class="bg-sky-700 px-32 py-2 bg-slice-right">
            <p class="text-2xl text-white font-semibold uppercase italic">{{ $t('desription') }}</p>
          </div>
          
        </div>
        <div class=" px-8 py-4">
          <div v-if="product.description.length > 1" v-html="product.description" class="text-sky-700 text-base"></div>
          <div v-else class="">
            <div v-for="category in categories" :key="category.id" class="text-sky-700 text-base">
              <div v-if="category.id === product.category" class="" v-html="category.description"></div>
            </div>
          </div>
        </div>
      </div>
    </div>


    <div v-if="true" class="">

      <div class=" grid grid-cols-1 content-center">
        <div id="product-property" class="container mx-auto lg:max-w-7xl lg:px-8">
          <div class=" bg-white flex gap-8 py-8 ">
            


            <div class="w-full text-sm">
              <div class="flex border-b border-sky-700">
                <div class=" bg-sky-700 px-20 py-2 bg-slice-right flex">
                  <p class="text-2xl text-white font-semibold uppercase italic">{{ $t('specifications') }}</p>
                </div>                
              </div>



              <div class="px-8 grid grid-cols-1 gap-2 py-4">
                <div v-for="propdata in product.product_properties" :key="propdata.id" class="">
                  <div v-if="propdata.value" class="">
                    <div class="flex items-center justify-between text-base border-b border-sky-700/30 hover:border-sky-700/50 transition-all duration-300">
                      <p class="text-sky-700 se lect-none font-sans">{{ propdata.name }}</p>
                      <p class="text-sky-700 se lect-none font-sans font-semibold">{{ propdata.value }}</p>
                    </div>                
                  </div>
                  <div v-else class="">
                    <div class="flex items-center justify-start text-base mt-6">
                      <p class="text-sky-700 se lect-none font-sans font-semibold">{{ propdata.name }}</p>
                    </div>
                  </div>

                </div>
              </div>            
            </div>


            <div class=" w-1/3 hidden">
              <div class="my-2">
                <p class="text-xl text-sky-700 se lect-none font-sans font-semibold uppercase">Материалы:</p>
              </div>
              
              <div class="py-2 ">
                <div class="grid grid-cols-1 gap-2 text-sky-700">
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

          </div>
        </div>
      </div>



      <div v-if="product.product_advantages.length > 0" class=" bg-sky-700 grid grid-cols-1 content-center py-4 border-t border-black/10">
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


    <AppFooter :categories="categories" :subcategories="subcategories" />
  </div>
</template>