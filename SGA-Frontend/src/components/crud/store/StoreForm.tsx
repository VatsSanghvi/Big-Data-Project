// * React Libraries
import { FC } from "react";

// * Third Party Libraries
import { FormikProps } from "formik"

// * Components
import { MInputText } from "@components";

// * Helpers
import { getProps } from "@helpers";

// * Models
import { BreakpointColumns, StoreForm as IStoreForm } from "@models";

export const StoreForm : FC<StoreFormProps> = (props) => {
    const {
        formik
    } = props;

    const breakpoints : BreakpointColumns = {
        sm: 6,
    }

    return (
        <form
            className="store-form"
        >
            <MInputText 
                {...getProps(formik, 'store_name', 'Store Name')}
                columns={12}
                breakpoints={breakpoints}
            />
            <MInputText 
                {...getProps(formik, 'location', 'Address')}
                columns={12}
                breakpoints={breakpoints}
            />
            <MInputText 
                {...getProps(formik, 'manager_email', 'Manager Email')}
                columns={12}
                breakpoints={breakpoints}
            />
        </form>
    )
}

interface StoreFormProps {
    formik: FormikProps<IStoreForm>;
}