// * React Libraries
import { FC } from "react";

// * Models
import { Product } from "@models";

// * Components
import { ListTemplate } from "../ListTemplate";
import { ProductItemTemplate } from "./ProductItemTemplate";

export const ProductListTemplate: FC<ProductListTemplateProps> = (props) => {
    const {
        items,
        onAdd
    } = props;

    return (
        <ListTemplate<Product>
            noItemsMessage="No Products Found"
            items={items}
        >
            {
                (item, index) => (
                    <ProductItemTemplate
                        key={index}
                        item={item}
                        index={index}
                        onAdd={onAdd}
                    />
                )
            }
        </ListTemplate>
    )
}

interface ProductListTemplateProps {
    items: Product[];
    onAdd: (item: Product) => void;
}