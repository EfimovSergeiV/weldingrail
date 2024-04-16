<script lang="ts" setup>
  import { createApp } from 'vue';

  const moveUp = () => {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  }


</script>


<template>
  <div class="">
    <AppHeader />
    <slot />
    <AppFooter />

    <div id="move-up" class="invisible transition-all duration-900">
      <div class="fixed bottom-0 right-0 z-50">
        <div class="flex items-center justify-center">
          <div class="px-6 py-6">
            <div @click="moveUp()" class="mdi mdi-48px mdi-arrow-up-bold-hexagon-outline cursor-pointer text-sky-600">

            </div>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>