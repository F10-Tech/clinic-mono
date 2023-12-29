import {
  mdiAccountGroupOutline,
  mdiCartOutline,
  mdiClipboardListOutline,
  mdiClipboardTextMultipleOutline,
  mdiAccountTieOutline,
} from '@mdi/js';

export default [
  {
    to: '/services',
    label: 'Services',
    icon: mdiClipboardListOutline,
  },
  {
    to: '/patients',
    label: 'المرضى',
    icon: mdiClipboardListOutline,
  },
  {
    to: '/subservices',
    label: 'Subservices',
    icon: mdiClipboardTextMultipleOutline,
  },
  {
    to: '/orders',
    label: 'Orders',
    icon: mdiCartOutline,
  },
  {
    to: '/clients',
    label: 'Clients',
    icon: mdiAccountGroupOutline,
  },
  {
    to: '/staff',
    label: 'Staff',
    icon: mdiAccountTieOutline,
  },
];
