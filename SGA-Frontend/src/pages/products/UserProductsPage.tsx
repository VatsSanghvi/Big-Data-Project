// * React Libraries
import { useState } from "react"

// * Third Party Libraries
import { useFormik } from "formik";
import { confirmDialog, ConfirmDialog } from "primereact/confirmdialog";
import { DataView } from "primereact/dataview";

// * Components
import { AddButton, PageTitle, GroceryListDialog, ProductListTemplate } from "@components"

// * Hooks
import { useAppDispatch, useAppSelector, useToast } from "@hooks";

// * Services
import { userProduct } from "@services";

// * Forms
import { groceryListInitialValues, groceryListValidationSchema } from "@forms";

// * Models
import { DialogMode, Product, GroceryListForm } from "@models";

export const UserProductsPage = () => {
    const { showSuccess, showError } = useToast();

    const { products } = useAppSelector(state => state.info);
    const dispatch = useAppDispatch();

    const [openMode, setOpenMode] = useState<DialogMode>(DialogMode.CLOSE);

    const { createList } = userProduct;

    const formik = useFormik<GroceryListForm>({
        initialValues: groceryListInitialValues,
        validationSchema: groceryListValidationSchema,
        onSubmit: async (values) => {
            console.log(values);

            const { data } = await (createList)(values);
            if (data.ok) {
                setOpenMode(DialogMode.CLOSE);
                dispatch(createGroceryList(data.data));
                showSuccess('Success', `Product Added Successfully`);
            } else {
                showError('Error', 'Something went wrong');
            }
        }
    });

    const onCreate = () => {
        formik.resetForm();
        setOpenMode(DialogMode.ADD);
    };

    const listTemplate = (items: Product[]) => (
        <ProductListTemplate
            items={items}
        />
    )
    return (
        <>
            <PageTitle title="Products" />
            <AddButton
                label="Add Product"
                onClick={onCreate}
            />
            <div className="h-full overflow-auto">
                <DataView
                    paginator
                    className="h-full"
                    rows={4}
                    value={products}
                    listTemplate={listTemplate}
                />
            </div>
            <GroceryListDialog
                openMode={openMode}
                setOpenMode={setOpenMode}
                formik={formik}
            />
            <ConfirmDialog />
        </>
    )
}