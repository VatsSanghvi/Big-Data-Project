// * Third Party Libraries
import { number, object, string } from "yup";

// * Models
import { GroceryListForm } from "@models";

export const groceryListInitialValues : GroceryListForm = {
    id: 0,
    name: '',
    user_id: 0,
}

export const groceryListValidationSchema = object<GroceryListForm>({
    id: number(),
    name: string().required('Name is required'),
    user_id: number(),
})