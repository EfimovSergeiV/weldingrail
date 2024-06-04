export default defineNuxtPlugin(nuxtApp => {
  if (process.client) {
    window.addEventListener('scroll', () => {
      const scrollPosition = document.documentElement.scrollTop
      // const navBar = document.querySelector('#navbar')
      const navMenu = document.getElementById('navbar')
      const navMoveUp = document.getElementById('move-up')
      // const writeUs = document.getElementById('navbar-style')

      if (scrollPosition > 600) {
        /// Отображение навбара
        navMenu.classList.remove('absolute')
        navMenu.classList.add('fixed', 'bg-white', 'shadow-lg', 'rounded-b-md',)
        navMoveUp.classList.remove('invisible')
        /// Отображение врайт закладки

        // writeUs.classList.remove('invisible')
        // writeUs.classList.add('visible')
        
      } else {
        /// Отображение навбара
        navMenu.classList.remove('fixed', 'bg-white', 'shadow-lg', 'rounded-b-md',)
        navMenu.classList.add('absolute')
        navMoveUp.classList.add('invisible')
        // writeUs.classList.remove('bg-white', 'shadow-lg', 'rounded-b-md')
        /// Отображение врайт закладки
        // writeUs.classList.remove('visible')
        // writeUs.classList.add('invisible')
      }

      // if (scrollPosition > 200) {
      //   navMenu.classList.add('fixed', 'bg-white')

      // } else {
      //   navMenu.classList.remove('fixed', 'bg-white')
      // }

    })    
  }
})
