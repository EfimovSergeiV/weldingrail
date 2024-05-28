<script lang="ts" setup>
  import { createApp } from 'vue';
  const { locale, setLocale } = useI18n()

  const mainStore = useMainStore()

  const moveUp = () => {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  }

  const fontClass = computed(() => {
    const currentLocale = locale.value
    return `font-${currentLocale}`
  })

</script>


<template>
  <div :class="`${fontClass} bg-gray-100`">
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
    <AppFooter />

    <div id="move-up" class="invisible transition-all duration-900">
      <div class="fixed bottom-4 right-4 z-40">
        <div class="bg-white h-[48px] w-[48px] rounded-full border-2 border-sky-800">
          <div class="flex items-center justify-center h-full w-full">
            <p @click="moveUp()" class="mdi mdi-36px mdi-arrow-up-bold cursor-pointer text-sky-900"></p>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>