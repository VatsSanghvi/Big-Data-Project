import { Department } from "@models";
import { FC } from "react";
import { ListTemplate } from "../ListTemplate";
import { DepartmentItemTemplate } from "./DepartmentItemTemplate";

export const DepartmentListTemplate : FC<DepartmentListTemplateProps> = (props) => {

    const {
        items,
        onDelete,
        onEdit
    } = props;

    return (
        <ListTemplate<Department>
            noItemsMessage="No Departments Found" 
            items={items}
        >
            {
                (item, index) => (
                    <DepartmentItemTemplate 
                        key={index}
                        item={item} 
                        index={index}
                        onDelete={(store_id: number) => onDelete(store_id)}
                        onEdit={(item : Department) => onEdit(item)}
                    />
                )
            }
        </ListTemplate>
    )
}

interface DepartmentListTemplateProps {
    items: Department[];
    onDelete: (store_id: number) => void;
    onEdit: (item: Department) => void;
}