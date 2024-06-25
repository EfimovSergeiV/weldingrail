<script lang="ts" setup>
  import { createApp } from 'vue';
  const { locale, setLocale } = useI18n()
  const localePath = useLocalePath()
  const config = useRuntimeConfig()
  const mainStore = useMainStore()

  const route = useRoute()
  const router = useRouter()


  const moveUp = () => {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  }

  // const fontClass = computed(() => {
  //   const currentLocale = locale.value
  //   return `font-${currentLocale}`
  // })

  const fontClass = computed(() => {
    const currentLocale = locale.value
    return `font-${currentLocale}`
  })

  onMounted( async () => {
    const selectors = document.querySelectorAll("div.sec")
    // console.log(selectors)

    const scrollHeight = Math.max(
      document.documentElement.scrollHeight,
      document.body.scrollHeight
    )

    // console.log(scrollHeight)


  })


</script>


<template>
  <div id="weldingrail" :class="`${fontClass} bg-gray-100 min-w-7xl`">
    <transition name="list">
      <div v-if="mainStore.mobileMenu" class="fixed z-50">
        <MobileMenu />
      </div>
    </transition>


    
    <div class="min-h-[48px]">
      <AppHeader />
    </div>


    <!-- <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8 pt-4">
      <MainSlider />
    </div> -->


    
    <slot />
    <!-- <AppFooter :categories="categories"/> -->

    <div id="move-up" class="invisible transition-all duration-900">
      <div class="fixed bottom-4 right-4 z-40">
        <div class="">
          <div class="flex items-center justify-center h-full w-full">
            <p @click="moveUp()" class="mdi mdi-48px mdi-arrow-up-bold-hexagon-outline cursor-pointer text-sky-900"></p>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>