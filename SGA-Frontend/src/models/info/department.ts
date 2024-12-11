interface DepartmentBase {
    department_id: number;
    department_name: string;
    fk_store_id: number;
}

export type Department = DepartmentBase

export type DepartmentForm = DepartmentBase