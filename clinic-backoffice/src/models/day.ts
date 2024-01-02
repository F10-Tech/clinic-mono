
export class Day {
    id!: string;
    name!: string;
  
    constructor(data: Partial<Day>) {
      Object.assign(this, data);
    }
  }