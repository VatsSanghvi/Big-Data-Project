// * React Libraries
import { useState } from "react"

// * Third Party Libraries
import { useFormik } from "formik";
import { DataView } from "primereact/dataview";

// * Components
import { PageTitle, ProductListTemplate, GroceryListItemDialog } from "@components"

// * Hooks
import { useAppDispatch, useAppSelector, useToast } from "@hooks";

// * Services
import { userProduct } from "@services";

// * Forms
import { groceryListItemInitialValues, groceryListItemValidationSchema } from "@forms";

// * Models
import { DialogMode, Product, GroceryListItemForm } from "@models";

// * Store
import { addGroceryListItem } from "@store";

export const UserProductsPage = () => {
    const { showSuccess, showError } = useToast();

    const { products } = useAppSelector(state => state.info);
    const { groceryList } = useAppSelector(state => state.user);
    const dispatch = useAppDispatch();

    const [openMode, setOpenMode] = useState<DialogMode>(DialogMode.CLOSE);

    const formik = useFormik<GroceryListItemForm>({
        initialValues: groceryListItemInitialValues,
        validationSchema: groceryListItemValidationSchema,
        onSubmit: async (values) => {
            const { data } = await userProduct.addItem(values);
            if (data.ok) {
                setOpenMode(DialogMode.CLOSE);
                dispatch(addGroceryListItem(data.data));
                showSuccess('Success', `Product Added Successfully`);
            } else {
                showError('Error', 'Something went wrong');
            }
        }
    });

    const onAdd = (item: Product) => {
        if (!groceryList) {
            showError("Error", "Please create a grocery list first");
            return;
        }

        formik.resetForm();
        formik.setFieldValue('product_id', item.product_id);
        formik.setFieldValue('grocery_list_id', groceryList.id);
        
        setOpenMode(DialogMode.ADD);
    }

    const listTemplate = (items: Product[]) => (
        <ProductListTemplate
            items={items}
            onAdd={(item: Product) => onAdd(item)}
        />
    )
    return (
        <>
            <PageTitle title="Products" />
            <div className="h-full overflow-auto">
                <DataView
                    paginator
                    className="h-full"
                    rows={3}
                    value={products}
                    listTemplate={listTemplate}
                />
            </div>
            <GroceryListItemDialog
                openMode={openMode}
                setOpenMode={setOpenMode}
                formik={formik}
            />
        </>
    )
}