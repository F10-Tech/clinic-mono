export class Service {
  id!: string;
  name_AR!: string;
  name_EN!: string;
  name_FR!: string;
  description_AR!: string;
  description_EN!: string;
  description_FR!: string;
  image_light?: string;
  image_dark?: string;
  is_active!: boolean;

  constructor(data: Partial<Service>) {
    Object.assign(this, data);
  }
}
export class SubserviceService {
  id!: string;
  name_EN!: string;

  constructor(data: Partial<SubserviceService>) {
    Object.assign(this, data);
  }
}
