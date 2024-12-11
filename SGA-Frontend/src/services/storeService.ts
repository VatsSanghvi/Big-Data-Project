// * Models
import { StoreForm } from "@models";

// * Constants
import { endpoints } from "@constants";

// * Services
import { instance } from "./axiosService";

export const store = {
    get: (owner_id: number) => {
        return instance.get(`${endpoints.store.get}/${owner_id}`);
    },
    create: (newStore: StoreForm) => {
        return instance.post(endpoints.store.create, newStore);
    },
    update: (store: StoreForm) => {
        return instance.put(`${endpoints.store.update}/${store.store_id}`, store);
    },
    delete: (store_id: number) => {
        return instance.delete(`${endpoints.store.delete}/${store_id}`);
    }
}