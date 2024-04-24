import { type } from 'os'
import { defineStore } from 'pinia'


export const useMainStore = defineStore('MainStore', {
    /// Хранение данных о магазинах
    state: () => ({
      mobileMenu: false,
    }),
    actions: {
      // selectCityMaps(city: any) {
      //   this.city = city
      // },
    },
  })