// * React Libraries
import { FC } from "react";

// * Third Party Libraries
import { FormikProps } from "formik";

// * Models
import { DialogMode, ProductForm as IProductForm } from "@models";

// * Components
import { CrudDialog } from "../CrudDialog";
import { ProductForm } from "./ProductForm";

export const ProductDialog :  FC<ProductDialogProps> = (props) => {

    const {
        openMode,
        formik,
        setOpenMode
    } = props;

    return (
        <CrudDialog
            openMode={openMode}
            setOpenMode={setOpenMode}
            title="Product"
            onSubmit={formik.handleSubmit}
        >
            <ProductForm
                formik={formik}
            />
        </CrudDialog>
    )
}

interface ProductDialogProps {
    openMode: DialogMode;
    formik: FormikProps<IProductForm>;
    setOpenMode: (openMode: DialogMode) => void;
}