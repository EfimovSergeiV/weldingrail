<script setup>


</script>


<template>
  <div class="">


    <div class="h-[100px] bg-white ">
      <!-- <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8">
        <div id="logo" class="">
          <img :src="`/logo-weldingrail.png`" class="" />
        </div>
        <div id="products-menu" class=""></div>

      </div> -->

    </div>
    
    
  <MainSlider />


    <div class="min-h-screen">

    </div>


  </div>
</template>


<style>
  .swiper-pagination {
    position: absolute;
    text-align: left;
    margin-left: 6vw;
    transition: 300ms opacity;
    transform: translate3d(0, 0, 0);
    z-index: 10;
  }
  .swiper-pagination-bullet {
    width: 18px;
    width: var(--swiper-pagination-bullet-width, var(--swiper-pagination-bullet-size, 18px));
    height: 18px;
    height: var(--swiper-pagination-bullet-height, var(--swiper-pagination-bullet-size, 18px));
    display: inline-block;
    border-radius: 50%;
    border-radius: var(--swiper-pagination-bullet-border-radius, 50%);
    background: #0369a1;
    background: var(--swiper-pagination-bullet-inactive-color, #0369a1);
    opacity: 0.5;
    opacity: var(--swiper-pagination-bullet-inactive-opacity, 0.5);
  }
  .swiper-pagination-bullet-active {
    opacity: 1;
    opacity: var(--swiper-pagination-bullet-opacity, 1);
    background: #082f49;
  }
</style>