import { FormikProps } from "formik";

// eslint-disable-next-line @typescript-eslint/no-explicit-any
export const getProps = (formik: FormikProps<any>, name: string, label: string, variant: 'filled' | 'outlined' = 'filled') => ({
    formik,
    name,
    label,
    variant
});