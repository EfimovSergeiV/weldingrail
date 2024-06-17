<script setup>
  const localePath = useLocalePath()
  const config = useRuntimeConfig()
  const route = useRoute()
  const { locale, setLocale } = useI18n()



  const { data: slides } = await useFetch(`${ config.public.baseURL }${locale.value}/d/slides/`)
  const { data: categories } = await useFetch(`${ config.public.baseURL }${locale.value}/c/categories/`)
  const { data: subcategories } = await useFetch(`${ config.public.baseURL }${locale.value}/c/subcategories/`)
  const { data: products } = await useFetch(`${ config.public.baseURL }${locale.value}/c/products/`)


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
  <div>

    <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8 pt-4">
      <MainSlider :slides="slides" />
    </div>


    <div class="">
      <div class="">
        <div class="">
          <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8">
            <div class="bg-white py-8 px-4">
              <div class="grid grid-cols-1 lg:flex items-end justify-between">
                <div class="">
                  <p class="text-xl text-white font-bold uppercase italic">{{ $t('chooseUS.title') }}</p>
                  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 text-sm md:text-base font-semibold">
                    <div class="flex items-center gap-1 mdi mdi-brightness-1 text-sky-800 uppercase"><p class="text-sm text-sky-800">{{ $t('chooseUS.1') }}</p></div>
                    <div class="flex items-center gap-1 mdi mdi-brightness-1 text-sky-800 uppercase"><p class="text-sm text-sky-800">{{ $t('chooseUS.2') }}</p></div>
                    <div class="flex items-center gap-1 mdi mdi-brightness-1 text-sky-800 uppercase"><p class="text-sm text-sky-800">{{ $t('chooseUS.3') }}</p></div>
                    <div class="flex items-center gap-1 mdi mdi-brightness-1 text-sky-800 uppercase"><p class="text-sm text-sky-800">{{ $t('chooseUS.4') }}</p></div>
                    <div class="flex items-center gap-1 mdi mdi-brightness-1 text-sky-800 uppercase"><p class="text-sm text-sky-800">{{ $t('chooseUS.5') }}</p></div>
                    <div class="flex items-center gap-1 mdi mdi-brightness-1 text-sky-800 uppercase"><p class="text-sm text-sky-800"> {{ $t('chooseUS.6') }}</p></div>
                  </div>                  
                </div>
                <div class="grid grid-cols-1 gap-2 text-right">
                  <div class="">
                    <a href="mailto:info@railwelding.com" target="_blank" class="text-sky-900 text-lg font-semibold">info@weldingrail.com</a>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="">
          <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8">
            <div class="grid grid-cols-1 md:grid-cols-2 lg:flex items-center min-h-20 justify-between bg-sky-900   px-8">

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
      <div class="min-h-[60vh] flex items-center justify-center bg-white">
        <div class="grid grid-cols-1 gap-2">
          <p class="text-center text-4xl text-sky-900 font-bold uppercase italic my-4">Страница не найдена</p>
          <nuxt-link :to="localePath('index')" class="text-center text-2xl text-sky-900">Вернуться на главную</nuxt-link>
        </div>
      </div>      
    </div>



    <AppFooter :categories="categories" :subcategories="subcategories" />
  </div>

  <!-- <div class="h-screen flex items-center justify-center">
    <div class="">
      
      <p class="text-center text-red-800 text-2xl">
        ERROR 404: Page not found
      </p>

      <p class="text-center text-red-800 text-2xl">
        {{ route }}
      </p>      
    </div>

  </div> -->
</template>