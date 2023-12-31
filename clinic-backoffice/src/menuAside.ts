import {
  mdiAccountGroupOutline,
  mdiAccountOutline ,
  mdiClipboardListOutline,
  mdiClipboardTextMultipleOutline,
  mdiListBox ,
} from '@mdi/js';

export default [
  {
    to: '/patients',
    label: 'المرضى',
    icon: mdiAccountOutline ,
  },
  {
    to: '/records',
    label: 'الحضور',
    icon: mdiListBox,
  },
  {
    to: '/diseases',
    label: 'الأمراض',
    icon: mdiClipboardTextMultipleOutline,
  },
  {
    to: '/regiment',
    label: 'الأفواج',
    icon: mdiAccountGroupOutline ,
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
