import { AddButton, DeleteButton, EditButton, PageTitle, ProductDialog } from "@components"
import { productFormValidationSchema, productFormValues } from "@forms";
import { useAppDispatch, useAppSelector, useToast } from "@hooks";
import { DialogMode, Product, ProductForm } from "@models";
import { product } from "@services";
import { addProduct, deleteProduct, updateProduct } from "@store";
import { useFormik } from "formik";
import { Column } from "primereact/column";
import { confirmDialog, ConfirmDialog } from "primereact/confirmdialog"
import { DataTable } from "primereact/datatable";
import { useState } from "react";

export const ProductsPage = () => {
    const { showSuccess, showError } = useToast();

    const { products } = useAppSelector(state => state.info);
    const dispatch = useAppDispatch();

    const [openMode, setOpenMode] = useState<DialogMode>(DialogMode.CLOSE);

    const { create, update } = product;

    const formik = useFormik<ProductForm>({
        initialValues: productFormValues,
        validationSchema: productFormValidationSchema,
        onSubmit: async(values) => {
            console.log(values);

            const { data } = await (openMode === DialogMode.CREATE ? create : update)(values);

            console.log(data);
            
            if (data.ok) {
                setOpenMode(DialogMode.CLOSE);

                dispatch((openMode === DialogMode.CREATE ? addProduct : updateProduct)(data.data));
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

    const onEdit = (product: Product) => {
        formik.setValues({
            ...product,
            fk_store_id: product.store.store_id,
            fk_department_id: product.department.department_id,
            fk_category_id: product.category.category_id
        });

        setOpenMode(DialogMode.EDIT);
    };

    const onAcceptDelete = async(product_id: number) => {
        console.log(product_id)
        
        const { data } = await product.delete(product_id);

        console.log(data);

        if (data.ok) {
            showSuccess('Success', 'Product Deleted Successfully');
            dispatch(deleteProduct(product_id))
        } else {
            showError('Error', 'Something went wrong');
        }
    };

    const onDelete = (product_id: number) => {
        confirmDialog({
            message: 'Do you want to delete this product?',
            header: 'Delete Product',
            icon: 'pi pi-exclamation-triangle',
            accept: () => onAcceptDelete(product_id)
        });
    };

    const actionButtonsTemplate = (rowData: Product) => {
        return (
            <div
                className="flex gap-2 align-items-center"
            >
                <EditButton onClick={() => onEdit(rowData)}/>
                <DeleteButton onClick={() => onDelete(rowData.product_id)}/>
            </div>
        )
    }

    return (
        <>
            <PageTitle title="Invetory Manager"/>
            <AddButton 
                label="Create New Product"
                onClick={onCreate}
            />
            <div className="h-full overflow-auto">
                <DataTable 
                    paginator 
                    rows={6}
                    value={products} 
                >
                    <Column
                        sortable
                        field="product_name" 
                        header="Name"
                    >
                    </Column>
                    <Column
                        sortable
                        field="stock_quantity" 
                        header="Stock Available"
                    >
                    </Column>
                    <Column
                        sortable
                        field="price" 
                        header="Price"
                    >
                    </Column>
                    <Column
                        sortable
                        field="status" 
                        header="Status"
                    >
                    </Column>
                    <Column
                        sortable
                        field="store.store_name" 
                        header="Store"
                    >
                    </Column>
                    <Column
                        sortable
                        field="department.department_name" 
                        header="Department"
                    >
                    </Column>
                    <Column
                        sortable
                        field="category.category_name" 
                        header="Category"
                    >
                    </Column>
                    <Column
                        body={actionButtonsTemplate}
                        exportable
                    >
                    </Column>
                </DataTable>
            </div>
            <ProductDialog 
                openMode={openMode}
                setOpenMode={setOpenMode}
                formik={formik}
            />
            <ConfirmDialog />
        </>
    )
}