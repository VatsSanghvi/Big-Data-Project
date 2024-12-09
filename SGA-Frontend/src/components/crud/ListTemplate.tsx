// * React Libraries
import { ReactNode } from "react";

// * Third Party Libraries
import { classNames } from "primereact/utils";

// * Models
import { ComponentStyle } from "@models";

// * ListTemplate for CRUD
export const ListTemplate = <T,>(props : ListTemplateProps<T>) => {

    const {
        items,
        noItemsMessage,
        children,
        className,
        style
    } = props;

    if (!items || items.length === 0) {
        return (
            <div className="list-template-empty">
                <h3>{noItemsMessage}</h3>
            </div>
        )
    }

    const classes = classNames(
        'list-template',
        className
    )

    return (
        <div 
            className={classes}
            style={style}
        >
            {
                items.map((item, index) => (
                    children(item, index)
                ))
            }
        </div>
    )
}

interface ListTemplateProps<T> extends ComponentStyle {
    items: T[];
    noItemsMessage: string;
    children: (item : T, index: number) => ReactNode;
}