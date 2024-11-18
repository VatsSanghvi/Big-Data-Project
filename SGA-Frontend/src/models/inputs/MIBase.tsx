// * React Libraries
import { CSSProperties } from "react";

// * Third Party Libraries
import { FormikProps } from "formik";

export interface MIBase {
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    formik: FormikProps<any>;
    label: string;
    name: string;
    className?: string;
    id?: string;
    placeholder?: string;
    style?: CSSProperties;
    wrapperClassName?: string;
    wrapperStyle?: CSSProperties;
    variant?: 'outlined' | 'filled';
}