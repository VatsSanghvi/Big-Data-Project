// * Third Party Libraries
import { number, object } from "yup";

// * Models
import { GroceryListItemForm } from "@models";

export const groceryListItemInitialValues: GroceryListItemForm = {
  id: 0,
  grocery_list_id: 0,
  product_id: 0,
  quantity: 0,
};

export const groceryListItemValidationSchema = object({
  id: number(),
  grocery_list_id: number(),
  product_id: number(),
  quantity: number().required("Quantity is required"),
});
