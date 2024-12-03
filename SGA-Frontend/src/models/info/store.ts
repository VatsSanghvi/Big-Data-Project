// * Models
import { User } from "../auth";

export interface Store {
    store_id: number;
    store_name: string;
    location: string;
    manager?: User;
}

export interface StoreCreate extends Omit<Store, 'store_id' | 'manager'> {
    fk_owner_id: number;
    manager_email?: string;
}

export interface StoreUpdate extends Omit<Store, 'store_id' | 'manager'> {
    manager_email?: string;
}

export interface StoreForm extends Omit<Store, 'store_id' | 'manager'> {
    fk_owner_id: number;
    manager_email: string;
}