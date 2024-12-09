// * Constants
import { endpoints } from "@constants";

// * Services
import { instance } from "./axiosService";

// * Models
import { GroceryListForm, GroceryListItemForm } from "@models";

export const userProduct = {
  createList: (newGroceryList: GroceryListForm) => {
    return instance.post(endpoints.groceryList.create, newGroceryList);
  },
  addItem: (newGroceryListItem: GroceryListItemForm) => {
    return instance.post(endpoints.groceryList.addItem, newGroceryListItem);
  },
  updateItem(updatedGroceryListItem: GroceryListItemForm) {
    return instance.put(
      endpoints.groceryList.updateItem,
      updatedGroceryListItem
    );
  },
  deleteItem(list_id: number, item_id: number) {
    return instance.delete(
      `${endpoints.groceryList.deleteItem}/${list_id}/${item_id}`
    );
  },
};
