// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  
  app: {
    head: {
      title: 'WeldingRail Equipment',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1.0, minimum-scale=1.0' },
        { 
          hid: 'description', 
          name: 'description', 
          content: 'WeldingRail Equipment'
        },
        { name: 'format-detection', content: 'telephone=yes' }
      ],
      link: [
        { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
      ]
    },

    pageTransition: { 
      name: 'page', 
      mode: 'out-in' 
    },

  },

  modules: [
    '@nuxtjs/i18n',
    '@pinia/nuxt',
    '@nuxtjs/tailwindcss',
    'nuxt-swiper',
  ],

  runtimeConfig: {
    public: {
      baseURL: process.env.BASE_URL || 'http://192.168.60.201:8080/', ///'http://192.168.60.201:8080/', 'http://127.0.0.1:8000/'
    },
  },

  plugins: [
    // { src: '~/plugins/bg-scroll.js', mode: 'client' },
    { src: '~/plugins/navbar.js', mode: 'client' },
  ],

  css: [
    '@/assets/css/main.css',
    '@/assets/css/tailwind.css',
    '@mdi/font/css/materialdesignicons.min.css',
  ],

  i18n: {
    strategy: 'prefix_except_default',
    defaultLocale: 'en',
    detectBrowserLanguage: {
      useCookie: true,
      cookieKey: 'i18n_redirected',
      redirectOn: 'root',  // recommended
    },
    // baseUrl: 'https://my-nuxt-app.com',
    locales: [
      {
        code: 'en',
        iso: 'en-US',
        file: 'en-US.json'
      },
      {
        code: 'zh',
        iso: 'zh-ZH',
        file: 'zh-ZH.json'
      },
      {
        code: 'de',
        iso: 'de-DE',
        file: 'de-DE.json'
      },
      {
        code: 'ru',
        iso: 'ru-RU',
        file: 'ru-RU.json'
      },
    ],
    lazy: true,
    langDir: 'lang/',
  },

})
