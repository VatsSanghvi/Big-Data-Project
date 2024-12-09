// * React Libraries
import { FC } from "react";

// * Third Party Libraries
import { FormikProps } from "formik";

// * Models
import { DialogMode, GroceryListItemForm as IGroceryListItemForm } from "@models";

// * Components
import { CrudDialog } from "../CrudDialog";
import { GroceryListItemForm } from "./GroceryListItemForm";


// * Dialog to add a new product to grocery list
export const GroceryListItemDialog :  FC<GroceryListItemDialogProps> = (props) => {

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
            <GroceryListItemForm
                formik={formik}
            />
        </CrudDialog>
    )
}

interface GroceryListItemDialogProps {
    openMode: DialogMode;
    formik: FormikProps<IGroceryListItemForm>;
    setOpenMode: (openMode: DialogMode) => void;
}