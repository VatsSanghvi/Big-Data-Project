// * React Libraries
import { FC, useMemo } from "react";

// * Third Party Libraries
import { FormikProps } from "formik";

// * Models
import { BreakpointColumns, DepartmentForm as IDepartmentForm, Option, Store } from "@models";

// * Helpers
import { getProps } from "@helpers";

// * Components
import { MDropdown, MInputText } from "@components";

// * Hooks
import { useAppSelector } from "@hooks";

export const DepartmentForm : FC<DepartmentFormProps> = (props) => {

    const {
        formik
    } = props;

    const { stores } = useAppSelector(state => state.info);

    const storeOptions : Option<number>[] = useMemo(() => {
        return stores.map((store : Store) => ({
            label: store.store_name,
            value: store.store_id
        }))
    }, [stores]);

    const breakpoints : BreakpointColumns = {
        sm: 6,
    }

    return (
        <form
            className="department-form"
        >
            <MInputText 
                {...getProps(formik, 'department_name', 'Department Name')}
                columns={12}
                breakpoints={breakpoints}
            />
            <MDropdown 
                {...getProps(formik, 'fk_store_id', 'Owner Store')}
                columns={12}
                breakpoints={breakpoints}
                options={storeOptions}
            />
        </form>
    )
}

interface DepartmentFormProps {
    formik: FormikProps<IDepartmentForm>;
}