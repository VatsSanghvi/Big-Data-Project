// * React Libraries
import { FC } from "react";

// * Third Party Libraries
import { FormikProps } from "formik";

// * Models
import { GroceryListForm as IGroceryListForm, DialogMode } from "@models";

// * Components
import { CrudDialog } from "../CrudDialog";
import { GroceryListForm } from "./GroceryListForm";

export const GroceryListDialog: FC<GroceryListDialogProps> = (props) => {

    const {
        openMode,
        formik,
        setOpenMode
    } = props;

    return (
        <CrudDialog
            openMode={openMode}
            setOpenMode={setOpenMode}
            title="Grocery List"
            onSubmit={formik.handleSubmit}
        >
            <GroceryListForm
                formik={formik}
            />
        </CrudDialog>
    )
}

interface GroceryListDialogProps {
    openMode: DialogMode;
    formik: FormikProps<IGroceryListForm>;
    setOpenMode: (openMode: DialogMode) => void;
}