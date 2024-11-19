// * React Libraries
import { FC } from "react";

// * Third Party Libraries
import { classNames } from "primereact/utils";
import { Password } from "primereact/password";

// * Hooks
import { useBreakpoints } from "@hooks";

// * Components
import { MInputBase } from "./MInputBase";

// * Models
import { MIBase } from "@models";

// * Helpers
import { getId } from "@helpers";

export const MPassword : FC<MPasswordProps> = (props) => {
    const {
        id,
        name,
        formik,
        className,
        feedback = false,
        toogleMask = false    
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
            <Password 
                {...props}
                inputClassName="w-full"
                id={getId(name, id)}
                className={classes}
                value={formik.values[name]}
                onChange={formik.handleChange}
                onBlur={formik.handleBlur}
                feedback={feedback}
                toggleMask={toogleMask}
            />
        </MInputBase>
    )
}

interface MPasswordProps extends MIBase {
    feedback?: boolean;
    toogleMask?: boolean;
}