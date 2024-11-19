import { FormikProps } from "formik";

export const getId = (name: string, id?: string) => {
    return id || name;
}

// eslint-disable-next-line @typescript-eslint/no-explicit-any
export const hasError = (formik: FormikProps<any>, name: string) => {
    return !!formik.touched[name] && !!formik.errors[name];
}