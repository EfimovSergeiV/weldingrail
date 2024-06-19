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

</script>


<template>
  <div>

    <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8 ">
      <div class="bg-white">
        <div class="bg-[url('/backgrounds/10.jpg')] bg-no-repeat bg-bottom bg-cover footer-polygon">
          <div class=" bg-sky-900/80">

            <div class="flex flex-wrap items-center justify-between py-14">
              <div class="flex flex-wrap items-start gap-14 px-8">
                <div class="">
                  <div class="pb-2">
                    <p class="text-white uppercase  font-semibold text-lg italic border-b border-white/80">{{ $t('RWQ')}}</p>
                  </div>
                  <div class="grid grid-cols-1 gap-y-2 gap-x-14">
                    <div v-for="ct in props.categories" class="">
                      <nuxt-link :to="localePath({ name: 'ct', params: { ct: ct.url } })" class="text-gray-300 cursor-pointer hover:text-orange-400 transition-all duration-300">{{ ct.name }}</nuxt-link>
                    </div>
                  </div>
                </div>
                <div class="">
                  <div class="pb-2">
                    <p class="text-white uppercase font-semibold text-lg italic border-b border-white/80">{{ $t('components')}}</p>
                  </div>
                  <div class="grid grid-cols-1 gap-y-2 gap-x-14">
                    <div v-for="sct in props.subcategories" class="">
                      <nuxt-link :to="localePath({ name: 'ct', params: { ct: sct.url } })" class="text-gray-300 cursor-pointer hover:text-orange-400 transition-all duration-300">{{ sct.name }}</nuxt-link>
                    </div>
                  </div>
                </div>
              </div>
              <div class="">
                <div class="bg-sky-800/90 bg-slice-left border-y  border-white/50 px-6 py-6 min-w-[400px]">
                  <p class="text-white text-lg font-bold uppercase italic text-center">{{ $t('subscriebe') }}</p>

                  <div id="subscriebe" class="flex items-center justify-center w-full gap-4 py-2 pl-4">
                    <div class=" w-full ">
                      <input id="subs-form" type="email" style="font-family: Play;" class="w-full text-center h-8 px-4 text-base text-sky-900 border border-white/0 focus:border-white/0 focus:ring-gray-600/0 ring-0 placeholder-sky-800" :placeholder="$t('contactus.email')" /> 
                    </div>

                  </div>
                  <div class="flex items-center justify-center mt-1">
                    <button class="h-7 px-6 text-base text-white hover:text-orange-400 transition-all duration-300 ">
                      <p class="">{{ $t('subscribe') }}</p>
                    </button>                   
                  </div>
                </div>

                <!-- <div class="">
                  <div class="flex items-center justify-end mt-2 py-2 px-8 ">
                    <a style="font-family: Play;" href="mailto:info@railwelding.com" target="_blank" class="text-white text-center text-lg ">info@weldingrail.com</a>
                  </div>                
                </div> -->


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
              <div class="grid grid-cols-1 gap-1">
                <p style="font-family: Play;" class="text-xs text-gray-100">weldingrail.com | {{ currentData }} (c)</p>
                <!-- <a style="font-family: Play;" href="mailto:info@railwelding.com" target="_blank" class="text-white text-right text-xs">info@weldingrail.com</a> -->
              </div>
              
            </div>
          </div>
        </div>
      </div>      
    </div>


  </div>
</template>