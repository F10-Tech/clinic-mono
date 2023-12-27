// import type { Product } from './product';

export class Order {
  id!: string;
  created_at!: Date;
  scheduled!: Date;
  state!: 'CANCELLED' | 'COMPLETED' | 'INPROGRESS' | 'REJECTED' | 'PENDING';
  price!: number;
  location?: string;
  customer!: OrderCustomer;
  subservice!: OrderSubservice;
  service!: OrderService;

  constructor(data: Partial<Order>) {
    Object.assign(this, data);
  }
}

export class OrderSubservice {
  id?: string;
  name_fr?: string;
  name_en?: string;
  name_ar!: string;

  constructor(data: Partial<OrderSubservice>) {
    Object.assign(this, data);
  }
}
export class OrderService {
  image_light?: string;
  image_dark?: string;
  name_fr?: string;
  name_en?: string;
  name_ar!: string;

  constructor(data: Partial<OrderService>) {
    Object.assign(this, data);
  }
}
export class OrderCustomer {
  last_name?: string;
  first_name?: string;
  phone?: string;

  constructor(data: Partial<OrderCustomer>) {
    Object.assign(this, data);
  }
}
