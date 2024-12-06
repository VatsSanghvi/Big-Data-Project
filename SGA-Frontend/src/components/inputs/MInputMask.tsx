// * React Libraries
import { FC } from "react";

// * Third Party Libraries
import { InputMask, InputMaskProps } from 'primereact/inputmask';
import { classNames } from "primereact/utils";

// * Hooks
import { useBreakpoints } from "@hooks";

// * Components
import { MInputBase } from "./MInputBase";

// * Models
import { MIBase } from "@models";

// * Helpers
import { getId, hasError } from "@helpers";

export const MInputMask : FC<MIBase<InputMaskProps>> = (props) => {
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
            <InputMask 
                {...props}
                id={getId(name, id)}
                className={classes}
                value={formik.values[name]}
                onChange={formik.handleChange}
                onBlur={formik.handleBlur}
                invalid={hasError(formik, name)}
            />
        </MInputBase>
    )
}