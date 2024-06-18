<script setup>

  const props = defineProps(['categories', 'products',])
  const catSelected = ref(1)
  const prodSelected = ref(0)

  const message = (message) => {
    alert(message)
  }

</script>



<template>
  <div class="">
    <!-- Вторая версия -->
    
    <div class="flex items-center px-8 py-2">
      <transition name="fade">
        <nuxt-link :to="localePath({ name: 'ct-id', params: { ct: categories[catSelected - 1].url, id: products[prodSelected].id } })" class="text-4xl text-sky-800 italic font-semibold">{{ products[prodSelected].name }}</nuxt-link>
      </transition>
    </div>

    <div class="grid grid-cols-2 gap-4 py-8">



      <div class="flex items-center justify-between gap-2 px-14">

        <div class="">
          <div v-if="prodSelected > 0" @click="prodSelected = prodSelected - 1" class="mdi mdi-48px mdi-arrow-left-bold-hexagon-outline text-sky-800 cursor-pointer"></div>
          <div v-else class="mdi mdi-48px mdi-arrow-left-bold-hexagon-outline text-sky-800/50 cursor-not-allowed"></div>
        </div>

        <div class="flex items-center justify-center">
          <div class="grid grid-cols-1 gap-4">
            <div class="grid grid-cols-1 gap-4">
              <div class="flex items-center justify-center">
                <img :src="products[prodSelected].image" class="w-[240px]" />
              </div>
            </div>

            <div class="flex flex-col items-start justify-center gap-8 mt-2">                
              <div class="flex items-center justify-start gap-4">
                <button  @click="message(`Запросили стоимость стоимость товара`)" class="min-w-[180px] bg-gradient-to-tr from-sky-800 via-sky-700 to-sky-800 font-semibold text-white text-base py-2 px-4 button-polygon ">{{ $t('requestPrice') }}</button>
                <nuxt-link :to="localePath({ name: 'ct-id', params: { ct: categories[catSelected -1].url, id: products[prodSelected].id } })" class="text-base text-sky-800 font-semibold">{{ $t('learnMore') }}</nuxt-link>
              </div>                  
            </div>

          </div>
        </div>

        <div class="">
          <div v-if="prodSelected < products.length - 1" @click="prodSelected = prodSelected + 1" class="mdi mdi-48px mdi-arrow-right-bold-hexagon-outline text-sky-800 cursor-pointer"></div>
          <div v-else class="mdi mdi-48px mdi-arrow-right-bold-hexagon-outline text-sky-800/50 cursor-not-allowed"></div>
        </div>

      </div>



      <div class="flex flex-col gap-2">
        <div v-for="ct in categories" class="">
          <div class="flex items-center justify-end">
            
            <div v-if="ct.id === catSelected" :class="`bg-sky-800 pl-24 pr-4 transition-all duration-[800ms] border-r-4 border-orange-500 py-2 bg-slice-left cursor-pointer`">
              <!-- localePath({ name: 'ct', params: { ct: ct.url } }) <p class="text-xl text-white italic font-semibold text-right px-8">{{ ct.name }}</p> -->
              <nuxt-link :to="localePath({ name: 'ct', params: { ct: categories[catSelected -1].url} })" class="text-xl text-white italic font-semibold text-right px-8">{{ ct.name }}</nuxt-link>
            </div>
            <div v-else @click="catSelected = ct.id" :class="`bg-sky-800 pl-14 hover:pl-24 hover:pr-3 transition-all duration-[800ms] py-2 bg-slice-left cursor-pointer`">
              <p class="text-xl text-white italic font-semibold text-right px-8">{{ ct.name }}</p>
            </div>
            
          </div>
        </div>
      </div>

    </div>


  </div>
</template>