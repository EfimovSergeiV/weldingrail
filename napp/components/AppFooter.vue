<script setup>

const currentData = new Date().getFullYear()

</script>


<template>
  <div>

    <div class="bg-sky-950 h-[320px]">
      <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8">
        sadasd
      </div>
    </div>

    
    <div class=" bg-gradient-to-br from-sky-950 via-sky-900 to-sky-950 min-h- screen grid grid-cols-1 content-center border-t border-white/20">
      <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8">
        <div class="">
          <div class="flex items-end justify-center py-4">
            <div class="grid grid-cols-1 gap-2 text-center">
              <img src="/logo-white.webp" class="h-8"/>        
              <p class="text-xs text-gray-100">weldingrail.com | {{ currentData }} (c)</p>
            </div>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>