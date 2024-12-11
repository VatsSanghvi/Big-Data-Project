import { Category } from "./category";
import { Department } from "./department";
import { Store } from "./store";

interface ProductBase {
    product_id: number;
    product_name: string;
    stock_quantity: number;
    price: number;
}

export interface Product extends ProductBase {
    status: string;
    category: Omit<Category, 'fk_store_id'>,
    department: Department,
    store: Store
}

export interface ProductForm extends ProductBase {
    fk_department_id: number;
    fk_category_id: number;
    fk_store_id: number;
}