// import type { Product } from './product';

export class Patient {
    id!: string;
    name!: string;
    created_at!: Date;
    updated_at!: Date;
    medical_operation_date!: Date;
    doctor!: string;
    number_of_days!: number;
    regiment!: PatientRegiment;
    city!: PatientCity;
    age!: number;
    phone!: string;
    disease!: PatientDisease;
    other_diseases!: string[];
    status!: string;
    presence!: PatientPresence[];
    img_1!: string;
    img_2!: string;
  
    constructor(data: Partial<Patient>) {
      Object.assign(this, data);
    }
  }
export class PatientDisease {
  id?: string;
  name?: string;

  constructor(data: Partial<PatientDisease>) {
    Object.assign(this, data);
  }
}

// export class OtherDiseases {
//   id?: string;

//   constructor(data: Partial<OtherDiseases>) {
//     Object.assign(this, data);
//   }
// }


export class PatientPresence {
  day?: string;
  created_at?: Date;
  id?: string;

  constructor(data: Partial<PatientDisease>) {
    Object.assign(this, data);
  }
}
  export class PatientRegiment {
    id?: string;
    name?: string;
    days?: string[];
  
    constructor(data: Partial<PatientRegiment>) {
      Object.assign(this, data);
    }
  }
  
  export class PatientCity {
    id?: string;
    name?: string;
    state?: CityState;
  
    constructor(data: Partial<PatientCity>) {
      Object.assign(this, data);
    }
  }
  
  export class CityState {
    name?: string;
  
    constructor(data: Partial<CityState>) {
      Object.assign(this, data);
    }
  }