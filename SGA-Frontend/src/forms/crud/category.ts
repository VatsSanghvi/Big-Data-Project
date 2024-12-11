// * Third Party Libraries
import { number, object, string } from "yup";

// * Models
import { CategoryForm } from "@models";

export const categoryFormValues : CategoryForm = {
    category_id: 0,
    category_name: '',
    fk_store_id: 0,
    fk_department_id: 0,
}

export const categoryFormValidationSchema = object<CategoryForm>({
    category_id: number(),
    category_name: string().required('Category name is required'),
    fk_store_id: number().moreThan(0, 'Select a store to use'),
    fk_department_id: number().moreThan(0, 'Select a department to use')
});