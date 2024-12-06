// * React Libraries
import { FC } from "react";

// * Third Party Libraries
import { Button } from "primereact/button";

// * Models
import { ComponentStyle } from "@models";

export const DeleteButton : FC<DeleteButtonProps> = (props) => {

    const {
        onClick,
        className,
        style,
        icon = 'pi-trash',
    } = props;

    return (
        <Button 
            rounded 
            icon={`pi ${icon}`} 
            severity="danger" 
            aria-label="Delete" 
            className={className}
            style={style}
            onClick={onClick}
        />
    )
}

interface DeleteButtonProps extends ComponentStyle {
    onClick: () => void;
    icon?: string;
}