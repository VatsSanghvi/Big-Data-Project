interface GroceryListItemBase {
  id: number;
  name: string;
  total_spent: number;
}

export interface GroceryListItem extends GroceryListItemBase {
  quantity: number;
  grocery_list_id: number;
  product_id: number;
}

export interface GroceryListItemForm extends GroceryListItemBase {
  quantity: number;
  grocery_list_id: number;
  product_id: number;
}
