// * React Libraries
import { FC, useMemo } from "react";

// * Third Party Libraries
import { FormikProps } from "formik";

// * Models
import { BreakpointColumns, Department, Option, ProductForm as IProductForm, Store, Category } from "@models";

// * Helpers
import { getProps } from "@helpers";

// * Components
import { MDropdown, MInputNumber, MInputText } from "@components";

// * Hooks
import { useAppSelector } from "@hooks";

// * Product Form for CRUD operations
export const ProductForm : FC<ProductFormProps> = (props) => {

    const {
        formik
    } = props;

    const { stores, departments, categories } = useAppSelector(state => state.info);

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

    const categoryOptions : Option<number>[] = useMemo(() => {
        return categories
            .filter((category: Category) => category.fk_department_id == formik.values.fk_department_id)
            .map((category: Category) => ({
                label: category.category_name,
                value: category.category_id
            }))
    }, [formik.values.fk_department_id, formik.values.fk_store_id, categories]);

    const breakpoints : BreakpointColumns = {
        sm: 6,
    }

    return (
        <form
            className="product-form"
        >
            <MInputText 
                {...getProps(formik, 'product_name', 'Product Name')}
                columns={12}
                breakpoints={breakpoints}
            />
            <MInputNumber 
                {...getProps(formik, 'stock_quantity', 'Stock Available')}
                columns={12}
                breakpoints={breakpoints}
            />
            <MInputNumber 
                {...getProps(formik, 'price', 'Price')}
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
                    <>
                        <MDropdown 
                            {...getProps(formik, 'fk_department_id', 'Owner Department')}
                            columns={12}
                            breakpoints={breakpoints}
                            options={departmentOptions}
                        />
                        {
                            !!formik.values.fk_department_id && (
                                <MDropdown 
                                    {...getProps(formik, 'fk_category_id', 'Owner Category')}
                                    columns={12}
                                    breakpoints={breakpoints}
                                    options={categoryOptions}
                                />
                            )
                        }
                    </>
                )
            }
        </form>
    )
}

interface ProductFormProps {
    formik: FormikProps<IProductForm>;
}