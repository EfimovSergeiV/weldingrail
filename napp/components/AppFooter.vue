<script lang="ts" setup>



</script>


<template>
  <div>
    <div id="contact-us" class=" bg-gradient-to-br from-sky-950 via-sky-900 to-sky-950 min-h- screen grid grid-cols-1 content-center border-t border-white py-2">
      <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8">
        <div class="">
          <div class="">
            <div class="">
              <div class="">
                <div class="flex items-center justify-center border-b border-gray-100/20">
                  <div class="py-4">
                    <p class="text-4xl text-gray-100 uppercase">
                      {{ $t('pages.index.aboutus-title') }}
                    </p>
                  </div>
                </div>
                <div class="py-8">
                  <div class="">
                    <p class="text-2xl text-gray-100 text-center font-sans">
                      {{ $t('pages.index.aboutus-text-1') }}
                    </p>                  
                  </div>
                  <div class="">
                    <p class="text-2xl text-gray-100 text-center font-sans">
                      {{ $t('pages.index.aboutus-text-2') }}
                    </p>                  
                  </div>                  
                </div>


                <div class="my-4">
                  <p class="text-2xl text-gray-100 text-center font-sans">
                    {{ $t('pages.index.aboutus-text-3') }}
                  </p>                  
                </div>
              </div>
              <div class="">
                <div class="flex items-center justify-center py-4">
                  <p class="text-center text-2xl text-gray-100 se lect-none font-sans">{{ $t('pages.index.aboutus-promo') }}</p>
                </div>
                <div class="flex items-end justify-center py-6">
                  <img src="/logo-white.png" class=" h-6"/>
                </div>
              </div>
            </div>
          </div>


          <div class="">

            <div class="flex items-center justify-center py-6">
              <p class="text-white text-xl">Нашими партнёрами уже стали</p>
            </div>

            <div class="grid grid-cols-4 gap-2">
              <div class="px-8">
                <div class="flex items-center justify-center py-2">
                  <img src="/partners/2.png" class="h-12"/>
                </div>
                <div class="flex items-center justify-center py-2">
                  <p class="text-gray-100 text-xs">Kazakh Railways</p>
                </div>
              </div>
              <div class="px-8">
                <div class="flex items-center justify-center py-2">
                  <img src="/partners/1.png" class="h-12"/>
                </div>
                <div class="flex items-center justify-center py-2">
                  <p class="text-gray-100 text-xs">Lithuanian Railways</p>
                </div>
              </div>
              <div class="px-8">
                <div class="flex items-center justify-center py-2">
                  <img src="/partners/3.png" class="h-12"/>
                </div>
                <div class="flex items-center justify-center py-2">
                  <p class="text-gray-100 text-xs">Ozbekiston temir yollari</p>
                </div>
              </div>
              <div class="px-8">
                <div class="flex items-center justify-center py-2">
                  <img src="/partners/4.png" class="h-12"/>
                </div>
                <div class="flex items-center justify-center py-2">
                  <p class="text-gray-100 text-xs">Belarusian railways</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class=" bg-main-dark border-t border-white/40">
      <div class="mx-auto max-w-7xl px-4 lg:max-w-7xl lg:px-8 relative">
        <div class="py-4">
          <div class="flex items-center justify-start py-1">
            <p class="text-xs text-gray-100">Railwelding GmbH 2023</p>
          </div>      
        </div>
      </div>
    </div>
  </div>
</template>