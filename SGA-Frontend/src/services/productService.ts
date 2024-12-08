// * Models
import { ProductForm } from "@models";

// * Services
import { instance } from "./axiosService";

// * Constants
import { endpoints } from "@constants";

export const product = {
    get: (owner_id: number) => {
        return instance.get(`${endpoints.product.get}/${owner_id}`);
    },
    create: (newProduct: ProductForm) => {
        return instance.post(endpoints.product.create, newProduct);
    },
    update: (product: ProductForm) => {
        return instance.put(`${endpoints.product.update}/${product.product_id}`, product);
    },
    delete: (product_id: number) => {
        return instance.delete(`${endpoints.product.delete}/${product_id}`);
    }
}