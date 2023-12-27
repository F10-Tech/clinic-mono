export const convertToDict = (data: any[]) => {
  const dict = {};
  const order: number[] = [];
  data.forEach((elt) => {
    order.push(elt.id);
    dict[elt.id] = elt;
  });
  return { all: dict, order };
};

export type baseType<T> = {
  all: { [id: string]: T };
  order: number[];
  filteredIds: string[];
  filterQuery: string;
  selectedId?: string;
  editedId?: string;
};
