import { Store } from "@models";
import { classNames } from "primereact/utils";
import { FC } from "react";
import { EditButton } from "../EditButton";
import { DeleteButton } from "../DeleteButton";

export const StoreItemTemplate : FC<StoreItemTemplateProps> = (props) => {
    const {
        item,
        index,
        onDelete,
        onEdit
    } = props;

    const classes = classNames(
        'store-item',
        {
            'border-top-1': index === 0
        }
    )

    return (
        <div className={classes}>
            <div className="store-item-info">
                <h3>{item.store_name}</h3>
                <p>{item.location}</p>
                {
                    item.manager && (
                        <p>Manager: {item.manager.first_name} {item.manager.last_name}</p>
                    )
                }
            </div>
            <div className="store-item-actions">
                <EditButton onClick={() => onEdit(item)}/>
                <DeleteButton onClick={() => onDelete(item.store_id)}/>
            </div>
        </div>
    )
}

interface StoreItemTemplateProps {
    item: Store;
    index: number;
    onDelete: (store_id: number) => void;
    onEdit: (item : Store) => void;
}