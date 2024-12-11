// * React Libraries
import { FC } from "react";

// * Models
import { Category } from "@models";

// * Components
import { ListTemplate } from "../ListTemplate";
import { CategoryItemTemplate } from "./CategoryItemTemplate";

// * Template for Category List
export const CategoryListTemplate : FC<CategoryListTemplateProps> = (props) => {
    const {
        items,
        onDelete,
        onEdit
    } = props;

    return (
        <ListTemplate<Category>
            noItemsMessage="No Categories Found" 
            items={items}
        >
            {
                (item, index) => (
                    <CategoryItemTemplate
                        key={index}
                        item={item} 
                        index={index}
                        onDelete={(store_id: number) => onDelete(store_id)}
                        onEdit={(item : Category) => onEdit(item)}
                    />
                )
            }
        </ListTemplate>
    )
}

interface CategoryListTemplateProps {
    items: Category[];
    onDelete: (store_id: number) => void;
    onEdit: (item: Category) => void;
}