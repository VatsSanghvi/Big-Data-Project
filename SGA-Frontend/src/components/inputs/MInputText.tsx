// * React Libraries
import { FC, HTMLInputTypeAttribute } from "react";

// * Third Party Libraries
import { classNames } from "primereact/utils";
import { InputText } from "primereact/inputtext";

// * Hooks
import { useBreakpoints } from "@hooks";

// * Components
import { MInputBase } from "./MInputBase";

// * Models
import { MIBase } from "@models";

// * Helpers
import { getId, hasError } from "@helpers";

export const MInputText : FC<MInputTextProps> = (props) => {
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
            <InputText
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

export type InputMode = "none" | "text" | "tel" | "url" | "email" | "numeric" | "decimal" | "search";

interface MInputTextProps extends MIBase {
    type?: HTMLInputTypeAttribute;
    inputMode?: InputMode;
}