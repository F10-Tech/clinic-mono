import {
  mdiAccountGroupOutline,
  mdiAccountOutline ,
  mdiClipboardListOutline,
  mdiClipboardTextMultipleOutline,
  mdiListBox ,
} from '@mdi/js';

export default [
  // {
  //   to: '/services',
  //   label: 'Services',
  //   icon: mdiClipboardListOutline,
  // },
  {
    to: '/patients',
    label: 'المرضى',
    icon: mdiAccountOutline ,
  },
  {
    to: '/presences',
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
