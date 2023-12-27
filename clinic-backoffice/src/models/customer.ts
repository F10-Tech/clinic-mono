export class Customer {
  id!: string;
  first_name!: string;
  last_name!: string;
  username!: string;
  email!: string;
  phone!: number;

  constructor(data: Partial<Customer>) {
    Object.assign(this, data);
  }
}
