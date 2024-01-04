import type { Patient } from './patient';

export class Price {
    id!: string;
    name!: Patient;
    price!: number;
    created_at!: Date;
    updated_at!: Date;
  
    constructor(data: Partial<Price>) {
      Object.assign(this, data);
    }
  }
