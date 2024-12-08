// * React Libraries
import { FC, useMemo } from "react";

// * Third Party Libraries
import { FormikProps } from "formik";

// * Models
import { BreakpointColumns, Department, CategoryForm as ICategoryForm, Option, Store } from "@models";

// * Helpers
import { getProps } from "@helpers";

// * Components
import { MDropdown, MInputText } from "@components";

// * Hooks
import { useAppSelector } from "@hooks";

export const CategoryForm : FC<CategoryFormProps> = (props) => {

    const {
        formik
    } = props;

    const { stores, departments } = useAppSelector(state => state.info);

    const storeOptions : Option<number>[] = useMemo(() => {
        return stores.map((store : Store) => ({
            label: store.store_name,
            value: store.store_id
        }))
    }, [stores]);

    const departmentOptions : Option<number>[] = useMemo(() => {
        return departments
            .filter((department: Department) => department.fk_store_id == formik.values.fk_store_id)
            .map((department: Department) => ({
                label: department.department_name,
                value: department.department_id
            }))
    }, [formik.values.fk_store_id, departments]);

    const breakpoints : BreakpointColumns = {
        sm: 6,
    }

    return (
        <form
            className="category-form"
        >
            <MInputText 
                {...getProps(formik, 'category_name', 'Category Name')}
                columns={12}
                breakpoints={breakpoints}
            />
            <MDropdown 
                {...getProps(formik, 'fk_store_id', 'Owner Store')}
                columns={12}
                breakpoints={breakpoints}
                options={storeOptions}
            />
            {
                !!formik.values.fk_store_id && (
                    <MDropdown 
                        {...getProps(formik, 'fk_department_id', 'Owner Department')}
                        columns={12}
                        breakpoints={breakpoints}
                        options={departmentOptions}
                    />
                )
            }
        </form>
    )
}

interface CategoryFormProps {
    formik: FormikProps<ICategoryForm>;
}