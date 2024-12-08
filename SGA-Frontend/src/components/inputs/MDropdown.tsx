// * React Libraries
import { FC } from "react"

// * Third Party Libraries
import { Dropdown, DropdownProps } from "primereact/dropdown"
import { classNames } from "primereact/utils";

// * Models
import { MIBase } from "@models"

// * Components
import { MInputBase } from "./MInputBase";

// * Helpers
import { getId, hasError } from "@helpers";

export const MDropdown : FC<MIBase<DropdownProps>> = (props) => {
    const {
        id,
        name,
        formik,
        className,
    } = props;

    const classes = classNames(
        'w-full',
        className
    )

    return (
        <MInputBase
            {...props}
        >
            <Dropdown 
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
