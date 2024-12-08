// * React Libraries
import { FC } from "react";

// * Third Party Libraries
import { FormikProps } from "formik";

// * Models
import { CategoryForm as ICategoryForm, DialogMode } from "@models";

// * Components
import { CrudDialog } from "../CrudDialog";
import { CategoryForm } from "./CategoryForm";

export const CategoryDialog :  FC<CategoryDialogProps> = (props) => {

    const {
        openMode,
        formik,
        setOpenMode
    } = props;

    return (
        <CrudDialog
            openMode={openMode}
            setOpenMode={setOpenMode}
            title="Category"
            onSubmit={formik.handleSubmit}
        >
            <CategoryForm 
                formik={formik}
            />
        </CrudDialog>
    )
}

interface CategoryDialogProps {
    openMode: DialogMode;
    formik: FormikProps<ICategoryForm>;
    setOpenMode: (openMode: DialogMode) => void;
}