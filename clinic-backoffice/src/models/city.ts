import type { State } from './state';


export class City {
    id!: string;
    name!: string;
    state!: string;

    constructor(data: Partial<City>) {
      Object.assign(this, data);
    }
  }
