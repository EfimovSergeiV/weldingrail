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



  const variant = ref(2)


  const message = (message) => {
    alert(message)
  }

</script>


<template>
  <div id="home">

    <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8 pt-4">
      <MainSlider :slides="slides" />
    </div>


    <div id="why-choose-us" class="sec">
      <div class="">
        <div class="">
          <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8">
            <div class="bg-white">
              <div class="grid grid-cols-1 lg:flex items-end justify-between">
                <div class="">
                  
                  <div class=" py-2">
                    <div class="flex border-b border-sky-800">
                      <div class=" px-14 py-2 bg-slice-right bg-sky-800 ">
                        <p class="text-xl text-white font-bold uppercase italic">{{ $t('chooseUS.title') }}</p>
                      </div>                    
                    </div>                    
                  </div>


                  
                  <div class="px-8 py-2 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-x-4 gap-y-2 text-sm md:text-base font-semibold">
                    <div class="flex items-center gap-1 mdi mdi-brightness-1 text-sky-800 uppercase"><p class="text-sm text-sky-800">{{ $t('chooseUS.1') }}</p></div>
                    <div class="flex items-center gap-1 mdi mdi-brightness-1 text-sky-800 uppercase"><p class="text-sm text-sky-800">{{ $t('chooseUS.2') }}</p></div>
                    <div class="flex items-center gap-1 mdi mdi-brightness-1 text-sky-800 uppercase"><p class="text-sm text-sky-800">{{ $t('chooseUS.3') }}</p></div>
                    <div class="flex items-center gap-1 mdi mdi-brightness-1 text-sky-800 uppercase"><p class="text-sm text-sky-800">{{ $t('chooseUS.4') }}</p></div>
                    <div class="flex items-center gap-1 mdi mdi-brightness-1 text-sky-800 uppercase"><p class="text-sm text-sky-800">{{ $t('chooseUS.5') }}</p></div>
                    <div class="flex items-center gap-1 mdi mdi-brightness-1 text-sky-800 uppercase"><p class="text-sm text-sky-800"> {{ $t('chooseUS.6') }}</p></div>
                  </div>                  
                </div>
              </div>
            </div>

            <div class="bg-white py-2">
              <div class="flex items-center justify-end">
                <div class="flex items-center justify-end gap-8 py-2 px-24 bg-sky-800 bg-slice-left">
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
            <div class="grid grid-cols-1 md:grid-cols-2 lg:flex items-center min-h-20 justify-between bg-sky-800 px-8">
              <div class="flex items-center gap-2"><span style="font-family: Play;" class="font-bold text-white text-[32px]">+250</span><p class="text-white text-xl font-semibold"> {{ $t('employees') }}</p></div>
              <div class="flex items-center gap-2"><span style="font-family: Play;" class="font-bold text-white text-[32px]">+300</span><p class="text-white text-xl font-semibold"> {{ $t('projects') }}</p></div>
              <div class="flex items-center gap-2"><span style="font-family: Play;" class="font-bold text-white text-[32px]">+460Ha</span><p class="text-white text-xl font-semibold"> {{ $t('prodArea') }}</p></div>
              <div class="flex items-center gap-2"><span style="font-family: Play;" class="font-bold text-white text-[32px]">+150</span><p class="text-white text-xl font-semibold"> {{ $t('clients') }}</p></div>
            </div>
          </div>
        </div>
      </div>
    </div>





    <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8">
      <div class="flex pt-6 bg-white  border-b border-sky-800">
        <div class="px-8 py-2 bg-slice-right bg-sky-800">
          <p class="text-2xl text-white font-semibold uppercase italic">{{ $t('RWQ') }}</p>
        </div>

        <div class="flex items-center justify-end gap-4">
          <p @click="variant = 1" class="text-sm text-black font-semibold py-1 uppercase cursor-pointer">вариант категории - 1</p>
          <p @click="variant = 2" class="text-sm text-black font-semibold py-1 uppercase cursor-pointer">вариант категории - 2</p>
          <p class="text-sm text-black py-1">( сейчас - {{ variant }} вариант )</p>
        </div>

      </div>

    </div>


    <div id="railwelding-equipment" class="sec container mx-auto px-4 lg:max-w-7xl lg:px-8">
      <div class=" bg-white pt-2">


        <!-- РЕЛЬСОСВАРОЧНОЕ ОБОРУДОВАНИЕ -->
         <div v-if="variant === 1">
          <EquipmentSection1 :categories="categories" />
         </div>
         <div v-else>
          <EquipmentSection2 :categories="categories" :products="products" />
         </div>



        <div v-if="subcategories" class="">
          <div class="mt-4">
            <div class="flex border-b border-sky-800 my-2">
              <div class=" px-8 py-2 bg-slice-right bg-sky-800">
                <p class="text-2xl text-white font-semibold uppercase italic">{{ $t('components') }}</p>
              </div>
            </div>

            <div class="flex flex-wrap gap-x-8 gap-y-4 px-8 pt-4 pb-8 bg-sky-800">
              <div v-for="subct in subcategories" :key="subct.id" class="">
                <div class="">
                  <nuxt-link :to="localePath({ name: 'ct', params: { ct: subct.url } })" class="w-full">
                    <p class="text-xl text-white text-center">{{ subct.name }}</p>
                  </nuxt-link>                    
                </div>
              </div>
            </div>
          </div>
        </div>



      </div>
    </div>






    <div id="about-us" class="sec">
      <div class="container mx-auto lg:max-w-7xl lg:px-8 ">
        <div class=" bg-sky-800">
          <div class="bg-[url('/backgrounds/bg-1.webp')] h-[480px] bg-no-repeat bg-left bg-cover about-polygon">
            <div class="bg-gradient-to-br from-white via-white/90 to-white/70 back drop-blur-sm transition-all duration-1000 h-full relative  ">
              <div class="absolute w-full h-full">

                <div class="flex items-center justify-center h-full">
                  <div class="grid grid-cols-1 gap-8">
                    
                    <div class="flex ">
                      <div class="px-8 py-3 bg-slice-right bg-sky-800">
                        <img src="/logo-white.webp" class="h-8" />
                      </div>                      
                    </div>


                    <div class="grid grid-cols-1 gap-6 px-8">
                      <p class="text-4xl text-sky-800 ">{{ $t('about.text-1') }}</p>
                      <div class="grid grid-cols-1 gap-3">
                        <p class="text-xl text-sky-800 ">{{ $t('about.text-2') }}</p>
                        <p class="text-xl text-sky-800 ">{{ $t('about.text-4') }}</p>                        
                      </div>
                    </div>

                    <div class="flex items-center justify-end gap-4">
                      <div class="">
                        <p class="text-base text-sky-800 py-1 uppercase">{{ $t('about.text-3') }}</p>
                      </div>
                      <div class="flex items-center justify-center gap-0.5 text-sky-800 bg-white bg-slice-left px-8 py-1 cursor-pointer">
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
    </div>







    <div id="write-to-us" class="sec container mx-auto px-4 lg:max-w-7xl lg:px-8">
      <div class="flex items-center justify-center bg-sky-800">
        <div class="px-8 pt-8">
          <div class=" flex items-start justify-center">
            <p class="text-2xl text-white font-bold uppercase italic">{{ $t('contactus.title-1') }}</p>
          </div>
          <div class="flex items-start justify-center">
            <p class="text-xl text-white py-1 uppercase">{{ $t('contactus.title-2') }}</p>
          </div>          
        </div>
      </div>

      <div class="bg-white">
        <div class="bg-sky-800 contactus-polygon">

          <div class=" bg-[url('/backgrounds/10.png')] bg-no-repeat bg-bottom bg-cover">
            <div class="bg-sky-800/70">

              <div class="px-20 grid grid-cols-2 gap-2 pt-8">
                <div class="">
                  <label for="text-1" class="text-sm text-white">{{ $t('contactus.name-title') }}</label>
                  <div class="relative">
                    <!-- <p class="absolute px-2 py-1 mdi mdi-16px mdi-account-tie text-sky-800/90"></p> -->
                    <input type="text" id="text-1" class="bg-gray-50 shadow-lg shadow-black/10 border border-gray-300 focus:border-gray-300 text-gray-900 text-sm focus:ring-blue-500/0 focus:border-blue-500/0 block w-full pl-2 py-1.5 " :placeholder="$t('contactus.name')" />
                  </div>              
                </div>          
                <div class="">
                  <label for="text-2" class="text-sm text-white">{{ $t('contactus.company-title') }}</label>
                  <div class="relative">
                    <!-- <p class="absolute px-2 py-1 mdi mdi-16px mdi-account-tie text-sky-800/90"></p> -->
                    <input type="text" style="font-family: Play;" id="text-2" class="bg-gray-50 shadow-lg shadow-black/10 border border-gray-300 focus:border-gray-300 text-gray-900 text-sm focus:ring-blue-500/0 focus:border-blue-500/0 block w-full pl-2 py-1.5 " :placeholder="$t('contactus.company')" />
                  </div>              
                </div>

                <div style="font-family: Play;" class="">
                  <label for="text-4" class="text-sm text-white">{{ $t('contactus.email-title') }}</label>
                  <div class="relative">
                    <!-- <p class="absolute px-2 py-1 mdi mdi-16px mdi-account-tie text-sky-800/90"></p> -->
                    <input type="text" id="text-4" class="bg-gray-50 shadow-lg shadow-black/10 border border-gray-300 focus:border-gray-300 text-gray-900 text-sm focus:ring-blue-500/0 focus:border-blue-500/0 block w-full pl-2 py-1.5 " :placeholder="$t('contactus.email')" />
                  </div>
                </div>
                  
                <div class="">
                  <label for="text-5" class="text-sm text-white">{{ $t('contactus.land-title') }}</label>
                  <div class="relative">
                    <!-- <p class="absolute px-2 py-1 mdi mdi-16px mdi-account-tie text-sky-800/90"></p> -->
                    <input type="text" id="text-5" style="font-family: Play;" class="bg-gray-50 shadow-lg shadow-black/10 border border-gray-300 focus:border-gray-300 text-gray-900 text-sm focus:ring-blue-500/0 focus:border-blue-500/0 block w-full pl-2 py-1.5 " :placeholder="$t('contactus.land')" />
                  </div>              
                </div>   
              </div>


              <div class="px-20 grid grid-cols-1 gap-4 py-4 ">
                <div class="">
                  <label for="text-6" class="text-sm text-white">{{ $t('contactus.message-title') }}</label>
                  <div class="relative">
                    <!-- <p class="absolute px-2 py-1 mdi mdi-16px mdi-text-long text-sky-800/90"></p> -->
                    <textarea type="text" id="text-6" rows="8" class="bg-gray-50 shadow-lg shadow-black/10 border border-gray-300 focus:border-gray-300 text-gray-900 text-sm focus:ring-blue-500/0 focus:border-blue-500/0 block w-full pl-2 p-1.5 " :placeholder="$t('contactus.message')"></textarea>
                  </div>              
                </div>
              </div>

              <div class="flex items-center justify-end gap-4 px-20 pb-12">
                <div class="flex gap-4">
                  <div class="flex items-center gap-4 max-w-[50rem]">
                    <label for="privacy" class="text-sm text-white text-right">{{ $t('privacy') }}</label> 
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
                    <button class="bg-gradient-to-tr from-white via-gray-100 to-white font-semibold text-sky-800 w-60 py-2 shadow-xl shadow-gray-900/10  ">{{ $t('contactus.send') }}</button>
                  </div>
                </div>
              </div>



            </div>



          </div>


        </div>        
      </div>

    </div>






    <div id="our-partners" class="sec">
      <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8">

        <div class="py-2 px-4 bg-white">
          <div class="flex items-center justify-center">
            <p class="text-xl text-sky-800 font-bold uppercase italic">{{ $t('partners') }}</p>
          </div>

          <div class="grid grid-cols-2 lg:grid-cols-4 gap-2 pt-6">
            <div class="px-8">
              <div class="flex items-center justify-center py-2">
                <img src="/partners/2.png" class="h-12"/>
              </div>
              <div class="flex items-center justify-center py-2">
                <p style="font-family: Play;" class="text-sky-800 text-base">Kazakh Railways</p>
              </div>
            </div>
            <div class="px-8">
              <div class="flex items-center justify-center py-2">
                <img src="/partners/1.png" class="h-12"/>
              </div>
              <div class="flex items-center justify-center py-2">
                <p style="font-family: Play;" class="text-sky-800 text-base">Lithuanian Railways</p>
              </div>
            </div>
            <div class="px-8">
              <div class="flex items-center justify-center py-2">
                <img src="/partners/3.png" class="h-12"/>
              </div>
              <div class="flex items-center justify-center py-2">
                <p style="font-family: Play;" class="text-sky-800 text-base">Ozbekiston temir yollari</p>
              </div>
            </div>
            <div class="px-8">
              <div class="flex items-center justify-center py-2">
                <img src="/partners/4.png" class="h-12"/>
              </div>
              <div class="flex items-center justify-center py-2">
                <p style="font-family: Play;" class="text-sky-800 text-base">Belarusian railways</p>
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
                  <div class="bg-white h-[48px] w-[48px] rounded-full border-2 border-sky-800">
                    <div class="flex items-center justify-center h-full w-full">
                      <p @click="showParams = null" class="mdi mdi-36px mdi-window-close cursor-pointer text-sky-800"></p>
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
                <button class="bg-gradient-to-tr from-gray-100 via-white to-gray-100 font-semibold text-sky-800 text-base w-60 shadow-xl shadow-gray-900/10 px-6 py-2 my-2  ">Запросить стоимость</button>
              </div>

            </div>
        
          </div>
        </div>

      </div>      
    </transition>



    <AppFooter :categories="categories" :subcategories="subcategories" />
  </div>
</template>


