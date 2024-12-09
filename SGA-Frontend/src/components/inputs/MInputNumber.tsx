// * React Libraries
import { FC } from "react";

// * Third Party Libraries
import { InputNumber, InputNumberProps } from "primereact/inputnumber"
import { classNames } from "primereact/utils";

// * Hooks
import { useBreakpoints } from "@hooks";

// * Components
import { MInputBase } from "./MInputBase";

// * Models
import { MIBase } from "@models";

// * Helpers
import { getId, hasError } from "@helpers";


// * Number input component for inputting numbers
export const MInputNumber : FC<MIBase<InputNumberProps>> = (props) => {

    const {
        id,
        name,
        formik,
        className    
    } = props;
    
    const { isMobile } = useBreakpoints();

    const classes = classNames(
        'w-full',
        {'p-inputtext-sm': isMobile},
        className
    )

    return (
        <MInputBase
            {...props}
        >
            <InputNumber 
                {...props}
                id={getId(name, id)}
                className={classes}
                value={formik.values[name]}
                onValueChange={formik.handleChange}
                onBlur={formik.handleBlur}
                invalid={hasError(formik, name)}
            />
        </MInputBase>
    )
}