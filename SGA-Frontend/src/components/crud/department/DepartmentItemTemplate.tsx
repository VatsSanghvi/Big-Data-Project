// * React Libraries
import { FC } from "react";

// * Third Party Libraries
import { classNames } from "primereact/utils";

// * Models
import { Department } from "@models"

// * Components
import { EditButton } from "../EditButton";
import { DeleteButton } from "../DeleteButton";

export const DepartmentItemTemplate : FC<DepartmentItemTemplateProps> = (props) => {

    const {
        item,
        index,
        onDelete,
        onEdit
    } = props;

    const classes = classNames(
        'department-item',
        {
            'border-top-1': index === 0
        }
    )

    return (
        <div className={classes}>
            <div className="deparment-item-info">
                <h3>{item.department_name}</h3>
            </div>
            <div className="department-item-actions">
                <EditButton onClick={() => onEdit(item)}/>
                <DeleteButton onClick={() => onDelete(item.department_id)}/>
            </div>
        </div>
    )
}

interface DepartmentItemTemplateProps {
    item: Department;
    index: number;
    onDelete: (store_id: number) => void;
    onEdit: (item : Department) => void;
}