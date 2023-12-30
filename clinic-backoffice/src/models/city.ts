import type { State } from './state';


export class City {
    id!: string;
    name!: string;
    state!: State;

    constructor(data: Partial<City>) {
      Object.assign(this, data);
    }
  }
