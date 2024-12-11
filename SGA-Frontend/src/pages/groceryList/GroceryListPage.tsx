import { GroceryListDialog, GroceryListItemDialog, GroceryListListTemplate, PageTitle } from "@components"
import { groceryListInitialValues, groceryListItemInitialValues, groceryListItemValidationSchema, groceryListValidationSchema } from "@forms";
import { useAppDispatch, useAppSelector, useAuthStore, useToast } from "@hooks";
import { DialogMode, GroceryListForm, GroceryListItem, GroceryListItemForm } from "@models"
import { userProduct } from "@services";
import { deleteGroceryListItems, removeGroceryListItem, setGroceryList, updateGroceryListItem } from "@store";
import { useFormik } from "formik";
import { Button } from "primereact/button";
import { confirmDialog, ConfirmDialog } from "primereact/confirmdialog";
import { DataView } from "primereact/dataview"
import { useState } from "react";

export const GroceryListPage = () => {
    const { showSuccess, showError } = useToast();
    const { user } = useAuthStore();

    const { groceryList, groceryListItems } = useAppSelector(state => state.user);
    const dispatch = useAppDispatch();

    const [openModeItem, setOpenModeItem] = useState<DialogMode>(DialogMode.CLOSE);
    const [openMode, setOpenMode] = useState<DialogMode>(DialogMode.CLOSE);

    const formikItem = useFormik<GroceryListItemForm>({
        initialValues: groceryListItemInitialValues,
        validationSchema: groceryListItemValidationSchema,
        onSubmit: async (values) => {
            const { data } = await userProduct.updateItem(values);
            if (data.ok) {
                setOpenModeItem(DialogMode.CLOSE);
                dispatch(updateGroceryListItem(data.data));
                showSuccess('Success', `Product Added Successfully`);
            } else {
                showError('Error', 'Something went wrong');
            }
        }
    });

    const formik = useFormik<GroceryListForm>({
        initialValues: groceryListInitialValues,
        validationSchema: groceryListValidationSchema,
        onSubmit: async (values) => {
            const { data } = await userProduct.createGroceryList(values);

            if (data.ok) {
                setOpenMode(DialogMode.CLOSE);
                dispatch(setGroceryList(data.data));
                showSuccess('Success', `Grocery List Created Successfully`);
            } else {
                showError('Error', 'Something went wrong');
            }
        }
    });

    const onCreate = () => {
        formik.resetForm();
        formik.setFieldValue('user_id', user.user_id);
        setOpenMode(DialogMode.CREATE);
    }

    const onAcceptComplete = async() => {
        const { data } = await userProduct.deleteGroceryList(groceryList?.id ?? 0);

        if (data.ok) {
            showSuccess('Success', 'Grocery List Completed Successfully');
            dispatch(setGroceryList(undefined));
            dispatch(deleteGroceryListItems())
        } else {
            showError('Error', 'Something went wrong');
        }
    }

    const onCompleteList = () => {
        confirmDialog({
            message: 'Are you sure you are done with your grocery list?',
            header: 'Complete Grocery List',
            icon: 'pi pi-exclamation-triangle',
            accept: () => onAcceptComplete()
        });
    }

    const onEdit = (item: GroceryListItem) => {
        formikItem.setValues(item);
        setOpenModeItem(DialogMode.EDIT);
    }

    const onAcceptDelete = async(item_id: number) => {
        const { data } = await userProduct.deleteItem(groceryList?.id ?? 0, item_id);

        if (data.ok) {
            showSuccess('Success', 'Product deleted successfully from the grocery list');
            dispatch(removeGroceryListItem(item_id))
        } else {
            showError('Error', 'Something went wrong');
        }
    };

    const onDelete = (grocery_item_id: number) => {
        confirmDialog({
            message: 'Do you want to delete this product from the grocery list?',
            header: 'Delete Grocery List Item',
            icon: 'pi pi-exclamation-triangle',
            accept: () => onAcceptDelete(grocery_item_id)
        });
    };

    const listTemplate = (items: GroceryListItem[]) => (
        <GroceryListListTemplate
            items={items}
            onEdit={onEdit}
            onDelete={onDelete}
        />
    )

    return (
        <>
            <PageTitle title={`Grocery List ${groceryList ? ': ' + groceryList.name : ''}`} />
            <div className="flex justify-content-end">
                {
                    groceryList 
                    ? (
                        <Button 
                            label="Complete Grocery List"
                            severity="success"
                            icon="pi pi-check"
                            onClick={onCompleteList}
                        />
                    )
                    : (
                        <Button 
                            label="Create Grocery List"
                            severity="info"
                            icon="pi pi-plus"
                            onClick={onCreate}
                        />
                    )
                }
            </div>
            <div className="h-full overflow-auto">
                {
                    groceryList 
                        ? (
                            <DataView
                                paginator
                                className="h-full"
                                rows={3}
                                value={groceryListItems}
                                listTemplate={listTemplate}
                            />
                        ) 
                        : (
                            <h3>No Grocery List Created</h3>
                        )
                }
            </div>
            <GroceryListItemDialog
                openMode={openModeItem}
                setOpenMode={setOpenModeItem}
                formik={formikItem}
            />
            <GroceryListDialog 
                openMode={openMode}
                setOpenMode={setOpenMode}
                formik={formik}
            />
            <ConfirmDialog />
        </>
    )
}