interface GroceryListBase {
  id: number;
  name: string;
  user_id: number;
}

export interface GroceryList extends GroceryListBase {
  total_spent: number;
}

export type GroceryListForm = GroceryListBase
