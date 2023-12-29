// import type { Product } from './product';

export class Disease {
    id!: string;
    name!: string;
  
    constructor(data: Partial<Disease>) {
      Object.assign(this, data);
    }
  }