interface GroceryListBase {
  id: number;
  name: string;
  user_id: number;
}

export interface GroceryList extends GroceryListBase {
  id: number;
  name: string;
  total_spent: number;
  user_id: number;
}

export interface GroceryListForm extends GroceryListBase {
  name: string;
  user_id: number;
}
