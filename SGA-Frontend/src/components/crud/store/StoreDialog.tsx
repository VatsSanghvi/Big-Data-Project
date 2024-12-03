// * React Libraries
import { FC } from "react";

// * Third Party Libraries
import { FormikProps } from "formik";

// * Models
import { DialogMode, StoreForm as IStoreForm } from "@models";

// * Components
import { CrudDialog } from "../CrudDialog";
import { StoreForm } from "./StoreForm";

export const StoreDialog : FC<StoreDialogProps> = (props) => {
    const {
        mode,
        formik,
        setMode
    } = props;

    return (
        <CrudDialog
            mode={mode}
            setMode={setMode}
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
    mode: DialogMode;
    formik: FormikProps<IStoreForm>;
    setMode: (mode: DialogMode) => void;
}