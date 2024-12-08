interface CategoryBase {
    category_id: number;
    category_name: string;
    fk_department_id: number;
}

export type Category = CategoryBase

export type CategoryForm = CategoryBase