// * React Libraries
import { FC } from "react";

// * Third Party Libraries
import { FormikProps } from "formik";

// * Models
import { DepartmentForm as IDepartmentForm, DialogMode } from "@models";

// * Components
import { CrudDialog } from "../CrudDialog";
import { DepartmentForm } from "./DepartmentForm";

export const DepartmentDialog :  FC<DepartmentDialogProps> = (props) => {

    const {
        openMode,
        formik,
        setOpenMode
    } = props;

    return (
        <CrudDialog
            openMode={openMode}
            setOpenMode={setOpenMode}
            title="Department"
            onSubmit={formik.handleSubmit}
        >
            <DepartmentForm 
                formik={formik}
            />
        </CrudDialog>
    )
}

interface DepartmentDialogProps {
    openMode: DialogMode;
    formik: FormikProps<IDepartmentForm>;
    setOpenMode: (openMode: DialogMode) => void;
}