import { createRouter, createWebHistory } from 'vue-router';
import { useAgentStore } from '@/stores/models/agent';

const routes = [
  {
    meta: {
      title: 'المرضى',
      requiresAuth: true,
    },
    path: '/patients',
    name: 'patients',
    component: () => import('@/pages/patients/patientPage.vue'),
    children: [
      {
        path: '',
        name: 'patients.index',
        component: () => import('@/pages/patients/patientList.vue'),
      },
      {
        path: 'new',
        name: 'patients.new',
        component: () => import('@/pages/patients/patientNew.vue'),
      },
      {
        path: 'edit/:id',
        name: 'patients.edit',
        component: () => import('@/pages/patients/patientEdit.vue'),
      },
    ],
  },
  {
    meta: {
      title: 'الدفع',
      requiresAuth: true,
    },
    path: '/orders',
    name: 'orders',
    component: () => import('@/pages/orders/ordersPage.vue'),
    children: [
      {
        path: '',
        name: 'orders.index',
        component: () => import('@/pages/orders/ordersList.vue'),
      },
    ],
  },
  {
    meta: {
      title: 'فئة الأسعار',
      requiresAuth: true,
    },
    path: '/prices',
    name: 'prices',
    component: () => import('@/pages/prices/pricesPage.vue'),
    children: [
      {
        path: '',
        name: 'prices.index',
        component: () => import('@/pages/prices/pricesList.vue'),
      },
      {
        path: 'new',
        name: 'prices.new',
        component: () => import('@/pages/prices/pricesNew.vue'),
      },
    ],
  },
  {
    meta: {
      title: 'الأمراض',
      requiresAuth: true,
    },
    path: '/diseases',
    name: 'diseases',
    component: () => import('@/pages/diseases/diseasePage.vue'),
    children: [
      {
        path: '',
        name: 'diseases.index',
        component: () => import('@/pages/diseases/diseaseList.vue'),
      },
      {
        path: 'new',
        name: 'diseases.new',
        component: () => import('@/pages/diseases/diseaseNew.vue'),
      },
    ],
  },
  {
    meta: {
      title: 'تسجل الحضور',
      requiresAuth: true,
    },
    path: '/records',
    name: 'records',
    component: () => import('@/pages/records/recordsPage.vue'),
    children: [
      {
        path: '',
        name: 'records.index',
        component: () => import('@/pages/records/recordsList.vue'),
      },
      {
        path: 'presences',
        name: 'records.presences',
        component: () => import('@/pages/records/presenceList.vue'),
      },
    ],
  },
  {
    meta: {
      title: 'الأفواج',
      requiresAuth: true,
    },
    path: '/regiments',
    name: 'regiments',
    component: () => import('@/pages/regiments/regimentsPage.vue'),
    children: [
      {
        path: '',
        name: 'regiments.index',
        component: () => import('@/pages/regiments/regimentsList.vue'),
      },
      {
        path: 'new',
        name: 'regiments.new',
        component: () => import('@/pages/regiments/regimentsNew.vue'),
      },
      {
        path: 'edit/:id',
        name: 'regiments.edit',
        component: () => import('@/pages/regiments/regimentsEdit.vue'),
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
    redirect: '/patients',
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
