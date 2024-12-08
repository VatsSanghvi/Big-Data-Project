// * React Libraries
import { useState } from "react";

// * Third Party Libraries
import { useFormik } from "formik";
import { confirmDialog, ConfirmDialog } from "primereact/confirmdialog"
import { DataView } from "primereact/dataview";
import { TabPanel, TabView } from "primereact/tabview";

// * Components
import { AddButton, CategoryDialog, CategoryListTemplate, PageTitle } from "@components";

// * Forms
import { categoryFormValidationSchema, categoryFormValues } from "@forms";

// * Hooks
import { useAppDispatch, useAppSelector, useToast } from "@hooks";

// * Models
import { Category, CategoryForm, Department, DialogMode, Store } from "@models";

// * Services
import { category } from "@services";

// * Store
import { addCategory, deleteCategory, updateCategory } from "@store";

export const CategoriesPage = () => {
    const { showSuccess, showError } = useToast();

    const { stores, departments, categories } = useAppSelector(state => state.info);
    const dispatch = useAppDispatch();

    const [openMode, setOpenMode] = useState<DialogMode>(DialogMode.CLOSE);

    const { create, update } = category;

    const formik = useFormik<CategoryForm>({
        initialValues: categoryFormValues,
        validationSchema: categoryFormValidationSchema,
        onSubmit: async(values) => {
            console.log(values);

            const { data } = await (openMode === DialogMode.CREATE ? create : update)(values);
            
            if (data.ok) {
                setOpenMode(DialogMode.CLOSE);

                const newCategory : Category = {
                    ...data.data,
                    fk_store_id: values.fk_store_id
                }

                dispatch((openMode === DialogMode.CREATE ? addCategory : updateCategory)(newCategory));
                showSuccess('Success', `Store ${openMode === DialogMode.CREATE ? 'Created' : 'Updated'} Successfully`);
            } else {
                showError('Error', 'Something went wrong');   
            }
        }
    });

    const onCreate = () => {
        formik.resetForm();
        setOpenMode(DialogMode.CREATE);
    };

    const onEdit = (category: Category) => {
        formik.setValues(category);

        setOpenMode(DialogMode.EDIT);
    };

    const onAcceptDelete = async(category_id: number) => {
        const { data } = await category.delete(category_id);

        if (data.ok) {
            showSuccess('Success', 'Category Deleted Successfully');
            dispatch(deleteCategory(category_id))
        } else {
            showError('Error', 'Something went wrong');
        }
    };

    const onDelete = (category_id: number) => {
        confirmDialog({
            message: 'Do you want to delete this category?',
            header: 'Delete Category',
            icon: 'pi pi-exclamation-triangle',
            accept: () => onAcceptDelete(category_id)
        });
    };

    const getDepartments = (store_id : number) => {
        return departments.filter((department: Department) => department.fk_store_id === store_id);
    };

    const getCategories = (department_id: number) => {
        return categories.filter((category: Category) => category.fk_department_id === department_id)
    }

    const listTemplate = (items: Category[]) => (
        <CategoryListTemplate
            items={items}
            onDelete={onDelete}
            onEdit={onEdit}
        />
    );

    return (
        <>
            <PageTitle title="Categories Manager"/>
            <AddButton 
                label="Create New Category"
                onClick={onCreate}
            />
            <div className="h-full overflow-auto">
                <TabView>
                    {
                        stores.map((store : Store) => (
                            <TabPanel 
                                key={store.store_id}
                                header={store.store_name}
                            >
                                <TabView>
                                    {
                                        getDepartments(store.store_id).map((department: Department) => (
                                            <TabPanel
                                                key={department.department_id}
                                                header={department.department_name}
                                            >
                                                <DataView
                                                    paginator
                                                    className="h-full"
                                                    rows={4}
                                                    value={getCategories(department.department_id)}
                                                    listTemplate={listTemplate}
                                                />
                                            </TabPanel>
                                        ))
                                    }
                                </TabView>
                            </TabPanel>
                        ))
                    }
                </TabView>
            </div>
            <CategoryDialog 
                openMode={openMode}
                setOpenMode={setOpenMode}
                formik={formik}
            />
            <ConfirmDialog />
        </>
    )
}