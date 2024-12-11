// * React Libraries
import { FC } from "react";

// * Third Party Libraries
import { classNames } from "primereact/utils";

// * Models
import { GroceryListItem } from "@models";

// * Hooks
import { useAppSelector } from "@hooks";

// * Components
import { EditButton } from "../EditButton";
import { DeleteButton } from "../DeleteButton";

export const GroceryListItemTemplate: FC<GroceryListItemTemplateProps> = (props) => {

    const {
        item,
        index,
        onEdit,
        onDelete
    } = props;

    const { products } = useAppSelector(state => state.info);

    const product = products.find(p => p.product_id === item.product_id);

    const classes = classNames(
        'product-item',
        {
            'border-top-1': index === 0
        }
    )

    return (
        <div className={classes}>
            <div className="product-item-info">
                <h3>{product?.product_name}</h3>
                <p>Price: {product?.price}</p>
                <p>Quantity: {item.quantity}</p>
            </div>
            <div className="product-item-actions">
                <EditButton onClick={() => onEdit(item)}/>
                <DeleteButton onClick={() => onDelete(item.id)}/>
            </div>
        </div>
    )
}

interface GroceryListItemTemplateProps {
    item: GroceryListItem;
    index: number;
    onEdit: (item: GroceryListItem) => void;
    onDelete: (grocery_list_item_id: number) => void;
}