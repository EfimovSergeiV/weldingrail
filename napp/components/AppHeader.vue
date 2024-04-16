<script lang="ts" setup>

  const localePath = useLocalePath()
  const switchLocalePath = useSwitchLocalePath()


  const railmachines = ref([
    { 'id': 1, 'name': 'FBM-60', 'path': 'fbm-60' },
    { 'id': 2, 'name': 'FBM-140', 'path': 'fbm-140' },
    { 'id': 3, 'name': 'FBM-150', 'path': 'fbm-150' },
    { 'id': 4, 'name': 'FBM-160', 'path': 'fbm-160' },
    { 'id': 5, 'name': 'FBM-170', 'path': 'fbm-170' },
  ])

  const mashineDescription = ref('The machine is designed for flash butt welding of rails with cross-sectional area of from 6,500 mm to 10,000 mm in field conditions, through continuous or pulsating flashing, and removes flash immediately after welding. Due to the increased upsetting force of 140 tons, the welding machine is capable of welding long rail strings into tracks and tightening the strings. The welding machine can hold the welded joint within the time necessary for the joint to cool down after welding and removing flash. The welding machine is equipped with a welding process control system, which allows monitoring the welding process and and issues data sheets for every welded joint.')


</script>


<template>
  <div class="">

    <div class=" ">
      <div id="navbar" class="bg-white/60 border-b border-main-primary/40 shadow-sm shadow-main-primary/40 w-full absolute z-50 backdrop-blur-sm duration-700 transition-all">
        <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8 flex items-center justify-between gap-12 h-full relative">
          <div class="py-1 ">
            <nuxt-link :to="localePath('index')">
              <img src="/railwelding-logo.webp" class=" h-6" />
            </nuxt-link>                
          </div>
          <div class="flex gap-8 items-center">
            <div class="group">
              <nuxt-link :to="localePath({ name: 'index'})" class="text-xl text-center text-sky-900 h-[56px] flex items-center">{{ $t('railWeldingEquipment') }}</nuxt-link>
              <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8 absolute w-full right-0 invisible group-hover:visible ease-in-out transition-opacity duration-300 opacity-0 group-hover:opacity-100">
                <div class="py-1">
                  <div class="bg-white shadow-md shadow-black/30 rounded-sm w-full">

                    <div class="flex justify-end">

                      <div class="border border-white px-2 py-4 w-full">

                        <div class="">
                          <div class="border-b border-sky-950/50 px-4 mx-4">
                            <p class="text-sky-900 text-sm font-semibold">Стационарные рельсосварочные машины</p>
                          </div>
                          
                          <div class="grid grid-cols-2 gap-2">
                            <div v-for="machine in railmachines.slice(0, 3)" :key="machine.id" class="">
                              <div class="">
                                <nuxt-link :to="localePath({ name: 'ct-name', hash: '#product-description', params: { name: machine.path } })" class="">
                                  <div class="px-2 py-2">
                                    <div class="flex items-center gap-2">
                                      <div class="px-4 py-2">
                                        <img src="/prod/fbm-140.png" class=" w-14" />
                                      </div>
                                      
                                      <div class=" grid grid-cols-1">
                                        <p class=" text-sm text-sky-950 py-1">{{  machine.name }}</p>
                                        <div class="flex justify-start">
                                          <p class="text-xs text-sky-950">перейти к машине</p>
                                        </div>
                                      </div>
                                      

                                    </div>

                                    <div>


                                    </div>

                                  </div>
                                </nuxt-link>
                              </div>

                            </div>
                          </div>
                        </div>

                        <div class="">
                          <div class="border-b border-sky-950/50 px-4 mx-4">
                            <p class="text-sky-900 text-sm font-semibold">Мобильные рельсосварочные машины</p>
                          </div>
                          
                          <div class="grid grid-cols-2 gap-2">
                            <div v-for="machine in railmachines.slice(0, 2)" :key="machine.id" class="">
                              <div class="">
                                <nuxt-link :to="localePath({ name: 'ct-name', hash: '#product-description', params: { name: machine.path } })" class="">
                                  <div class="px-2 py-2">
                                    <div class="flex items-center gap-2">
                                      <div class="px-4 py-2">
                                        <img src="/prod/fbm-140.png" class=" w-14" />
                                      </div>
                                      
                                      <div class=" grid grid-cols-1">
                                        <p class=" text-sm text-sky-950 py-1">{{  machine.name }}</p>
                                        <div class="flex justify-start">
                                          <p class="text-xs text-sky-950">перейти к машине</p>
                                        </div>
                                      </div>
                                      

                                    </div>

                                    <div>


                                    </div>

                                  </div>
                                </nuxt-link>
                              </div>

                            </div>
                          </div>
                        </div>
                        <div class="">
                          <div class="border-b border-sky-950/50 px-4 mx-4">
                            <p class="text-sky-900 text-sm font-semibold">Испытательное оборудование</p>
                          </div>
                          
                          <div class="grid grid-cols-2 gap-2">
                            <div v-for="machine in railmachines.slice(0, 1)" :key="machine.id" class="">
                              <div class="">
                                <nuxt-link :to="localePath({ name: 'ct-name', hash: '#product-description', params: { name: machine.path } })" class="">
                                  <div class="px-2 py-2">
                                    <div class="flex items-center gap-2">
                                      <div class="px-4 py-2">
                                        <img src="/prod/fbm-140.png" class=" w-14" />
                                      </div>
                                      
                                      <div class=" grid grid-cols-1">
                                        <p class=" text-sm text-sky-950 py-1">ГЕРКУЛЕС 300</p>
                                        <div class="flex justify-start">
                                          <p class="text-xs text-sky-950">перейти к машине</p>
                                        </div>
                                      </div>
                                      

                                    </div>

                                    <div>


                                    </div>

                                  </div>
                                </nuxt-link>
                              </div>

                            </div>
                          </div>
                        </div>
                      </div>


                      <div class="px-4 bg-sky-800 border border-sky-800 w-[640px] py-4 flex items-center">
                        <div class="">
                          <div class="">
                            <p class="text-white font-semibold text-2xl">Рельсосварочое оборудование</p>
                          </div>
                          <div class="my-4 py-4 border-t border-white/50">
                            <p class="text-sm text-gray-100">Представляем вашему вниманию наши решения для сварки рельсов. Наше оборудование является сертифицированным по самим жёстким стандартам и проверенное временем</p>
                          </div>
                        </div>
                      </div>

                    </div>

                  </div>
                </div>
              </div>
            </div>



            <div class="group">
              <nuxt-link :to="localePath({ name: 'index'})" class="text-xl text-center text-sky-900 h-[56px] flex items-center">{{ $t('services') }}</nuxt-link>
              <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8 absolute w-full right-0 invisible group-hover:visible ease-in-out transition-opacity duration-300 opacity-0 group-hover:opacity-100">
                <div class="py-1">
                  <div class="bg-white shadow-md shadow-black/30 rounded-sm w-full">

                    <div class="flex justify-end">

                      <div class="border border-white px-2 py-4 w-full">

                        <div class="">
                          <div class="border-b border-sky-950/50 px-4 mx-4">
                            <p class="text-sky-900 text-sm font-semibold">Капитальный ремонт оборудования</p>
                          </div>
                          
                          <div class="grid grid-cols-1 gap-2 px-8 py-2">
                            <p class="text-sm text-sky-800">
                              Мы готовы не только осуществить полное восстановление бывшего в эксплуатации оборудования, но и улучшить его технические характеристики, необходимые для введения вашей устаревшей рельсосварочной машины в современное производство.                            </p>
                          </div>
                        </div>

                        <div class="">
                          <div class="border-b border-sky-950/50 px-4 mx-4">
                            <p class="text-sky-900 text-sm font-semibold">Обучение и техническая поддержка</p>
                          </div>
                          
                          <div class="grid grid-cols-1 gap-2 px-8 py-2">
                            <p class="text-sm text-sky-800">
                              Наша команда состоит из опытных инженеров и квалифицированных рабочих, которые всегда готовы и рады поделиться своими знаниями с другими профессионалами в этой области.                            </p>
                          </div>
                        </div>
                        <div class="">
                          <div class="border-b border-sky-950/50 px-4 mx-4">
                            <p class="text-sky-900 text-sm font-semibold">Ремонт и техническое обслуживание</p>
                          </div>
                          
                          <div class="grid grid-cols-1 gap-2 px-8 py-2">
                            <p class="text-sm text-sky-800">
                              С нашим многолетним опытом работы в железнодорожной отрасли, наша команда экспертов готова предоставить выдающийся уровень профессионализма и экспертизы при обслуживании и устранении неполадок для всех видов продукции Railwelding. Независимо от того, имеется ли у вас оборудование для сварки рельсов, электропередвижные сварочные машины или другие товары из нашего разнообразного ассортимента, мы обеспечиваем полное техническое обслуживание и оперативное устранение любых возможных неисправностей.
                            </p>
                          </div>
                        </div>
                      </div>


                      <div class="px-4 bg-sky-800 border border-sky-800 w-[640px] py-4 flex items-center">
                        <div class="">
                          <div class="">
                            <p class="text-white font-semibold text-2xl">Наши услуги</p>
                          </div>
                          <div class="my-4 py-4 border-t border-white/50">
                            <p class="text-sm text-gray-100">С нашим многолетним опытом работы в железнодорожной отрасли, наша команда экспертов готова предоставить выдающийся уровень профессионализма и экспертизы при обслуживании и устранении неполадок для всех видов продукции Railwelding</p>
                          </div>
                        </div>
                      </div>

                    </div>

                  </div>
                </div>
              </div>
            </div>




            
            <div class="relative group">
              <p class="text-xl text-center text-main-primary h-[56px] flex items-center cursor-pointer">{{ $t('language') }}</p>
              <div class="absolute right-0 invisible group-hover:visible ease-in-out transition-opacity duration-300 opacity-0 group-hover:opacity-100">
                <div class="py-1">
                  <div class="bg-gray-100 border border-main-primary/40 shadow-sm shadow-black/30 rounded-sm w-[260px]">
                    <div class="grid grid-cols-1 gap-2 px-10 py-2">
                      <nuxt-link :to="switchLocalePath('ru')" class="text-right text-sm text-main-primary font-semibold px-2 py-2">Русский</nuxt-link>
                      <nuxt-link :to="switchLocalePath('en')" class="text-right text-sm text-main-primary font-semibold px-2 py-2">English</nuxt-link>
                      <nuxt-link :to="switchLocalePath('pt')" class="text-right text-sm text-main-primary font-semibold px-2 py-2">Português</nuxt-link>
                      <nuxt-link :to="switchLocalePath('de')" class="text-right text-sm text-main-primary font-semibold px-2 py-2">Deutsch</nuxt-link>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            

          </div>
          <div></div>
        </div>

      </div>      
    </div>


  </div>
</template>