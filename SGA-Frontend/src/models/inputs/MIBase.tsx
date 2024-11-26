// * React Libraries
import { CSSProperties } from "react";

// * Third Party Libraries
import { FormikProps } from "formik";
export interface IBase {
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    formik: FormikProps<any>;
    name: string;
    label: string;
    wrapperClassName?: string;
    wrapperStyle?: CSSProperties;
}

export type MIBase<T> = Omit<T & IBase, 'value' | 'onChange' | 'onBlur'>