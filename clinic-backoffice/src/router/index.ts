import { createRouter, createWebHistory } from 'vue-router';
import { useAgentStore } from '@/stores/models/agent';
import OrdersPage from '@/pages/orders/ordersPage.vue';

const routes = [
  {
    meta: {
      title: 'Services',
      requiresAuth: true,
    },
    path: '/services',
    name: 'services',
    component: () => import('@/pages/services/servicePage.vue'),
    children: [
      {
        path: '',
        name: 'services.index',
        component: () => import('@/pages/services/servicesList.vue'),
      },
      {
        path: 'new',
        name: 'services.new',
        component: () => import('@/pages/services/servicesNew.vue'),
      },
      {
        path: 'edit/:id',
        name: 'services.edit',
        component: () => import('@/pages/services/servicesEdit.vue'),
      },
    ],
  },
  {
    meta: {
      title: 'Patients',
      requiresAuth: true,
    },
    path: '/patients',
    name: 'patients',
    component: () => import('@/pages/patients/patientPage.vue'),
    children: [
      {
        path: '',
        name: 'services.index',
        component: () => import('@/pages/patients/patientList.vue'),
      },
      {
        path: 'new',
        name: 'services.new',
        component: () => import('@/pages/patients/patientNew.vue'),
      },
      {
        path: 'edit/:id',
        name: 'services.edit',
        component: () => import('@/pages/patients/patientEdit.vue'),
      },
    ],
  },
  {
    meta: {
      title: 'Sub Services',
    },
    path: '/subservices',
    name: 'SubServices',
    component: () => import('@/pages/subServices/SubServicesPage.vue'),
    children: [
      {
        path: '',
        name: 'subservices.index',
        component: () => import('@/pages/subServices/SubServicesList.vue'),
      },
      {
        path: 'new',
        name: 'subservices.new',
        component: () => import('@/pages/subServices/SubServicesNew.vue'),
      },
      {
        path: 'edit/:id',
        name: 'subservices.edit',
        component: () => import('@/pages/subServices/SubServiceEdit.vue'),
      },
    ],
  },
  {
    meta: {
      title: 'Orders',
    },
    path: '/orders',
    name: 'orders',
    // ...

      component: OrdersPage,
    children: [
      {
        path: '',
        name: 'orders.index',
        component: () => import('@/pages/orders/OrdersList.vue'),
      },
      {
        path: 'new',
        name: 'orders.new',
        component: () => import('@/pages/orders/OrdersNew.vue'),
      },
      {
        path: 'edit/:id',
        name: 'orders.edit',
        component: () => import('@/pages/orders/OrdersEdit.vue'),
      },
    ],
  },
  {
    meta: {
      title: 'Clients',
    },
    path: '/clients',
    name: 'clients',
    component: () => import('@/pages/ClientsView.vue'),
  },
  {
    meta: {
      title: 'Staff',
    },
    path: '/staff',
    name: 'staff',
    component: () => import('@/pages/StaffView.vue'),
  },
  {
    meta: {
      title: 'Profile',
    },
    path: '/profile',
    name: 'profile',
    component: () => import('@/pages/ProfileView.vue'),
  },
  {
    meta: {
      title: 'Login',
      requiresAuth: false,
    },
    path: '/login',
    name: 'login',
    component: () => import('@/pages/LoginView.vue'),
  },
  {
    meta: {
      title: 'Logout',
      requiresAuth: true,
    },
    path: '/logout',
    name: 'logout',
    component: () => import('@/pages/logout.vue'),
  },
  {
    meta: {
      title: 'Not Found',
      requiresAuth: true,
    },
    path: '/:notFound(.*)',
    name: 'notFound',
    redirect: '/services',
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    return savedPosition || { top: 0 };
  },
});
router.beforeEach((to, _from, next) => {
  const store = useAgentStore();
  if (to.name === 'login') {
    next();
  } // login route is always  okay (we could use the requires authModule flag below). prevent a redirect loop
  else if (store.isLoggedIn === true) {
    next(); // i'm logged in. carry on
  } else if (to.meta && to.meta.requiresAuth === false) {
    next(); // requires authModule is explicitly set to false
  } else {
    // always put your redirect as the default case
    next({ name: 'login' }); // redirect to login
  }
});
export default router;
