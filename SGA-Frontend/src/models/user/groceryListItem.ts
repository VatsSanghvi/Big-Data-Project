interface GroceryListItemBase {
  id: number;
  quantity: number;
  grocery_list_id: number;
  product_id: number;
}

export type GroceryListItem = GroceryListItemBase

export type GroceryListItemForm = GroceryListItemBase
