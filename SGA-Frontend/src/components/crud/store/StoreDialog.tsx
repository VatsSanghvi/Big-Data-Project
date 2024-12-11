// * React Libraries
import { FC } from "react";

// * Third Party Libraries
import { FormikProps } from "formik";

// * Models
import { DialogMode, StoreForm as IStoreForm } from "@models";

// * Components
import { CrudDialog } from "../CrudDialog";
import { StoreForm } from "./StoreForm";

// * Dialog for Store CRUD
export const StoreDialog : FC<StoreDialogProps> = (props) => {
    const {
        openMode,
        formik,
        setOpenMode
    } = props;

    return (
        <CrudDialog
            openMode={openMode}
            setOpenMode={setOpenMode}
            title="Store"
            onSubmit={formik.handleSubmit}
        >
            <StoreForm 
                formik={formik}
            />
        </CrudDialog>
    )
}

interface StoreDialogProps {
    openMode: DialogMode;
    formik: FormikProps<IStoreForm>;
    setOpenMode: (openMode: DialogMode) => void;
}