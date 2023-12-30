

export class Presence {
    day?: string;
    created_at?: Date;
    id?: string;
  
    constructor(data: Partial<Presence>) {
      Object.assign(this, data);
    }
  }