import { ProductForm } from "@models";
import { number, object, string } from "yup";

export const productFormValues : ProductForm = {
    product_id: 0,
    product_name: '',
    price: 0,
    stock_quantity: 0,
    fk_store_id: 0,
    fk_department_id: 0,
    fk_category_id: 0
}

export const productFormValidationSchema = object<ProductForm>({
    product_id: number(),
    product_name: string().required('Product name is required'),
    price: number().required('Price is required').moreThan(0, 'Price is required'),
    stock_quantity: number().required('Stock quantity is required').moreThan(0, 'Stock quantity is required'),
    fk_store_id: number().moreThan(0, 'Select a store to use'),
    fk_department_id: number().moreThan(0, 'Select a department to use'),
    fk_category_id: number().moreThan(0, 'Select a category to use')
})