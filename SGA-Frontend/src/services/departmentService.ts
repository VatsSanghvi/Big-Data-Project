import { endpoints } from "@constants";
import { instance } from "./axiosService";
import { DepartmentForm } from "@models";

export const department = {
    get: (store_id: number) => {
        return instance.get(`${endpoints.department.get}/${store_id}`);
    },
    create: (newDepartment: DepartmentForm) => {
        return instance.post(endpoints.department.create, newDepartment);
    },
    update: (department: DepartmentForm) => {
        return instance.put(`${endpoints.department.update}/${department.department_id}`, department);
    },
    delete: (department_id: number) => {
        return instance.delete(`${endpoints.department.delete}/${department_id}`);
    }
}