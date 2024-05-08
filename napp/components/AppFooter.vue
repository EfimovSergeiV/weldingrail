<script setup>

  const currentData = new Date().getFullYear()

  const moveUp = () => {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  }


</script>


<template>
  <div>

    <div class="bg-sky-950 min-h-[320px]">
      <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8 h-full">        
        <div class="grid grid-cols-1 content-between h-full">

          <div class="text-white py-8">
            <!-- <div class="flex items-center justify-between">
              <div class="">
                <p class="">Hallo welt</p>
              </div>
              <div class="">
                <p class="">Hallo welt</p>
              </div>
            </div> -->
          </div>

          <div class="flex items-center justify-center lg:max-w-7xl py-4">
            <div class="grid grid-cols-1 gap-2">
              <p class="text-white text-4xl text-center">Подписывайтесь на нашу новостную рассылку</p>
              <p class="text-white text-base text-center py-2">Будьте первым, кто узнает последние новости о тенденциях в сварочных технологиях!</p>
              <div id="subscriebe" class="flex gap-0.5 py-4">
                <input type="email" class="w-[640px] text-center h-12 px-4 text-2xl text-sky-900 bg-white border border-white/0 focus:border-white/0 focus:ring-gray-600/0 ring-0 placeholder-sky-800" placeholder="Enter your email address" /> 
                <button class="h-12 px-4 text-lg text-white bg-sky-700 w-[260px]">Join</button>
              </div>
            </div>
          </div>

        </div>
      </div>
    </div>

    
    <div class=" bg-gradient-to-br from-sky-950 via-sky-900 to-sky-950 min-h- screen grid grid-cols-1 content-center border-t border-white/20">
      <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8">
        <div class="">
          <div class="flex items-end justify-center py-4">
            <div class="grid grid-cols-1 gap-2 text-center">
              <img @click="moveUp()" src="/logo-white.webp" class="h-8 cursor-pointer"/>        
              <p class="text-xs text-gray-100">weldingrail.com | {{ currentData }} (c)</p>
            </div>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>