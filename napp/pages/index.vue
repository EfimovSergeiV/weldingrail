<script setup>
  const localePath = useLocalePath()
  const config = useRuntimeConfig()
  const route = useRoute()
  const { locale, setLocale } = useI18n()



  const { data: slides } = await useFetch(`${ config.public.baseURL }${locale.value}/d/slides/`)
  const { data: categories } = await useFetch(`${ config.public.baseURL }${locale.value}/c/categories/`)
  const { data: subcategories } = await useFetch(`${ config.public.baseURL }${locale.value}/c/subcategories/`)
  const { data: products } = await useFetch(`${ config.public.baseURL }${locale.value}/c/products/`)


  const showParams = ref(null)
  const ctSelect = ref(1)

</script>


<template>
  <div>

    <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8 pt-4">
      <MainSlider :slides="slides" />
    </div>


    <div class="">
      <div class="">
        <div class="">
          <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8">
            <div class="bg-white px-8">
              <div class="grid grid-cols-1 lg:flex items-end justify-between">
                <div class="">
                  <p class="text-2xl text-sky-700 font-bold uppercase italic my-4">{{ $t('chooseUS.title') }}</p>
                  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-x-4 gap-y-2 text-sm md:text-base font-semibold">
                    <div class="flex items-center gap-1 mdi mdi-brightness-1 text-sky-700 uppercase"><p class="text-sm text-sky-700">{{ $t('chooseUS.1') }}</p></div>
                    <div class="flex items-center gap-1 mdi mdi-brightness-1 text-sky-700 uppercase"><p class="text-sm text-sky-700">{{ $t('chooseUS.2') }}</p></div>
                    <div class="flex items-center gap-1 mdi mdi-brightness-1 text-sky-700 uppercase"><p class="text-sm text-sky-700">{{ $t('chooseUS.3') }}</p></div>
                    <div class="flex items-center gap-1 mdi mdi-brightness-1 text-sky-700 uppercase"><p class="text-sm text-sky-700">{{ $t('chooseUS.4') }}</p></div>
                    <div class="flex items-center gap-1 mdi mdi-brightness-1 text-sky-700 uppercase"><p class="text-sm text-sky-700">{{ $t('chooseUS.5') }}</p></div>
                    <div class="flex items-center gap-1 mdi mdi-brightness-1 text-sky-700 uppercase"><p class="text-sm text-sky-700"> {{ $t('chooseUS.6') }}</p></div>
                  </div>                  
                </div>
              </div>
            </div>

            <div class="bg-white py-2">
              <div class="flex items-center justify-end">
                <div class="flex items-center justify-end gap-8 py-2 px-24 bg-sky-700 bg-slice-left">
                  <div class="">
                    <a style="font-family: Play;" href="mailto:info@railwelding.com" target="_blank" class="text-white text-lg font-semibold">info@weldingrail.com</a>
                  </div>
                </div>                
              </div>

            </div>

          </div>
        </div>



        <div class="">
          <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8">
            <div class="grid grid-cols-1 md:grid-cols-2 lg:flex items-center min-h-20 justify-between bg-sky-700 px-8">
              <div class="flex items-center gap-4"><span style="font-family: Play;" class="font-bold text-white text-[36px]">+250</span><p class="text-white text-xl font-semibold"> {{ $t('employees') }}</p></div>
              <div class="flex items-center gap-4"><span style="font-family: Play;" class="font-bold text-white text-[36px]">+300</span><p class="text-white text-xl font-semibold"> {{ $t('projects') }}</p></div>
              <div class="flex items-center gap-4"><span style="font-family: Play;" class="font-bold text-white text-[36px]">+460Ha</span><p class="text-white text-xl font-semibold"> {{ $t('prodArea') }}</p></div>
              <div class="flex items-center gap-4"><span style="font-family: Play;" class="font-bold text-white text-[36px]">+150</span><p class="text-white text-xl font-semibold"> {{ $t('clients') }}</p></div>
            </div>
          </div>
        </div>
      </div>
    </div>





    <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8">
      <div class=" bg-white">
        <div class="py-8 px-8">
          <p class="text-4xl text-sky-700 font-semibold uppercase italic">{{ $t('RWQ') }}</p>
        </div>
      </div>
    </div>


    <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8">
      <div class=" bg-white">



        <div class="grid grid-cols-2 gap-4">
          <div class="" v-for="ct in categories" :key="ct.id">
            <div class="relative">
              <img src="/backgrounds/10.jpg" class="h-[240px] w-full" />
              <div class="absolute bg-sky-700/80 hover:bg-sky-800/90 transition-all duration-300 h-full w-full top-0 left-0">
                <div class="flex items-center justify-center h-full">
                  <nuxt-link :to="localePath({ name: 'ct', params: { ct: ct.url } })" class="">
                    <p class="text-white text-2xl font-bold uppercase italic cursor-pointer">{{ ct.name }}</p>
                  </nuxt-link>
                </div>
              </div>
            </div>
          </div>
        </div>




        <div v-if="subcategories" class="">
          <div class="py-8">

            <div class="flex border-b border-sky-700">
              <div class=" px-8 py-2 bg-slice-right bg-sky-700">
                <p class="text-2xl text-white font-semibold uppercase italic">{{ $t('components') }}</p>
              </div>              
            </div>


            <div class="flex flex-wrap gap-x-8 gap-y-4 px-8 py-8">
              <div v-for="subct in subcategories" :key="subct.id" class="">
                <div class="">
                  <nuxt-link :to="localePath({ name: 'ct', params: { ct: subct.url } })" class="w-full">
                    <p class="text-xl text-sky-700 font-semibold">{{ subct.name }}</p>
                  </nuxt-link>                    
                </div>
              </div>
            </div>
          </div>

        </div>

      </div>  

    </div>






    <div class="">
      <div class="container mx-auto lg:max-w-7xl lg:px-8">

        <div class="bg-[url('/backgrounds/bg-1.webp')] h-[400px] bg-no-repeat bg-left bg-cover  ">
          <div class="bg-gradient-to-br from-sky-800/90 via-sky-700/70 to-sky-800/80 backdrop-blur-sm transition-all duration-1000 h-full relative  ">
            <div class="absolute w-full h-full">

              <div class="flex items-center justify-center h-full">
                <div class="grid grid-cols-1 gap-10">
                  <div class="grid grid-cols-1 gap-6 px-8">
                    
                    <div class="py-4">
                      <img src="/logo-white.webp" class="h-8" />
                    </div>
                    
                    <p class="text-2xl text-white ">{{ $t('about.text-1') }}</p>
                    <p class="text-xl text-white ">{{ $t('about.text-2') }}</p>

                  </div>

                  <div class="flex items-center justify-end gap-4">
                    <div class="">
                      <p class="text-base text-white py-1 font-semibold uppercase">{{ $t('contactus.title-2') }}</p>
                    </div>
                    <div class="flex items-center justify-center gap-0.5 text-sky-700 bg-white bg-slice-left px-8 py-1 cursor-pointer">
                      <div class="mdi mdi-24px mdi-download"></div>
                      <p class="text-base font-semibold uppercase ">{{ $t('getCatalog') }}</p>
                    </div>
                  </div>

                </div>




              </div>




            </div>
          </div>
        </div>

      </div>
    </div>





    <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8">

      <div class="grid grid-cols-1">

        <div class="py-8 px-4 bg-white">
          <div class=" flex items-start justify-center">
            <p class="text-2xl text-sky-700 font-bold uppercase italic ">{{ $t('contactus.title-1') }}</p>
          </div>

          <div class=" flex items-start justify-center">
            <p class="text-xl text-sky-700 py-1 uppercase">{{ $t('contactus.title-2') }}</p>
          </div>          
        </div>

        <div class="px-8 bg-white">
          <div class="grid grid-cols-2 gap-y-2 gap-x-6">
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
                <input type="text" id="text-5" style="font-family: Play;" class="bg-gray-50 shadow-lg shadow-black/10 border border-gray-300 focus:border-gray-300 text-gray-900 text-sm focus:ring-blue-500/0 focus:border-blue-500/0 block w-full pl-2 py-1.5 " :placeholder="$t('contactus.land')" />
              </div>              
            </div>              

          </div>


          <div class="grid grid-cols-1 gap-4 py-4 ">
          
            <div class="">
              <label for="text-6" class="text-sm text-sky-700">{{ $t('contactus.message-title') }}</label>
              <div class="relative">
                <!-- <p class="absolute px-2 py-1 mdi mdi-16px mdi-text-long text-sky-700/90"></p> -->
                <textarea type="text" id="text-6" rows="8" class="bg-gray-50 shadow-lg shadow-black/10 border border-gray-300 focus:border-gray-300 text-gray-900 text-sm focus:ring-blue-500/0 focus:border-blue-500/0 block w-full pl-2 p-1.5 " :placeholder="$t('contactus.message')"></textarea>
              </div>              
            </div>
          </div>

        </div>


        <div class="flex items-center justify-end gap-4 bg-white px-8">
          <div class="flex gap-4">
            <div class="flex items-center gap-4 max-w-[50rem]">
              <label for="privacy" class="text-sm text-sky-700 text-right">{{ $t('privacy') }}</label> 
              <input 
                id="privacy"
                type="checkbox"
                class="w-4 h-4 
                  rounded text-gray-700 focus:ring-0 
                  focus:ring-gray-300 ring-offset-gray-300 bg-gray-700 border-gray-300
                  dark:focus:ring-gray-700 dark:ring-offset-gray-800 dark:bg-gray-700 dark:border-gray-700" 
                />
            </div>
          </div>
          <div class="">
            <div class="flex items-center justify-end">
              <button class="bg-gradient-to-tr from-sky-700 via-sky-600 to-sky-700 font-semibold text-white w-60 py-2 shadow-xl shadow-gray-900/10  ">{{ $t('contactus.send') }}</button>
            </div>
          </div>
        </div>

      </div>
    </div>


    <div class="">
      <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8">

        <div class="py-4 px-4 bg-white">
          <div class="flex items-center justify-center py-6">
            <p class="text-xl text-sky-700 font-bold uppercase italic">{{ $t('partners') }}</p>
          </div>

          <div class="grid grid-cols-2 lg:grid-cols-4 gap-2">
            <div class="px-8">
              <div class="flex items-center justify-center py-2">
                <img src="/partners/2.png" class="h-12"/>
              </div>
              <div class="flex items-center justify-center py-2">
                <p style="font-family: Play;" class="text-sky-700 text-base">Kazakh Railways</p>
              </div>
            </div>
            <div class="px-8">
              <div class="flex items-center justify-center py-2">
                <img src="/partners/1.png" class="h-12"/>
              </div>
              <div class="flex items-center justify-center py-2">
                <p style="font-family: Play;" class="text-sky-700 text-base">Lithuanian Railways</p>
              </div>
            </div>
            <div class="px-8">
              <div class="flex items-center justify-center py-2">
                <img src="/partners/3.png" class="h-12"/>
              </div>
              <div class="flex items-center justify-center py-2">
                <p style="font-family: Play;" class="text-sky-700 text-base">Ozbekiston temir yollari</p>
              </div>
            </div>
            <div class="px-8">
              <div class="flex items-center justify-center py-2">
                <img src="/partners/4.png" class="h-12"/>
              </div>
              <div class="flex items-center justify-center py-2">
                <p style="font-family: Play;" class="text-sky-700 text-base">Belarusian railways</p>
              </div>
            </div>
          </div>          
        </div>

      </div>
    </div>



    <transition name="slide-up">
      <div v-if="showParams" class="fixed bottom-0 left-0 w-full z-50">
        <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8 pt-4">
          <div class="bg-sky-900 min-h-[40vh] rounded-t-3xl border border-sky-900 shadow-4xl shadow-black">
            
            <div class="px-6 pt-4 pb-2">
              
              <div class="grid grid-cols-1 gap-6 border-b-2 border-white mb-2">
                <div class="flex items-center justify-between">
                  <p class="text-4xl text-white font-bold uppercase italic">{{showParams.name}}</p> 
                  <div class="bg-white h-[48px] w-[48px] rounded-full border-2 border-sky-700">
                    <div class="flex items-center justify-center h-full w-full">
                      <p @click="showParams = null" class="mdi mdi-36px mdi-window-close cursor-pointer text-sky-700"></p>
                    </div>
                  </div>
                </div>
                
                <p class="text-2xl text-white font-bold uppercase italic">характеристики машины</p>             
              </div>

              
              <div class="pr-2 py-4 text-white h-[40vh] overflow-y-auto">
                <div class="grid grid-cols-1 gap-2">
                  <div v-for="prop in showParams.product_properties" :key="i" class="">
                    <div v-if="prop.value" class="flex items-center gap-6 justify-between border-b border-white/50">
                      <p class="">{{ prop.name }}</p>
                      <p class="">{{ prop.value }}</p>                      
                    </div>
                    <div v-else class="mt-4">
                      <p class="uppercase font-bold">{{ prop.name }}</p>
                      <p class=""></p>                      
                    </div>                    

                  </div>                
                </div>
              </div>
              
              <div class="flex items-center justify-end pt-4">
                <button class="bg-gradient-to-tr from-gray-100 via-white to-gray-100 font-semibold text-sky-700 text-base w-60 shadow-xl shadow-gray-900/10 px-6 py-2 my-2  ">Запросить стоимость</button>
              </div>

            </div>
        
          </div>
        </div>

      </div>      
    </transition>



    <AppFooter :categories="categories" :subcategories="subcategories" />
  </div>
</template>


