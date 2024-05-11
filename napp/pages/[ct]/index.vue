<script setup>
  const localePath = useLocalePath()
  const config = useRuntimeConfig()
  const route = useRoute()
  const { locale, setLocale } = useI18n()
  const router = useRouter()

  const { data: categories } = await useFetch(`${ config.public.baseURL }${locale.value}/c/categories/`)
  const products = ref(null)

  const currentCategory = ref(null)

  if (route.params.ct) {
    currentCategory.value = categories.value.find(category => category.url === route.params.ct)
    products.value = await $fetch(`${ config.public.baseURL }${locale.value}/c/products/${ currentCategory.value.id }/`)
  }

</script>


<template>
  <div class="">

    
    <div class="">


      <div class="relative">
        <img src="/slides/3.webp" alt="logo" class="" />
        <div class="absolute bottom-0 left-0 w-full h-full ">
          <div class="container mx-auto lg:max-w-7xl lg:px-8 h-full">
            <div class="h-full flex items-center justify-start">
              
              <div class="">
                <p class="text-4xl text-white">Мобильные рельсосварочные комплексы </p>
                <div class="hidden md:block">
                  <div v-for="text, pk in ['Предназначены для контактной стыковой сварки в полевых условиях', 'Оборудование компактно размещается в небольшом 20-футовом контейнере.']" :key="pk" class="flex" >
                    <div :id="pk" class="bg-white/60 p-2 my-0.5">
                      <p class="text-sky-900 font-semibold text-base">{{ text }}</p>
                    </div>
                  </div>                  
                </div>
              </div>
            
            
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
                <div v-if="currentCategory" class="flex gap-1 text-sm font-semibold text-sky-950 text-center mdi mdi-chevron-double-right"><p class="uppercase">{{ currentCategory.name }}</p></div>
              </div>
            </div>
        </div>
      </div>



      <div class="container mx-auto lg:max-w-7xl lg:px-8">

        <div v-if="products" class="py-8">

          <div class="grid grid-cols-1 gap-8">
            <div class="" v-for="product in products" :key="product.id">
              <div class="flex gap-8">
                <div class="flex-none w-[340px]">
                  <img :src="product.image" class="w-[320px]" />
                </div>
                <div class="grid grid-cols-1 gap-4">
                  <p class="text-xl text-sky-900 font-semibold">{{ product.name }}</p>
                  <div class="text-sky-800" v-html="product.description"></div>
                  <div class="flex items-center gap-4 py-1">
                    <button class="text-sm shadow-md shadow-black/50 bg-sky-800 text-gray-100 px-4 py-2 font-semibold uppercase cut-corners">Request price</button>
                    <nuxt-link :to="localePath({ name: 'ct-id', params: { ct: `category.url`, id: product.id } })" class="text-sm text-sky-800 font-semibold">Read more</nuxt-link>
                  </div>
                </div>
              </div>
            </div>
          </div>          

        </div>


        <div v-else class="min-h-[24vh]">
          <div class="flex items-center justify-center">
            <p class="text-4xl text-sky-900 py-8">Нет товаров для отображения</p>
          </div>
        </div>

      </div>


    </div>
  </div>
</template>