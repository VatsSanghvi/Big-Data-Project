import { StoreForm } from "@models";
import { number, object, string } from "yup";

export const storeFormValues : StoreForm = {
    store_id: 0,
    store_name: '',
    location: '',
    fk_owner_id: 0,
    manager_email: ''
}

export const storeFormValidationSchema = object<StoreForm>({
    store_id: number(),
    store_name: string().required('Store name is required'),
    location: string().required('Location is required'),
    fk_owner_id: number(),
    manager_email: string()
        .email('It must be a valid email')
        .notRequired()
})