<script lang="ts" setup>
  import { createApp } from 'vue';

  const mainStore = useMainStore()

  const moveUp = () => {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  }


</script>


<template>
  <div class="">
    <transition name="list">
      <div v-if="mainStore.mobileMenu" class="fixed z-50">
        <MobileMenu />
      </div>
    </transition>

    <div class="h-[30px] bg-sky-800">

    </div>

    <AppHeader />


    
    <slot />
    <AppFooter />

    <div id="move-up" class="invisible transition-all duration-900">
      <div class="fixed bottom-4 right-4 z-40">
        <div class="bg-white h-[48px] w-[48px] rounded-full border-2 border-sky-800">
          <div class="flex items-center justify-center h-full w-full">
            <p @click="moveUp()" class="mdi mdi-36px mdi-arrow-up-bold cursor-pointer text-sky-800"></p>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>