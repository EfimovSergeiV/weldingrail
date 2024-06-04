<script lang="ts" setup>

  const localePath = useLocalePath()
  const { locale, setLocale } = useI18n()
  const switchLocalePath = useSwitchLocalePath()

  const mainStore = useMainStore()


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
      <div id="navbar" class="w-full absolute z-50 duration-50 transition-all">
        <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8 relative ">
          <div class="px-1 flex items-center justify-between gap-12 h-full ">
            <div class="">
              <nuxt-link :to="localePath('index')">
                <img src="/logo-blue.webp" class="h-4 md:h-8" />
              </nuxt-link>                
            </div>

            <div class="flex gap-4 items-center justify-end">

              <div class="">
                <p class="text-sky-900 font-semibold text-base text-center h-[56px] flex items-center uppercase">Версия для Китая</p>
              </div>


              <div class="flex items-center h-full gap-4 bg-red-500/10">
                <nuxt-link :to="switchLocalePath('ru')" class="text-sky-900 font-semibold text-base text-center py-2 uppercase">{{ locale }}</nuxt-link>
                <nuxt-link :to="switchLocalePath('en')" class="text-sky-900 font-semibold text-base text-center py-2 uppercase">EN</nuxt-link>
                <nuxt-link :to="switchLocalePath('zh')" class="text-sky-900 font-semibold text-base text-center py-2 uppercase">CN</nuxt-link>
              </div>




              <div class="md:hidden py-2">
                <div>
                  <div @click="mainStore.mobileMenu = !mainStore.mobileMenu" class="mdi mdi-24px mdi-menu text-sky-900 cursor-pointer"></div>
                </div>
              </div>

            </div>
          </div>




        </div>

      </div>      
    </div>


  </div>
</template>