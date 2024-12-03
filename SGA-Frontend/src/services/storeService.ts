// * Models
import { StoreCreate, StoreUpdate } from "@models";

// * Constants
import { endpoints } from "@constants";

// * Services
import { instance } from "./axiosService";

export const store = {
    get: (owner_id: number) => {
        return instance.get(`${endpoints.store.get}/${owner_id}`);
    },
    create: (newStore: StoreCreate) => {
        return instance.post(endpoints.store.create, newStore);
    },
    update: (store_id: number, updatedStore: StoreUpdate) => {
        return instance.put(`${endpoints.store.update}/${store_id}`, updatedStore);
    },
    delete: (store_id: number) => {
        return instance.delete(`${endpoints.store.delete}/${store_id}`);
    }
}