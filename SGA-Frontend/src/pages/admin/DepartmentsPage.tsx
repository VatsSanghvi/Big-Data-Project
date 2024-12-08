import { AddButton, DepartmentDialog, DepartmentListTemplate, PageTitle } from "@components"
import { departmentFormValidationSchema, departmentFormValues } from "@forms";
import { useAppDispatch, useAppSelector, useToast } from "@hooks";
import { Department, DepartmentForm, DialogMode, Store } from "@models";
import { department } from "@services";
import { addDepartment, deleteDepartment, updateDepartment } from "@store";
import { useFormik } from "formik";
import { confirmDialog, ConfirmDialog } from "primereact/confirmdialog"
import { DataView } from "primereact/dataview";
import { TabPanel, TabView } from "primereact/tabview";
import { useState } from "react";

export const DepartmentsPage = () => {

    const { showSuccess, showError } = useToast();

    const { stores, departments } = useAppSelector(state => state.info);
    const dispatch = useAppDispatch();

    const [openMode, setOpenMode] = useState<DialogMode>(DialogMode.CLOSE);

    const { create, update } = department;

    const formik = useFormik<DepartmentForm>({
        initialValues: departmentFormValues,
        validationSchema: departmentFormValidationSchema,
        onSubmit: async(values) => {
            console.log(values);

            const { data } = await (openMode === DialogMode.CREATE ? create : update)(values);
            
            if (data.ok) {
                setOpenMode(DialogMode.CLOSE);

                const newDepartment : Department = {
                    ...data.data,
                    fk_store_id: values.fk_store_id
                }

                dispatch((openMode === DialogMode.CREATE ? addDepartment : updateDepartment)(newDepartment));
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

    const onEdit = (department: Department) => {
        formik.setValues({
            ...department
        });

        setOpenMode(DialogMode.EDIT);
    };

    const onAcceptDelete = async(department_id: number) => {
        const { data } = await department.delete(department_id);

        if (data.ok) {
            showSuccess('Success', 'Department Deleted Successfully');
            dispatch(deleteDepartment(department_id))
        } else {
            showError('Error', 'Something went wrong');
        }
    };

    const onDelete = (department_id: number) => {
        confirmDialog({
            message: 'Do you want to delete this department?',
            header: 'Delete Department',
            icon: 'pi pi-exclamation-triangle',
            accept: () => onAcceptDelete(department_id)
        });
    };

    const getDepartments = (store_id : number) => {
        return departments.filter((department: Department) => department.fk_store_id === store_id);
    };

    const listTemplate = (items: Department[]) => (
        <DepartmentListTemplate 
            items={items}
            onDelete={onDelete}
            onEdit={onEdit}
        />
    );

    return (
        <>
            <PageTitle title="Departments Manager" />
            <AddButton 
                label="Create New Department"
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
                                <DataView 
                                    paginator
                                    className="h-full"
                                    rows={4}
                                    value={getDepartments(store.store_id)}
                                    listTemplate={listTemplate}
                                />
                            </TabPanel>
                        ))
                    }
                </TabView>
            </div>
            <DepartmentDialog 
                openMode={openMode}
                setOpenMode={setOpenMode}
                formik={formik}
            />
            <ConfirmDialog />
        </>
    )
}