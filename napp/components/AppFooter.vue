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
      <div class=" bg-sky-900">

        <div class="flex flex-wrap items-center justify-between py-8">
          <div class="flex flex-wrap items-start gap-14 px-8">
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
              <div class="grid grid-cols-1 gap-y-2 gap-x-14">
                <div v-for="sct in props.subcategories" class="">
                  <p class="text-white">{{ sct.name }}</p>
                </div>
              </div>
            </div>
          </div>
          <div class="">
            <div class="bg-white bg-slice-left px-8 py-2">
              <p class="text-sky-900 text-lg font-bold uppercase italic text-center">{{ $t('subscriebe') }}</p>

              <div id="subscriebe" class="flex items-center gap-0.5 py-2 pl-0.5">
                <div class="border-b border-sky-900">
                  <input type="email" style="font-family: Play;" class="w-[22vw] text-center h-8 px-4 text-base text-sky-900 border border-white/0 focus:border-white/0 focus:ring-gray-600/0 ring-0 placeholder-sky-800" :placeholder="$t('contactus.email')" /> 
                </div>
                <button class="h-8 px-4 text-base uppercase bg-white text-sky-900 shadow-xl shadow-gray-900/10 mdi mdi-send-variant"></button>
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