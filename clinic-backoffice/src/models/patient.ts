import type { City } from './city';
import type { Disease } from './disease';
import type { Regiment } from './regiment';
import type { Presence } from './presence';

export class Patient {
    id!: string;
    name!: string;
    created_at!: Date;
    updated_at!: Date;
    medical_operation_date!: string;
    price!: string;
    doctor!: string;
    number_of_days!: number;
    regiment!: Regiment;
    city!: City;
    state!: City['state'];
    age!: number;
    phone!: string;
    disease!: Disease;
    other_diseases!: string[];
    status!: string;
    presence!: Presence[];
    img_1!: string;
    img_2!: string;
    checkout!: boolean;
    rest!: number;
    sessions!: number;
    surgery!: boolean;
  
    constructor(data: Partial<Patient>) {
      Object.assign(this, data);
    }
  }
