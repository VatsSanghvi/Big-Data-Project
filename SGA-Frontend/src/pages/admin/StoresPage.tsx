import { AddButton, ListTemplate, PageTitle, StoreDialog, StoreItemTemplate } from "@components"
import { storeFormValidationSchema, storeFormValues } from "@forms";
import { useAppDispatch, useAppSelector, useAuthStore, useToast } from "@hooks";
import { DialogMode, Store, StoreCreate, StoreForm, StoreUpdate } from "@models";
import { store } from "@services";
import { addStore, deleteStore, setStores, updateStore } from "@store";
import { useFormik } from "formik";
import { confirmDialog, ConfirmDialog } from "primereact/confirmdialog";
import { DataView } from "primereact/dataview";
import { useEffect, useState } from "react"

export const StoresPage = () => {
    const { user } = useAuthStore();
    const { showSuccess, showError } = useToast();

    const { stores } = useAppSelector(state => state.info);
    const dispatch = useAppDispatch();

    const [openMode, setOpenMode] = useState<DialogMode>(DialogMode.CLOSE);
    const [openStoreId, setOpenStoreId] = useState<number>(0);

    const formik = useFormik<StoreForm>({
        initialValues: storeFormValues,
        validationSchema: storeFormValidationSchema,
        onSubmit: async(values) => {
            console.log(values);

            let response;

            if (openMode === DialogMode.CREATE) {
                // * Create Store
                const request : StoreCreate = {
                    store_name: values.store_name,
                    location: values.location,
                    fk_owner_id: user.user_id,
                    ...values.manager_email && { manager_email: values.manager_email }
                }

                response = await store.create(request);
            } else {
                // * Update Store
                const request : StoreUpdate = {
                    store_name: values.store_name,
                    location: values.location,
                    ...values.manager_email && { manager_email: values.manager_email }
                }

                response = await store.update(openStoreId, request);
            }

            if (response?.status === 200) {
                setOpenMode(DialogMode.CLOSE);

                if (openMode === DialogMode.CREATE) {
                    dispatch(addStore(response.data));
                    showSuccess('Success', 'Store Created Successfully');
                } else {
                    dispatch(updateStore(response.data));
                    showSuccess('Success', 'Store Updated Successfully');
                }
            } else {
                showError('Error', 'Something went wrong');   
            }
        }
    })

    useEffect(() => {
        const fetchStores = async () => {
            const { status, data } = await store.get(user.user_id);

            if (status === 200) dispatch(setStores(data));            
        };

        fetchStores();
    }, []);
    
    const onCreate = () => {
        setOpenMode(DialogMode.CREATE);
        formik.resetForm();
    };

    const onEdit = (store: Store) => {
        formik.setValues({
            store_name: store.store_name,
            location: store.location,
            fk_owner_id: user.user_id,
            manager_email: store.manager?.email ?? '',
        });

        setOpenStoreId(store.store_id);
        setOpenMode(DialogMode.EDIT);
    };

    const onAcceptDelete = async (store_id: number) => {
        console.log(store_id);

        const { status } = await store.delete(store_id);

        if (status === 200) {
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
        <ListTemplate 
            noItemsMessage="No Stores Found" 
            items={items} 
            itemTemplate={(index, item) => (
                <StoreItemTemplate 
                    key={index}
                    item={item as Store} 
                    index={index} 
                    onDelete={(store_id: number) => onDelete(store_id)} 
                    onEdit={(item : Store) => onEdit(item)}
                />
            )} 
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
                mode={openMode}
                setMode={setOpenMode}
                formik={formik}
            />
            <ConfirmDialog />
        </>
    )
}