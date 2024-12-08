// * React Libraries
import { useState } from "react";

// * Third Party Libraries
import { useFormik } from "formik";
import { confirmDialog, ConfirmDialog } from "primereact/confirmdialog"
import { DataView } from "primereact/dataview";
import { TabPanel, TabView } from "primereact/tabview";

// * Components
import { AddButton, DepartmentDialog, DepartmentListTemplate, PageTitle } from "@components"

// * Forms
import { departmentFormValidationSchema, departmentFormValues } from "@forms";

// * Hooks
import { useAppDispatch, useAppSelector, useToast } from "@hooks";

// * Models
import { Department, DepartmentForm, DialogMode, Store } from "@models";

// * Services
import { department } from "@services";

// * Store
import { addDepartment, deleteDepartment, updateDepartment } from "@store";

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

                dispatch((openMode === DialogMode.CREATE ? addDepartment : updateDepartment)(data.data));
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
        formik.setValues(department);

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