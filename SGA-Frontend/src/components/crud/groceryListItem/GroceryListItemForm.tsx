// * React Libraries
import { FC } from "react";

// * Third Party Libraries
import { FormikProps } from "formik";

// * Models
import { BreakpointColumns, GroceryListItemForm as IGroceryListItemForm } from "@models";

// * Helpers
import { getProps } from "@helpers";

// * Components
import { MInputNumber } from "@components";

// * Form for Department
export const GroceryListItemForm : FC<GroceryListItemFormProps> = (props) => {

    const {
        formik
    } = props;

    const breakpoints : BreakpointColumns = {
        sm: 6,
    }

    return (
        <form
            className="grocery-list-item-form"
        >
            <MInputNumber
                {...getProps(formik, 'quantity', 'Quantity')}
                columns={12}
                breakpoints={breakpoints}
            />
        </form>
    )
}

interface GroceryListItemFormProps {
    formik: FormikProps<IGroceryListItemForm>;
}