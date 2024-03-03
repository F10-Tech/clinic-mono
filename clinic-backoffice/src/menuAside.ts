import {
  mdiAccountGroup,
  mdiClipboardList ,
  mdiReceiptTextPlus,
  mdiCashClock ,
  mdiAccount,
  mdiMedicalBag,
  mdiCash,
} from '@mdi/js';

export default [
  {
    to: '/patients',
    label: 'المرضى',
    icon: mdiAccount ,
  },
  {
    to: '/records',
    label: 'تسجيل الحضور',
    icon: mdiReceiptTextPlus,
  },
  {
    to: '/records/presences',
    label: 'لإحة الحضور',
    icon: mdiClipboardList,
  },
  {
    to: '/diseases',
    label: 'الأمراض',
    icon: mdiMedicalBag,
  },
  {
    to: '/regiments',
    label: 'الأفواج',
    icon: mdiAccountGroup ,
  },
  {
    to: '/orders',
    label: 'الدفع',
    icon: mdiCashClock ,
  },
  {
    to: '/prices',
    label: 'فئة الاسعار',
    icon: mdiCash ,
  },
  {
    to: '/doctors',
    label: 'الطبيب',
    icon: mdiAccount ,
  },
  // {
  //   to: '/clients',
  //   label: 'Clients',
  //   icon: mdiAccountGroupOutline,
  // },
  // {
  //   to: '/staff',
  //   label: 'Staff',
  //   icon: mdiAccountTieOutline,
  // },
];
