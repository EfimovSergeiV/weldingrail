<script setup>
  const localePath = useLocalePath()
  const config = useRuntimeConfig()
  const route = useRoute()
  const { locale, setLocale } = useI18n()




  const { data: categories } = await useFetch(`${ config.public.baseURL }${locale.value}/c/categories/`)
  const { data: products } = await useFetch(`${ config.public.baseURL }${locale.value}/c/products/`)


</script>


<template>
  <div class="h-screen flex items-center justify-center">
    <div class="">
      
      <p class="text-center text-red-800 text-2xl">
        ERROR 404: Page not found
      </p>

      <p class="text-center text-red-800 text-2xl">
        {{ route }}
      </p>      
    </div>

  </div>
</template>