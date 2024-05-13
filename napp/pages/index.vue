<script setup>
  const localePath = useLocalePath()
  const config = useRuntimeConfig()
  const route = useRoute()
  const { locale, setLocale } = useI18n()




  const { data: categories } = await useFetch(`${ config.public.baseURL }${locale.value}/c/categories/`)
  const { data: products } = await useFetch(`${ config.public.baseURL }${locale.value}/c/products/`)

  const mashineDescription = ref('The machine is designed for flash butt welding of rails with cross-sectional area of from 6,500 mm to 10,000 mm in field conditions, through continuous or pulsating flashing, and removes flash immediately after welding. Due to the increased upsetting force of 140 tons, the welding machine is capable of welding long rail strings into tracks and tightening the strings. The welding machine can hold the welded joint within the time necessary for the joint to cool down after welding and removing flash. The welding machine is equipped with a welding process control system, which allows monitoring the welding process and and issues data sheets for every welded joint.')


</script>


<template>
  <div class="">
    
    <MainSlider />


    <div class="">
      <div class="">
        <div class="bg-gray-100">
          <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8 py-8">
            <div class="grid grid-cols-1 lg:flex items-end justify-between">
              <div class="">
                <p class="text-sky-900 text-xl md:text-4xl my-4">{{ $t('pages.index.chooseUs-title') }}</p>
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 text-sm md:text-base font-semibold">
                  <div class="flex items-center gap-1 mdi mdi-brightness-1 text-sky-900/80"><p class=" text-sky-900">{{ $t('pages.index.chooseUs-1') }}</p></div>
                  <div class="flex items-center gap-1 mdi mdi-brightness-1 text-sky-900/80"><p class=" text-sky-900">{{ $t('pages.index.chooseUs-2') }}</p></div>
                  <div class="flex items-center gap-1 mdi mdi-brightness-1 text-sky-900/80"><p class=" text-sky-900">{{ $t('pages.index.chooseUs-3') }}</p></div>
                  <div class="flex items-center gap-1 mdi mdi-brightness-1 text-sky-900/80"><p class=" text-sky-900">{{ $t('pages.index.chooseUs-4') }}</p></div>
                  <div class="flex items-center gap-1 mdi mdi-brightness-1 text-sky-900/80"><p class=" text-sky-900">{{ $t('pages.index.chooseUs-5') }}</p></div>
                  <div class="flex items-center gap-1 mdi mdi-brightness-1 text-sky-900/80"><p class=" text-sky-900"> {{ $t('pages.index.chooseUs-6') }}</p></div>
                </div>                  
              </div>
              <div class="grid grid-cols-1 gap-2 text-right">
                <div class="">
                  <a href="mailto:info@railwelding.com" target="_blank" class="text-sky-900 text-xl font-semibold">info@weldingrail.com</a>
                </div>
                <div class=" shadow-xl shadow-gray-900/10">
                  <button class="bg-gradient-to-tr from-sky-900 via-sky-900 to-sky-900 font-semibold text-white text-base w-60 py-2">{{ $t('requestCall') }}</button>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class=" bg-sky-900 border-t border-white/40">
          <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8">
            <div class="grid grid-cols-1 md:grid-cols-2 lg:flex items-center min-h-20 justify-between">
              <div class="flex items-center gap-2"><span class="font-bold text-white text-[36px]">+250</span><p class="text-white text-base font-semibold"> {{ $t('pages.index.employees') }}</p></div>
              <div class="flex items-center gap-2"><span class="font-bold text-white text-[36px]">+300</span><p class="text-white text-base font-semibold"> {{ $t('pages.index.complProjects') }}</p></div>
              <div class="flex items-center gap-2"><span class="font-bold text-white text-[36px]">+560Ha</span><p class="text-white text-base font-semibold"> {{ $t('pages.index.prodArea') }}</p></div>
              <div class="flex items-center gap-2"><span class="font-bold text-white text-[36px]">+150</span><p class="text-white text-base font-semibold">Клиентов</p></div>
            </div>
          </div>
        </div>
      </div>
    </div>



    <!-- <div class="py-16 hidden">
      <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8">
        <div class="flex items-center justify-center">
          <div class="grid grid-cols-1 gap-4 px-10">
            <p class="text-4xl text-sky-900 font-semibold text-center">Компания WELDINGRAIL – один из лидирующих мировых производителей оборудования для контактной стыковой сварки рельсов методом оплавления.</p>
            <p class="text-xl text-sky-900 text-center">Мы разрабатываем и производим надёжные рельсосварочные машины и комплексы, оказываем полный спектр услуг по гарантийному, постгарантийному обслуживанию оборудования, включая капитальный ремонт и модернизацию оборудования для сварки рельсов. Сильная инженерная команда и более 20 лет опыта позволяют нам разрабатывать высокотехнологичные решения по сварке рельсов. Оборудование WELDINGRAIL успешно эксплуатируется в 13-ти странах мира. Свяжитесь с нами, мы предложим вам лучшее решение для сварки рельсов.</p>
          </div>
        </div>
      </div>
    </div> -->



    <div class="bg-white py-10 min-h-screen grid grid-cols-1 content-center">

      <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8">
        <div v-for="category in categories" :key="category.id" class="py-8">
          
          <div class="grid grid-cols-1 gap-2">
            <p class="text-4xl font-semibold text-sky-900">{{ category.name }}</p>
            
            <div v-if="category.description" class="grid grid-cols-1 gap-4">
              <div class="text-base text-sky-900 px-0.5" v-html="category.description"></div>
            </div>

          </div>



          <div class="grid grid-cols-1">
            <div v-for="product in products" :key="product.id">
              <div v-if="product.category === category.id" class="py-8">
                


                <div class="">
                  <div class="flex items-center gap-4">
                    <div class="flex-none w-[340px]">
                      <img :src="product.image" class="w-[280px]" />
                    </div>
                    <div class="grid grid-cols-1 gap-4">
                      <p class="text-xl text-sky-900 font-semibold">{{ product.name }}</p>
                      <div class="text-sky-900" v-html="product.description"></div>
                      <div class="flex items-center gap-4 py-1">
                        <button class="bg-gradient-to-tr from-sky-900 via-sky-900 to-sky-900 font-semibold text-white text-base w-60 py-2">{{ $t('requestCall') }}</button>
                        <nuxt-link :to="localePath({ name: 'ct-id', params: { ct: category.url, id: product.id } })" class="text-base text-sky-900 font-semibold">Read more</nuxt-link>
                      </div>
                    </div>
                  </div>
                </div>

              


              </div>
            </div>                
          </div>





          <div v-if="category.children" class="mt-6">
            <div class="grid grid-cols-1 lg:grid-cols-3 gap-4">
              <div v-for="subct in category.children" :key="subct.id" class="">
                <nuxt-link :to="localePath({ name: 'ct', params: { ct: subct.url } })">
                  <p class="text-left text-xl text-sky-900 font-semibold">{{ subct.name }}</p>
                </nuxt-link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>






    <div class="">
      <div class="bg-white">

        <div class="bg-[url('images/rails-bg.webp')] h-[380px] bg-no-repeat bg-left-bottom bg-cover">
          <div class="bg-sky-900/70 hover:bg-sky-900/80 backdrop-blur-sm transition-all duration-1000 h-full relative">
            <div class="absolute w-full h-full">

              <div class="flex items-center justify-center h-full px-6">
                <div class="grid grid-cols-1 gap-4">
                  <p class="text-white text-3xl uppercase">
                    {{ $t('pages.index.quest-title') }}
                  </p>
                  <p class="text-4xl text-white uppercase">
                    {{ $t('pages.index.quest-text') }}
                  </p>
                </div>
              </div>

            </div>
          </div>
        </div>

      </div>
    </div>

    <div class="bg-sky-900 border-t border-b border-white/20">
      <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8">
        <div class="">
          <a href="#" class="flex items-center justify-center gap-2 py-6">
            <div class="mdi mdi-24px mdi-book-open-page-variant text-gray-100"></div>
            <p class="text-xl text-gray-100">Скачать каталог</p>
          </a>
        </div>
      </div>
    </div>





    <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8 py-8">

      <div class="py-4">
        <div class="flex items-center justify-start">
          <p class="text-4xl text-sky-900 font-semibold">О компании</p>
        </div>        
        <div class="py-4">
          <div class="grid grid-cols-1 gap-0.5">
            <p class="text-lg text-sky-900 font-semibold py-2">WELDINGRAIL – один из лидирующих мировых производителей оборудования для контактной стыковой сварки рельсов методом оплавления.</p>
            <p class="text-base text-sky-900">Мы разрабатываем и производим надёжные рельсосварочные машины и комплексы, оказываем полный спектр услуг по гарантийному, постгарантийному обслуживанию оборудования, включая капитальный ремонт и модернизацию оборудования для сварки рельсов.</p>
          </div>
        </div>
      </div>


      <div class="grid grid-cols-2 gap-4">

        <div class=" flex items-start justify-center">
          <div class="grid grid-cols-1 gap-2">

            <!-- <div class="flex items-center gap-2 text-sky-900 mdi mdi-24px mdi-checkbox-marked-outline">
              <p class="text-base"> Сильная инженерная команда и более 20 лет опыта позволяют нам разрабатывать высокотехнологичные решения по сварке рельсов.</p>
            </div>
            <div class="flex items-center gap-2 text-sky-900 mdi mdi-24px mdi-checkbox-marked-outline">
              <p class="text-base"> Оборудование WELDINGRAIL успешно эксплуатируется в 13-ти странах мира.</p>
            </div> -->

            <p class="text-base text-sky-900 "> Сильная инженерная команда и более 20 лет опыта позволяют нам разрабатывать высокотехнологичные решения по сварке рельсов.</p>
            <p class="text-base text-sky-900 "> Оборудование WELDINGRAIL успешно эксплуатируется в 13-ти странах мира.</p>
            <p class="text-base text-sky-900 py-1"> Свяжитесь с нами, мы предложим вам лучшее решение для сварки рельсов.</p>
            
            <div class="flex items-center justify-center py-8">
              <img src="/logo-blue.webp" class="w-[50%]"/>
            </div>
          </div>
        </div>

        <div class="grid grid-cols-1 gap-2">
          <div class="relative">
            <p class="absolute px-2 py-1 mdi mdi-16px mdi-account-tie text-sky-900/90"></p>
            <input type="text" id="person" class="bg-gray-50 shadow-lg shadow-black/10 border border-gray-300 focus:border-gray-300 text-gray-900 text-sm focus:ring-blue-500/0 focus:border-blue-500/0 block w-full pl-8 py-1.5 " :placeholder="$t('pages.index.yorname')" />
          </div>
          <div class="relative">
            <p class="absolute px-2 py-1 mdi mdi-16px mdi-at text-sky-900/90"></p>
            <input type="text" id="person" class="bg-gray-50 shadow-lg shadow-black/10 border border-gray-300 focus:border-gray-300 text-gray-900 text-sm focus:ring-blue-500/0 focus:border-blue-500/0 block w-full pl-8 p-1.5 " :placeholder="$t('pages.index.youremail')" />
          </div>
          <div class="relative">
            <p class="absolute px-2 py-1 mdi mdi-16px mdi-text-long text-sky-900/90"></p>
            <textarea type="text" id="person" rows="8" class="bg-gray-50 shadow-lg shadow-black/10 border border-gray-300 focus:border-gray-300 text-gray-900 text-sm focus:ring-blue-500/0 focus:border-blue-500/0 block w-full pl-8 p-1.5 " :placeholder="$t('pages.index.yourmess')"></textarea>
          </div>
          <div class="flex items-center justify-end">
            <button class="bg-gradient-to-tr from-sky-800 via-sky-700 to-sky-800 font-semibold text-white w-60 py-2 shadow-xl shadow-gray-900/10">Отправить сообщение</button>
          </div>
        </div>

      </div>
    </div>










    <div class=" bg-sky-900">
      <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8 py-2">

        <div class="flex items-center justify-center py-6">
          <p class="text-white text-xl">Нашими партнёрами уже стали</p>
        </div>

        <div class="grid grid-cols-2 lg:grid-cols-4 gap-2">
          <div class="px-8">
            <div class="flex items-center justify-center py-2">
              <img src="/partners/2.png" class="h-12"/>
            </div>
            <div class="flex items-center justify-center py-2">
              <p class="text-gray-100 text-base">Kazakh Railways</p>
            </div>
          </div>
          <div class="px-8">
            <div class="flex items-center justify-center py-2">
              <img src="/partners/1.png" class="h-12"/>
            </div>
            <div class="flex items-center justify-center py-2">
              <p class="text-gray-100 text-base">Lithuanian Railways</p>
            </div>
          </div>
          <div class="px-8">
            <div class="flex items-center justify-center py-2">
              <img src="/partners/3.png" class="h-12"/>
            </div>
            <div class="flex items-center justify-center py-2">
              <p class="text-gray-100 text-base">Ozbekiston temir yollari</p>
            </div>
          </div>
          <div class="px-8">
            <div class="flex items-center justify-center py-2">
              <img src="/partners/4.png" class="h-12"/>
            </div>
            <div class="flex items-center justify-center py-2">
              <p class="text-gray-100 text-base">Belarusian railways</p>
            </div>
          </div>
        </div>
      </div>
    </div>








  </div>
</template>


