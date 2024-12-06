// * React Libraries
import { CSSProperties } from "react";

// * Third Party Libraries
import { FormikProps } from "formik";

// * Models
import { Breakpoints } from "../breakpoints";

export type BreakpointColumns = Breakpoints<number>;
export interface IBase {
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    formik: FormikProps<any>;
    name: string;
    label: string;
    wrapperClassName?: string;
    wrapperStyle?: CSSProperties;
    columns?: number;
    breakpoints?: BreakpointColumns;
}

export type MIBase<T> = Omit<T & IBase, 'value' | 'onChange' | 'onBlur'>