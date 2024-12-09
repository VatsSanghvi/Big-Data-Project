// * Constants
import { endpoints } from "@constants";

// * Services
import { instance } from "./axiosService";

// * Models
import { GroceryListForm, GroceryListItemForm } from "@models";

export const userProduct = {
  getGroceryList: (user_id: number) => {
    return instance.get(`${endpoints.groceryList.get}/${user_id}`);
  },
  createGroceryList: (newGroceryList: GroceryListForm) => {
    return instance.post(endpoints.groceryList.create, newGroceryList);
  },
  deleteGroceryList: (list_id: number) => {
    return instance.delete(`${endpoints.groceryList.delete}/${list_id}`);
  },
  addItem: (newGroceryListItem: GroceryListItemForm) => {
    return instance.post(endpoints.groceryList.addItem, newGroceryListItem);
  },
  updateItem(updatedGroceryListItem: GroceryListItemForm) {
    return instance.put(`${endpoints.groceryList.updateItem}/${updatedGroceryListItem.grocery_list_id}/${updatedGroceryListItem.id}`, updatedGroceryListItem);
  },
  deleteItem(list_id: number, item_id: number) {
    return instance.delete(
      `${endpoints.groceryList.deleteItem}/${list_id}/${item_id}`
    );
  },
};
