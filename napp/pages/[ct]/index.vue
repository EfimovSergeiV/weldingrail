<script setup>
  const localePath = useLocalePath()
  const config = useRuntimeConfig()
  const route = useRoute()
  const { locale, setLocale } = useI18n()
  const router = useRouter()

  const { data: categories } = await useFetch(`${ config.public.baseURL }${locale.value}/c/categories/`)
  const { data: products } = await useFetch(`${ config.public.baseURL }${locale.value}/c/products/`)

  const currentCategory = ref(null)

  if (route.params.ct) {
    currentCategory.value = categories.value.find(category => category.url === route.params.ct)
  }

</script>


<template>
  <div class="">

    
    <div class="min-h-screen grid grid-cols-1 content-between">
      <div class="h-[48px]"></div>

      <div class="relative">
        <img src="/slides/1.webp" alt="logo" class="" />
        <div class="absolute bottom-0 left-0 w-full h-full ">
          <div class="container mx-auto lg:max-w-7xl lg:px-8 h-full">
            <div class="h-full flex items-center justify-center">
              <p class="text-6xl">hallo </p>
            </div>
            
          </div>
          
        </div>
      </div>


      <div id="breadcrumbs" class="bg-gray-300 grid grid-cols-1 content-center ">
        <div class="container mx-auto lg:max-w-7xl lg:px-8">
          <div class="my-4">
              <div class="flex items-center justify-start">
                <div class="flex gap-1 text-sm font-semibold text-sky-950 text-center"><nuxt-link :to="localePath({ name: 'index' })" class="uppercase">Главная</nuxt-link></div>
                <!-- BUG: ошибка не найденного URL -->
                <div v-if="currentCategory" class="flex gap-1 text-sm font-semibold text-sky-950 text-center mdi mdi-chevron-double-right"><nuxt-link :to="localePath({ name: 'ct', params: { ct: currentCategory.url } })" class="uppercase">{{ currentCategory.name }}</nuxt-link></div>
              </div>
            </div>
        </div>
      </div>


      <div class="h-screen flex items-center justify-center">
        <div class="">
          
          <p class="text-center text-red-800 text-2xl">
            /c/index/
          </p>

          <p class="text-center text-sky-950 text-2xl uppercase font-semibold">тут товары категории</p> 
          
          

          <p class="text-center text-red-800 text-2xl">
            {{ route.params }}
          </p>      
        </div>

      </div>
      
    </div>


  </div>
</template>