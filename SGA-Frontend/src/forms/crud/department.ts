// * Third Party Libraries
import { number, object, string } from "yup";

// * Models
import { DepartmentForm } from "@models";

export const departmentFormValues : DepartmentForm = {
    department_id: 0,
    department_name: '',
    fk_store_id: 0,
}

export const departmentFormValidationSchema = object<DepartmentForm>({
    department_id: number(),
    department_name: string().required('Department name is required'),
    fk_store_id: number().moreThan(0, 'Select a store to use')
});