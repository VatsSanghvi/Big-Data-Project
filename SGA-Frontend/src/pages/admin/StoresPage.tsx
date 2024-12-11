// * React Libraries
import { useState } from "react"

// * Third Party Libraries
import { useFormik } from "formik";
import { confirmDialog, ConfirmDialog } from "primereact/confirmdialog";
import { DataView } from "primereact/dataview";

// * Components
import { AddButton, PageTitle, StoreDialog, StoreListTemplate } from "@components"

// * Hooks
import { useAppDispatch, useAppSelector, useAuthStore, useToast } from "@hooks";

// * Services
import { store } from "@services";

// * Forms
import { storeFormValidationSchema, storeFormValues } from "@forms";

// * Models
import { DialogMode, Store, StoreForm } from "@models";

// * Store
import { addStore, deleteStore, updateStore } from "@store";

export const StoresPage = () => {

    const { user } = useAuthStore();
    const { showSuccess, showError } = useToast();

    const { stores } = useAppSelector(state => state.info);
    const dispatch = useAppDispatch();

    const [openMode, setOpenMode] = useState<DialogMode>(DialogMode.CLOSE);

    const { create, update } = store;

    const formik = useFormik<StoreForm>({
        initialValues: storeFormValues,
        validationSchema: storeFormValidationSchema,
        onSubmit: async(values) => {
            console.log(values);

            const { data } = await (openMode === DialogMode.CREATE ? create : update)(values);
            
            if (data.ok) {
                setOpenMode(DialogMode.CLOSE);

                dispatch((openMode === DialogMode.CREATE ? addStore : updateStore)(data.data));
                showSuccess('Success', `Store ${openMode === DialogMode.CREATE ? 'Created' : 'Updated'} Successfully`);
            } else {
                showError('Error', 'Something went wrong');   
            }
        }
    });

    const onCreate = () => {
        formik.resetForm();
        formik.setFieldValue('fk_owner_id', user.user_id);
        setOpenMode(DialogMode.CREATE);
    };

    const onEdit = (store: Store) => {
        formik.setValues({
            store_id: store.store_id,
            store_name: store.store_name,
            location: store.location,
            fk_owner_id: user.user_id,
            manager_email: store.manager?.email ?? '',
        });

        setOpenMode(DialogMode.EDIT);
    };

    const onAcceptDelete = async (store_id: number) => {
        const { data } = await store.delete(store_id);

        if (data.ok) {
            showSuccess('Success', 'Store Deleted Successfully');
            dispatch(deleteStore(store_id));
        }
        else {
            showError('Error', 'Something went wrong');
        }
    };

    const onDelete = (store_id: number) => {
        confirmDialog({
            message: 'Do you want to delete this store?',
            header: 'Delete Store',
            icon: 'pi pi-exclamation-triangle',
            accept: () => onAcceptDelete(store_id)
        })
    };

    const listTemplate = (items: Store[]) => (
        <StoreListTemplate 
            items={items}
            onDelete={onDelete}
            onEdit={onEdit}
        />
    )

    return (
        <>
            <PageTitle title="Store Manager"/>
            <AddButton 
                label="Create New Store"
                onClick={onCreate}
            />
            <div className="h-full overflow-auto">
                <DataView 
                    paginator
                    className="h-full"
                    rows={4}
                    value={stores}
                    listTemplate={listTemplate}
                />
            </div>
            <StoreDialog 
                openMode={openMode}
                setOpenMode={setOpenMode}
                formik={formik}
            />
            <ConfirmDialog />
        </>
    )
}