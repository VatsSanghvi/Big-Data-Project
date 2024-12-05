// * React Libraries
import { FC } from "react";

// * Models
import { Store } from "@models"

// * Components
import { ListTemplate } from "../ListTemplate";
import { StoreItemTemplate } from "./StoreItemTemplate";

export const StoreListTemplate : FC<StoreListTemplateProps> = (props) => {

    const {
        items,
        onDelete,
        onEdit
    } = props;

    return (
        <ListTemplate<Store>
            noItemsMessage="No Stores Found" 
            items={items}
        >
            {
                (item, index) => (
                    <StoreItemTemplate 
                        key={index}
                        item={item} 
                        index={index}
                        onDelete={(store_id: number) => onDelete(store_id)}
                        onEdit={(item : Store) => onEdit(item)}
                    />
                )
            }
        </ListTemplate>
    )
}

interface StoreListTemplateProps {
    items: Store[];
    onDelete: (store_id: number) => void;
    onEdit: (item: Store) => void;
}