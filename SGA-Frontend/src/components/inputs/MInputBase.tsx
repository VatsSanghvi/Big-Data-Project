// * React Libraries
import { FC, ReactNode } from "react"

// * Third Party Libraries
import { FloatLabel } from "primereact/floatlabel";
import { classNames } from "primereact/utils";

// * Helpers
import { getId, hasError } from "@helpers";

// * Models
import { MIBase } from "@models"

export const MInputBase : FC<MInputBaseProps> = (props) => {
    const {
        formik,
        label,
        name,
        id,
        children,
        wrapperClassName,
        wrapperStyle,
    } = props;

    const classes = classNames(
        'w-full flex flex-column gap-2',
        wrapperClassName
    );

    return (
        <div 
            className={classes}
            style={wrapperStyle}
        >
            <FloatLabel>
                {children}
                <label htmlFor={getId(name, id)}>{label}</label>
            </FloatLabel>
            <small
                className="p-error"
            >
                {
                    hasError(formik, name) ? formik.errors[name] as string : '\xa0'
                }
            </small>
        </div>
    )
}

interface MInputBaseProps extends MIBase {
    children: ReactNode;
}