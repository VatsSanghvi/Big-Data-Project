// * Models
import { User } from "../auth";

interface StoreBase {
    store_id: number;
    store_name: string;
    location: string;
}

export interface Store extends StoreBase {
    manager?: User;
}

export interface StoreForm extends StoreBase {
    fk_owner_id: number;
    manager_email: string;
}