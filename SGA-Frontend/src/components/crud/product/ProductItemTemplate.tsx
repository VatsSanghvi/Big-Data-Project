// * React Libraries
import { FC } from "react";

// * Third Party Libraries
import { classNames } from "primereact/utils";

// * Models
import { Product } from "@models"

export const ProductItemTemplate: FC<ProductItemTemplateProps> = (props) => {

    const {
        item,
        index,
    } = props;

    const classes = classNames(
        'product-item',
        {
            'border-top-1': index === 0
        }
    )

    return (
        <div className={classes}>
            <div className="deparment-item-info">
                <h3>{item.product_name}</h3>
            </div>
        </div>
    )
}

interface ProductItemTemplateProps {
    item: Product;
    index: number;
}