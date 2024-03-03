// import type { Product } from './product';

export class Doctor {
    id!: string;
    name!: string;
  
    constructor(data: Partial<Doctor>) {
      Object.assign(this, data);
    }
  }