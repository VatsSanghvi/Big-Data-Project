// * React Libraries
import { FC } from "react";

// * Third Party Libraries
import { classNames } from "primereact/utils";

// * Models
import { Category } from "@models"

// * Components
import { EditButton } from "../EditButton";
import { DeleteButton } from "../DeleteButton";

export const CategoryItemTemplate : FC<CategoryItemTemplateProps> = (props) => {

    const {
        item,
        index,
        onDelete,
        onEdit
    } = props;

    const classes = classNames(
        'category-item',
        {
            'border-top-1': index === 0
        }
    )

    return (
        <div className={classes}>
            <div className="deparment-item-info">
                <h3>{item.category_name}</h3>
            </div>
            <div className="department-item-actions">
                <EditButton onClick={() => onEdit(item)}/>
                <DeleteButton onClick={() => onDelete(item.category_id)}/>
            </div>
        </div>
    )
}

interface CategoryItemTemplateProps {
    item: Category;
    index: number;
    onDelete: (store_id: number) => void;
    onEdit: (item : Category) => void;
}