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


    

    
    <div class=" bg-sky-800">

      <div class="w-[1200px] absolute right-0 z-0">
        <div class="">
          <img src="/backgrounds/container-edd.webp" class="w-full" />
        </div>  
      </div>


      <div class="min-h-screen grid grid-cols-1 content-between">

        <div></div>

        <div class="">
          <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8">
            <div class="flex items-center">
              <div class="mt-32">
                <div class="py-2">
                  <p class="text-5xl text-white se lect-none font-sans">{{ $t('slogan') }}</p>
                </div>     
                <div class="grid grid-cols-1 gap-0">
                  <p class="leading-[4rem] font-extra text-transparent text-[58px] text-white uppercase se lect-none">{{ $t('title-1') }}</p>
                  <p class="leading-[4rem] font-extra text-transparent text-[58px] text-white uppercase se lect-none">{{ $t('title-2') }}</p>
                </div>
              </div>
            </div>
          </div>
        </div>


        <div class="">
          <div class="">

            <div class="">
              <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8 py-4">
                <div class="flex items-end justify-end">
                  <p class="text-white leading-[0rem] text-5xl font-semibold">info@weldingrail.com</p>
                </div>
                <div class="grid grid-cols-1 lg:flex items-end justify-between">
                  
                  <div class="">
                    <p class="text-white text-2xl md:text-4xl my-4">{{ $t('pages.index.chooseUs-title') }}</p>
                    <div class="grid grid-cols-1 lg:grid-cols-3 gap-4 text-gray-100 text-sm md:text-base">
                      <div class="flex items-center gap-1 mdi mdi-brightness-1"><p class=" text-gray-200 font-semibold ">{{ $t('pages.index.chooseUs-1') }}</p></div>
                      <div class="flex items-center gap-1 mdi mdi-brightness-1"><p class=" text-gray-200 font-semibold ">{{ $t('pages.index.chooseUs-2') }}</p></div>
                      <div class="flex items-center gap-1 mdi mdi-brightness-1"><p class=" text-gray-200 font-semibold ">{{ $t('pages.index.chooseUs-3') }}</p></div>
                      <div class="flex items-center gap-1 mdi mdi-brightness-1"><p class=" text-gray-200 font-semibold ">{{ $t('pages.index.chooseUs-4') }}</p></div>
                      <div class="flex items-center gap-1 mdi mdi-brightness-1"><p class=" text-gray-200 font-semibold ">{{ $t('pages.index.chooseUs-5') }}</p></div>
                      <div class="flex items-center gap-1 mdi mdi-brightness-1"><p class=" text-gray-200 font-semibold "> {{ $t('pages.index.chooseUs-6') }}</p></div>
                    </div>                  
                  </div>

                  <div class="">
                    <div class=" shadow-xl shadow-gray-900/10">
                      <button class="bg-gradient-to-tr from-white via-gray-200 to-gray-200 font-semibold text-main-secondary w-60 py-2 mt-2 cut-corners">{{ $t('requestCall') }}</button>
                    </div>
                  </div>
                  
                </div>
              </div>
            </div>


            <div class=" bg-sky-800 border-t border-white/10">
              <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8">
                <div class="grid grid-cols-1 lg:flex items-center min-h-20 justify-between">
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



      <div class="bg-white py-10 min-h-screen grid grid-cols-1 content-center">

        <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8">
          <div v-for="category in categories" :key="category.id" class="py-8">
            
            <div class="grid grid-cols-1 gap-2">
              <p class="text-4xl text-sky-950">{{ category.name }}</p>
              <div v-if="category.description" class="text-base text-sky-900" v-html="category.description"></div>              
            </div>



              <div class="grid grid-cols-1 lg:grid-cols-2 py-4">
                <div v-for="product in products" :key="product.id">
                  <div v-if="product.category === category.id">
                    
                    
                    <div class="">

                      <div class="">
                        <nuxt-link :to="localePath({ name: 'ct-id', params: { ct: category.url, id: product.id } })">
                          <p class="text-center text-xl text-sky-950">{{ product.name }}</p>
                        </nuxt-link>                        
                      </div>

                      <div class="grid grid-cols-1 md:flex gap-8 py-6">
                        <div class="py-2 flex items-center justify-center md:w-[160px]">
                          <img :src="product.image" class="w-[160px] h-[120px]" />
                        </div>
                        <div class="flex flex-col justify-between">
                          
                            <div class="grid grid-cols-1 gap-0.5 pb-4">
                              <div v-for="advantage in [{'id': 1, 'name': 'Квадратный'},{'id': 2, 'name': 'Практичный'},{'id': 2, 'name': 'Хороший'}, ]" :key="advantage.id" class="">

                                <div class="flex items-center gap-2">
                                  <div class="mdi mdi-circle text-sky-800"></div>
                                  <p class="text-sm text-sky-950">
                                     {{ advantage.name }}
                                     {{ advantage.name }}
                                     {{ advantage.name }}
                                     {{ advantage.name }}

                                  </p>
                                </div>

                              </div>
                            </div>
                          

                          <div class="flex items-center gap-4 py-1">
                            <button class="text-sm shadow-md shadow-black/50 bg-sky-800 text-gray-100 px-4 py-2 font-semibold uppercase cut-corners">Request price</button>
                            <nuxt-link :to="localePath({ name: 'ct-id', params: { ct: category.url, id: product.id } })" class="text-sm text-sky-800 font-semibold">Read more</nuxt-link>
                          </div>
                        </div>
                      </div>                        
                    </div>
                  
                  </div>

                </div>                
              </div>




              <div v-if="category.children" class="">
                <div class="grid grid-cols-1 lg:grid-cols-3 gap-x-6 gap-y-4">
                  <div v-for="subct in category.children" :key="subct.id">
                    
                    <nuxt-link :to="localePath({ name: 'ct', params: { ct: subct.url } })">
                      <button class="text-base shadow-md shadow-black/50 bg-sky-800 text-gray-100 px-4 py-6 font-semibold uppercase cut-corners w-full">{{ subct.name }}</button>
                    </nuxt-link>
                    

                  </div>
                </div>

              </div>




          </div>



        </div>



      </div>
    </div>


    <div class="">
      <div class="bg-white">

        <div class="bg-[url('images/rails-bg.jpg')] h-[380px] bg-no-repeat bg-left-bottom bg-cover">
          <div class="bg-sky-950/70 hover:bg-sky-950/80 backdrop-blur-sm transition-all duration-1000 h-full relative">
            <div class="absolute w-full h-full">

              <div class="flex items-center justify-center h-full px-6">
                <div class="grid grid-cols-1 gap-8">
                  <p class="text-slate-200 font-semibold text-xl uppercase">
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

    <div class="bg-sky-950 border-t border-b border-white/20">
      <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8">
        <div class="">
          <a href="#" class="flex items-center justify-center gap-2 py-6">
            <div class="mdi mdi-24px mdi-book-open-page-variant text-gray-100"></div>
            <p class="text-xl text-gray-100">Скачать каталог</p>
          </a>
        </div>
      </div>
    </div>


    <div id="repair" class="">
      <div class="bg-white/80 py-8 grid grid-cols-1 content-center border-t border-b border-sky-950/20">
        <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8">

          <div class="flex items-center justify-end my-4">
            <p class="font-sans font-extrabold text-transparent text-2xl bg-clip-text bg-gradient-to-r from-sky-900 to-sky-800 uppercase se lect-none">
              Наши услуги
            </p>
          </div>

          <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
            <div class="">
              <div class="flex">
                <div class="bg-sky-800 z-20 rounded-sm px-8 py-2">
                  <p class=" font-sans font-semibold text-transparent text-lg bg-clip-text bg-gradient-to-r from-white to-gray-200 uppercase">
                    {{ $t('pages.index.repair-title') }}
                  </p>                  
                </div>
              </div>
              <div class="bg-gradient-to-br z-10 from-white/70 to-white/40 backdrop-blur-sm border border-sky-950/10 shadow-xl shadow-black/10 rounded-md -mt-6 py-8 ">

                <div class="py-2 px-4">
                  <p class="text-sky-900 uppercase text-sm font-semibold"> Мы имеем:</p>

                  <div class="grid grid-cols-1 gap-1 my-2">
                    <div class="flex items-center gap-2 text-sky-900/30 mdi mdi-brightness-1 text-xs">
                      <p class="text-sm text-sky-950"> Собственное современное производство</p>
                    </div>
                    <div class="flex items-center gap-2 text-sky-900/30 mdi mdi-brightness-1 text-xs">
                      <p class="text-sm text-sky-950"> Собственный конструкторский отдел</p>
                    </div>
                    <div class="flex items-center gap-2 text-sky-900/30 mdi mdi-brightness-1 text-xs">
                      <p class="text-sm text-sky-950"> Проверенных поставщиков материалов</p>
                    </div>            
                  </div>

                  
                </div>

                <div class="bg-sky-800 px-6 py-2">
                  <p class="text-sm text-white font-sans">
                    {{ $t('pages.index.repair-text-1') }}
                  </p>                  
                </div>

                <div class="px-4">
                  <p class="text-sm text-sky-900 font-semibold se lect-none font-sans my-4">
                    {{ $t('pages.index.repair-text-2') }}
                  </p>
                </div>
               
              </div>
            </div>


            <div class="mt-8">
              <div class="flex">
                <div class="bg-sky-800 z-20 rounded-sm px-8 py-2">
                  <p class=" font-sans font-semibold text-transparent text-lg bg-clip-text bg-gradient-to-r from-white to-gray-200 uppercase">
                    {{ $t('pages.index.learn-title') }}
                  </p>                  
                </div>
              </div>
              <div class="bg-gradient-to-br z-10 from-white/70 to-white/40 backdrop-blur-sm border border-sky-950/10 shadow-xl shadow-black/10 rounded-md -mt-6 py-8 ">

                <div class="py-2 px-4">
                  <p class="text-sm text-sky-950 se lect-none font-sans">
                    Мы предлагаем специализированное техническое обучение и консультации по электросварке рельсов.
                  </p>
                </div>

                <div class="py-2 px-4">
                  <p class="text-sm text-sky-950 se lect-none font-sans">
                    Наша команда состоит из опытных инженеров и квалифицированных рабочих, которые всегда готовы и рады поделиться своими знаниями с другими профессионалами в этой области. 
                  </p>
                </div>
              
                <div class="bg-sky-800 px-6 py-2 rounded-sm">
                  <p class="text-sm text-gray-100 font-sans">
                    Сервисная служба компании Railwelding уделяет много внимания качественной передаче знаний, постоянному сопровождению и обеспечению устойчивого производства без необходимости частого технического обслуживания. Такой комплексный подход к клиентскому сервису является залогом долгосрочного плодотворного сотрудничества.
                  </p>                  
                </div>

                <div class="py-2 px-4">
                  <p class="text-sm font-semibold text-sky-900 se lect-none font-sans">
                    Мы охотно обучим и проконсультируем вас по всем вопросам эксплуатации и обслуживания выпускаемого нами оборудования.                  </p>
                </div>
        
              </div>
            </div>
          </div>

        </div>
      </div>
    </div>



    <div id="service" class="bg-white/80 py-8 min-h-screen grid grid-cols-1 content-center">
      <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8">

        <div class="flex">
          <div class="bg-sky-800 z-20 rounded-sm px-8 py-2 ">
            <p class=" font-sans font-semibold text-transparent text-lg bg-clip-text bg-gradient-to-r from-white to-gray-200 uppercase">
              Ремонт и обслуживание оборудования
            </p>                  
          </div>
        </div>


        <div class="grid grid-cols-1 gap-8">


          <div class="">
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 py-8">
              <div class="bg-gradient-to-br from-gray-100/95 to-gray-50/90 border-l-8 border-sky-800/90 shadow-lg shadow-black/10 px-4">
                <div class=" h-[6rem] flex items-center py-2">
                  <p class="text-md text-sky-800 font-sans">{{ $t('pages.index.service-2') }}</p>

                </div>
              </div>
            
              <div class="bg-gradient-to-br from-gray-100/95 to-gray-50/90 border-l-8 border-sky-800/90 shadow-lg shadow-black/10 px-4">
                <div class="h-[6rem] flex items-center py-2">
                  <p class="text-md text-sky-800 font-sans">{{ $t('pages.index.service-3') }}</p>

                </div>
              </div>

              <div class="bg-gradient-to-br from-gray-100/95 to-gray-50/90 border-l-8 border-sky-800/90 shadow-lg shadow-black/10 px-4">
                <div class="h-[6rem] flex items-center py-2">
                  <p class="text-md text-sky-800 font-sans">{{ $t('pages.index.service-4') }}</p>

                </div>
              </div>

              <div class="bg-gradient-to-br from-gray-100/95 to-gray-50/90 border-l-8 border-sky-800/90 shadow-lg shadow-black/10 px-4">
                <div class="h-[6rem] flex items-center py-2">
                  <p class="text-md text-sky-800 font-sans">{{ $t('pages.index.service-5') }}</p>

                </div>
              </div>
            </div>

          </div>
        </div>



        <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 py-8">

          <div class="flex items-center justify-center order-2 lg:order-1">
            <div class="w-full">
              <div class="grid grid-cols-1 gap-2">
                <div class="relative">
                  <p class="absolute px-2 py-1 mdi mdi-16px mdi-account-tie text-sky-950/90"></p>
                  <input type="text" id="person" class="bg-gray-50 shadow-lg shadow-black/10 border border-gray-300 focus:border-gray-300 text-gray-900 text-sm focus:ring-blue-500/0 focus:border-blue-500/0 block w-full pl-8 py-1.5 " :placeholder="$t('pages.index.yorname')" />
                </div>
                <div class="relative">
                  <p class="absolute px-2 py-1 mdi mdi-16px mdi-at text-sky-950/90"></p>
                  <input type="text" id="person" class="bg-gray-50 shadow-lg shadow-black/10 border border-gray-300 focus:border-gray-300 text-gray-900 text-sm focus:ring-blue-500/0 focus:border-blue-500/0 block w-full pl-8 p-1.5 " :placeholder="$t('pages.index.youremail')" />
                </div>
                <div class="relative">
                  <p class="absolute px-2 py-1 mdi mdi-16px mdi-text-long text-sky-950/90"></p>
                  <textarea type="text" id="person" rows="8" class="bg-gray-50 shadow-lg shadow-black/10 border border-gray-300 focus:border-gray-300 text-gray-900 text-sm focus:ring-blue-500/0 focus:border-blue-500/0 block w-full pl-8 p-1.5 " :placeholder="$t('pages.index.yourmess')"></textarea>
                </div>
              </div>
              <div class="flex items-center justify-end py-2 ">
                <button class="text-sm shadow-md shadow-black/50 bg-sky-800 text-gray-100 px-4 py-2 font-semibold uppercase cut-corners">Отправить сообщение</button>
              </div>
            </div>
          </div>


          <div class="flex items-center order-1 lg:order-2">
            <div class="">
              <p class="text-4xl font-semibold text-sky-900 se lect-none font-sans uppercase py-1">Почему выбирают нас ?</p>
              <p class="text-xl text-sky-950 se lect-none font-sans py-1">
                {{ $t('pages.index.service-1' ) }}
              </p>
              <div class="my-4">
                <p class="text-xl text-sky-950 se lect-none font-sans">
                  {{ $t('pages.index.service-6') }}
                </p>
              </div>              
            </div>
          </div>

        </div>
      </div>
    </div>


    <!-- <div class="border-t border-sky-950/30">
      <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8">
        <div class="flex items-center justify-center">
          <div class="grid grid-cols-3 gap-24 py-2">
            
            <div class="text-sky-900 flex items-center gap-4">
              <div>
                <div class="mdi mdi-36px mdi-map-marker text-sky-900"></div>
              </div>
              <div>
                <p class="font-semibold text-sm">Axel Springer Neubau</p>
                <div class="py-1 grid grid-cols-1 gap-0.5">
                  <p class="text-xs">Zimmerstraße 50, 10117 Berlin</p>                  
                </div>              
              </div>
            </div>

            <div class="text-sky-900 flex items-center gap-8">
              <div>
                <div class="mdi mdi-36px mdi-at text-sky-900"></div>
              </div>
              <div>
                <p class="font-semibold text-sm">Напишите нам</p>
                <div class="py-1 grid grid-cols-1 gap-0.5">
                  <p class="text-xs">info@weldingrail.com</p>
                </div>              
              </div>
            </div>

            <div class="text-sky-900 flex items-center gap-8">
              <div>
                <div class="mdi mdi-36px mdi-book-open-page-variant text-sky-900"></div>
              </div>
              <div>
                <p class="font-semibold text-sm">Cкачать каталог</p>
                <div class="py-1 grid grid-cols-1 gap-1">
                  <a href="#" class="text-xs cursor-pointer">catalog-railwelding.pdf</a>
                </div>              
              </div>
            </div>

          </div>
        </div>
      </div>
    </div> -->

    

  </div>
</template>