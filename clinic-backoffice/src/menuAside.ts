import {
  mdiAccountGroup,
  mdiClipboardList ,
  mdiReceiptTextPlus,
  mdiListBox ,
  mdiAccount,
  mdiMedicalBag,
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
