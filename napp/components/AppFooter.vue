<script setup>
  const localePath = useLocalePath()
  const config = useRuntimeConfig()
  const props = defineProps(['categories'])

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
      <div class=" bg-sky-900 px-8 py-8">        
        <div class="grid grid-cols-2 content-between h-full">

          <div class="">
            <div class="grid grid-cols-1 gap-2">
              <div v-for="ct in props.categories" class="">
                <p class="text-white">{{ ct.name }}</p>
              </div>
            </div>            
          </div>


          <div class="flex items-center justify-center">
            <div class="grid grid-cols-1 gap-2">
              <p class="text-white text-xl font-bold uppercase italic text-center">Подписывайтесь на нашу новостную рассылку</p>
              <p class="text-white text-sm font-bold uppercase italic text-center">Будьте первым, кто узнает последние новости о тенденциях в сварочных технологиях!</p>
              <div id="subscriebe" class="flex items-center justify-center gap-0.5 py-4">
                <input type="email" class=" w-[240px] text-center h-8 px-4 text-base text-sky-900 bg-white border border-white/0 focus:border-white/0 focus:ring-gray-600/0 ring-0 placeholder-sky-800" placeholder="ваша электронная почта" /> 
                <button class=" h-8 px-8 text-base bg-sky-800 font-semibold text-white shadow-xl shadow-gray-900/10">Подписаться</button>
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
              <p class="text-xs text-gray-100">weldingrail.com | {{ currentData }} (c)</p>
            </div>
          </div>
        </div>
      </div>      
    </div>


  </div>
</template>