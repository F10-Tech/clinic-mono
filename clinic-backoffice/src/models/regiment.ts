// import type { Product } from './product';

export class Regiment {
    id!: string;
    name!: string;
    days!: string[];
    period!: string;
  
    constructor(data: Partial<Regiment>) {
      Object.assign(this, data);
    }
  }