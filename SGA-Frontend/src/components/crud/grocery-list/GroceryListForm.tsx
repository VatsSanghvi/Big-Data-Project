// * React Libraries
import { FC } from "react";

// * Third Party Libraries
import { FormikProps } from "formik";

// * Models
import { BreakpointColumns, GroceryListForm as IGroceryListForm } from "@models";

// * Helpers
import { getProps } from "@helpers";

// * Components
import { MInputText } from "@components";

export const GroceryListForm: FC<GroceryListFormProps> = (props) => {

    const {
        formik
    } = props;

    const breakpoints: BreakpointColumns = {
        sm: 6,
    }

    return (
        <form
            className="grocery-list-form"
        >
            <MInputText
                {...getProps(formik, 'name', 'GroceryList Name')}
                columns={12}
                breakpoints={breakpoints}
            />
        </form>
    )
}

interface GroceryListFormProps {
    formik: FormikProps<IGroceryListForm>;
}