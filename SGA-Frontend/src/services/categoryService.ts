// * Models
import { CategoryForm } from "@models";

// * Services
import { instance } from "./axiosService";

// * Constants
import { endpoints } from "@constants";

export const category = {
    get: (owner_id: number) => {
        return instance.get(`${endpoints.category.get}/${owner_id}`);
    },
    create: (newCategory: CategoryForm) => {
        return instance.post(endpoints.category.create, newCategory);
    },
    update: (category: CategoryForm) => {
        return instance.put(`${endpoints.category.update}/${category.category_id}`, category);
    },
    delete: (category_id: number) => {
        return instance.delete(`${endpoints.category.delete}/${category_id}`);
    }
}