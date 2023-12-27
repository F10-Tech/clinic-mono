export class Subservice {
  id!: string;
  name_AR!: string;
  name_EN!: string;
  name_FR!: string;
  description_AR!: string;
  description_EN!: string;
  description_FR!: string;
  min_price!: number;
  image_light?: string;
  image_dark?: string;
  is_active!: boolean;
  service!: string;

  constructor(data: Partial<Subservice>) {
    Object.assign(this, data);
  }
}
