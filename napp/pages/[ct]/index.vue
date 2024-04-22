<script setup>
  const localePath = useLocalePath()
  const config = useRuntimeConfig()
  const route = useRoute()
  const { locale, setLocale } = useI18n()




  const { data: categories } = await useFetch(`${ config.public.baseURL }${locale.value}/c/categories/`)
  const { data: products } = await useFetch(`${ config.public.baseURL }${locale.value}/c/products/`)


</script>


<template>
  <div class="">

    
    <div class="min-h-screen grid grid-cols-1 content-between">
      <div></div>

      <div class="absolute h-screen   -z-10">
        <img src="/backgrounds/bg-5.webp" class="w-screen h-screen object-cover" />
      </div>

      <div class="">

        <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8">
          <div class="flex">
            <div class="bg-white/50 backdrop-blur-sm px-16 py-4 border-l-8 border-sky-800/90">
              <p class="font-sans font-extrabold text-transparent text-8xl bg-clip-text bg-gradient-to-br from-sky-950 to-sky-800 text-[40px] md:text-[72px] uppercase se lect-none">{{ $t('title-1') }}</p>
              <p class="font-sans font-extrabold text-transparent text-8xl bg-clip-text bg-gradient-to-br from-sky-950 to-sky-600 text-[40px] md:text-[68px] uppercase se lect-none">{{ $t('title-2') }}</p>          
              <div class="py-4">
                <p class="text-xl text-sky-800 se lect-none font-sans">{{ $t('slogan') }}</p>
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
                  <p class="text-white text-4xl my-4">{{ $t('pages.index.chooseUs-title') }}</p>
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



    <div class="h-screen flex items-center justify-center">
    <div class="">
      
      <p class="text-center text-red-800 text-2xl">
        /c/index/
      </p>

      <p class="text-center text-red-800 text-2xl">
        {{ route.params }}
      </p>      
    </div>

  </div>


  </div>
</template>