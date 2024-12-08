// * React Libraries
import { useState } from "react"

// * Third Party Libraries
import { useFormik } from "formik";
import { confirmDialog, ConfirmDialog } from "primereact/confirmdialog";
import { DataView } from "primereact/dataview";

// * Components
import { AddButton, PageTitle, /*ProductDialog, ProductListTemplate*/ } from "@components"

// * Hooks
import { useAppDispatch, useAppSelector, /* useAuthStore ,*/ useToast } from "@hooks";

// * Services

// * Forms
import { productFormValidationSchema, productFormValues } from "@forms";

// * Models
import { DialogMode, Product, ProductForm } from "@models";

// * Store
// import { addProductGroceryList } from "@store";

export const UserProductsPage = () => {

    const { showSuccess, showError } = useToast();

    const { products } = useAppSelector(state => state.info);
    const dispatch = useAppDispatch();

    const [openMode, setOpenMode] = useState<DialogMode>(DialogMode.CLOSE);

    // const { add } = product;

    const formik = useFormik<ProductForm>({
        initialValues: productFormValues,
        validationSchema: productFormValidationSchema,
        onSubmit: async (values) => {
            // console.log(values);

            // const { data } = await (add)(values);

            // if (data.ok) {
            //     setOpenMode(DialogMode.CLOSE);

            //     dispatch((addProductGroceryList)(data.data));
            //     showSuccess('Success', `Product Added Successfully`);
            // } else {
            //     showError('Error', 'Something went wrong');
            // }
        }
    });

    const onCreate = () => {
        formik.resetForm();
        setOpenMode(DialogMode.ADD);
    };


    const listTemplate = (items: Product[]) => (
        // <ProductListTemplate
        //     items={items}
        // />
        <></>
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
            {/* <ProductDialog
                openMode={openMode}
                setOpenMode={setOpenMode}
                formik={formik}
            /> */}
            <ConfirmDialog />
        </>
    )
}