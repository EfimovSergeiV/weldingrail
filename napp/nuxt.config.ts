// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  
  app: {
    head: {
      title: 'Rail Welding Solutions',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { 
          hid: 'description', 
          name: 'description', 
          content: 'Rail Welding'
        },
        { name: 'format-detection', content: 'telephone=yes' }
      ],
      link: [
        { rel: 'icon', type: 'image/x-icon', href: '/favicon.png' }
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
    '@nuxtjs/tailwindcss'
  ],

  runtimeConfig: {
    public: {
      baseURL: process.env.BASE_URL || 'http://127.0.0.1:8000/',
    },
  },

  plugins: [
    { src: '~/plugins/bg-scroll.js', mode: 'client' },
    { src: '~/plugins/navbar.js', mode: 'client' },
  ],

  css: [
    '@/assets/css/main.css',
    '@/assets/css/tailwind.css',
    '@mdi/font/css/materialdesignicons.min.css',
  ],

  i18n: {
    strategy: 'prefix_except_default',
    defaultLocale: 'ru',
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
        code: 'ru',
        iso: 'ru-RU',
        file: 'ru-RU.json'
      },
      {
        code: 'pt',
        iso: 'pt-PT',
        file: 'pt-PT.json'
      },
      {
        code: 'de',
        iso: 'de-DE',
        file: 'de-DE.json'
      }
    ],
    lazy: true,
    langDir: 'lang/',
  },

})
