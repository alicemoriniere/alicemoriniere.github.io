import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../HomeView.vue'
import ResearchView from '../ResearchView.vue'
import TeachingView from '../TeachingView.vue'
import AgregView from '../AgregView.vue'
import MiscView from '../MiscView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', component: HomeView },
    { path: '/recherche', component: ResearchView },
    { path: '/agreg', component: AgregView },
    { path: '/divers', component: MiscView },
    { path: '/enseignements', component: TeachingView },
  ],
})

export default router
