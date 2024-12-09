// * React Libraries
import { FC } from "react";

// * Third Party Libraries
import { classNames } from "primereact/utils";

// * Models
import { Product } from "@models"
import { AddButton } from "../AddButton";

export const ProductItemTemplate: FC<ProductItemTemplateProps> = (props) => {

    const {
        item,
        index,
        onAdd
    } = props;

    const classes = classNames(
        'product-item',
        {
            'border-top-1': index === 0
        }
    )

    return (
        <div className={classes}>
            <div className="product-item-info">
                <h3>{item.product_name}</h3>
                <p>Price: {item.price}</p>
                <p>Stock Available: {item.stock_quantity}</p>
                <p>Status: {item.status}</p>
                <p>Store: {item.store.store_name}</p>
            </div>
            <div className="product-item-actions">
                <AddButton 
                    label=""
                    onClick={() => onAdd(item)}
                />
            </div>
        </div>
    )
}

interface ProductItemTemplateProps {
    item: Product;
    index: number;
    onAdd: (item: Product) => void;
}