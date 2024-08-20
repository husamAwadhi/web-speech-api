import Home from './../views/Home.vue'
import Read from './../views/Read.vue'
import NotFound from './../views/errors/NotFound.vue'
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/read',
        name: 'Read',
        component: Read
    },
    {
        path: "/:notFound",
        component: NotFound
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes: routes
})

export default router
