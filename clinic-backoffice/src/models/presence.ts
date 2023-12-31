

export class Presence {
    id! : string;
    day!: string;
    created_at!: Date;
    patient!: string;
  
    constructor(data: Partial<Presence>) {
      Object.assign(this, data);
    }
  }