<script setup>
  const localePath = useLocalePath()
  const config = useRuntimeConfig()
  const props = defineProps(['categories', 'subcategories'])

  const { locale, setLocale } = useI18n()
  const currentData = new Date().getFullYear()

  const moveUp = () => {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  }

  const { data: categories } = await useFetch(`${ config.public.baseURL }${locale.value}/c/categories/`)

</script>


<template>
  <div>

    <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8">
      <div class=" bg-sky-900 px-8">        
        <div class="flex items-start justify-start gap-24 h-full py-8">


          <div class="">
            <div class="pb-2">
              <p class="text-white uppercase font-semibold text-lg italic">{{ $t('RWQ')}}</p>
            </div>
            
            <div class="grid grid-cols-1 gap-y-2 gap-x-14">
              <div v-for="ct in props.categories" class="">
                <p class="text-white">{{ ct.name }}</p>
              </div>
            </div>
          </div>



          <div class="">
            <div class="pb-2">
              <p class="text-white uppercase font-semibold text-lg italic">{{ $t('components')}}</p>
            </div>
            
            <div class="grid grid-cols-2 gap-y-2 gap-x-14">
              <div v-for="sct in props.subcategories" class="">
                <p class="text-white">{{ sct.name }}</p>
              </div>
            </div>
          </div>
        </div>


        <div class="flex items-end justify-end py-2">
          <div class="flex items-center justify-center">
            <div class="grid grid-cols-1 gap-1">
              <p class="text-white text-xl font-bold uppercase italic">{{ $t('subscriebe') }}</p>
              <!-- <p class="text-white text-base ">Будьте первым, кто узнает последние новости о тенденциях в сварочных технологиях!</p> -->
              <div id="subscriebe" class="flex items-center gap-0.5 py-2">
                <input type="email" style="font-family: Play;" class=" w-[22vw] text-center h-8 px-4 text-base text-sky-900 bg-white border border-white/0 focus:border-white/0 focus:ring-gray-600/0 ring-0 placeholder-sky-800" :placeholder="$t('contactus.email')" /> 
                <button class="h-8 px-4 text-base uppercase bg-white text-sky-900 shadow-xl shadow-gray-900/10 mdi mdi-send-variant"></button>
              </div>

              <div class="flex items-start gap-2 hidden">
                <input 
                  id="privacy"
                  type="checkbox"
                  class="w-4 h-4 mt-1
                    rounded text-gray-700 focus:ring-0 
                    focus:ring-gray-300 ring-offset-gray-300 bg-gray-700 border-gray-300
                    dark:focus:ring-gray-700 dark:ring-offset-gray-800 dark:bg-gray-700 dark:border-gray-700" 
                />
                
                <label for="privacy" class="text-xs text-white max-w-[30vw]">{{ $t('privacy') }}</label>              

              </div>

            </div>
          </div>          
        </div>









      </div>
    </div>

    <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8">
      <div class=" bg-gradient-to-br from-sky-950 via-sky-900 to-sky-950 min-h- screen grid grid-cols-1 content-center border-t border-white/20">
        <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8">
          <div class="">
            <div class="flex items-end justify-between py-4">
              <img @click="moveUp()" src="/logo-white.webp" class="h-6 cursor-pointer"/>
              <p style="font-family: Play;" class="text-xs text-gray-100">weldingrail.com | {{ currentData }} (c)</p>
            </div>
          </div>
        </div>
      </div>      
    </div>


  </div>
</template>