import type { Patient } from './patient';

export class Order {
    id!: string;
    patient!: Patient;
    created_at!: Date;
    updated_at!: Date;
    amount!: number;
  
    constructor(data: Partial<Order>) {
      Object.assign(this, data);
    }
  }
