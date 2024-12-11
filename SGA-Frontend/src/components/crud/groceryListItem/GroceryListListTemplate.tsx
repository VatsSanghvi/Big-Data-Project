// * React Libraries
import { FC } from "react";

// * Models
import { GroceryListItem } from "@models";

// * Components
import { ListTemplate } from "../ListTemplate";
import { GroceryListItemTemplate } from "./GroceryListItemTemplate";

export const GroceryListListTemplate: FC<GroceryListListTemplateProps> = (props) => {
    const {
        items,
        onEdit,
        onDelete
    } = props;

    return (
        <ListTemplate<GroceryListItem>
            noItemsMessage="No Grocery List Items Added"
            items={items}
        >
            {
                (item, index) => (
                    <GroceryListItemTemplate
                        key={index}
                        item={item}
                        index={index}
                        onEdit={onEdit}
                        onDelete={onDelete}
                    />
                )
            }
        </ListTemplate>
    )
}

interface GroceryListListTemplateProps {
    items: GroceryListItem[];
    onEdit: (item: GroceryListItem) => void;
    onDelete: (grocery_list_item_id: number) => void;
}