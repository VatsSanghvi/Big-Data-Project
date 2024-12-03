import { ComponentStyle } from "@models";
import { classNames } from "primereact/utils";
import { FC, ReactNode } from "react";

export const ListTemplate : FC<ListTemplateProps> = (props) => {

    const {
        items,
        noItemsMessage,
        itemTemplate,
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
                    itemTemplate(index, item)
                ))
            }
        </div>
    )
}

interface ListTemplateProps extends ComponentStyle {
    items: unknown[];
    noItemsMessage: string;
    itemTemplate: (index: number, props: unknown) => ReactNode;
}