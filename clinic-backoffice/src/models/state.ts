

export class State {
    id!: string;
    name!: string;

    constructor(data: Partial<State>) {
      Object.assign(this, data);
    }
  }