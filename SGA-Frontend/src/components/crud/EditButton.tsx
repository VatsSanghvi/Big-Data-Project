// * React Libraries
import { FC } from "react";

// * Third Party Libraries
import { Button } from "primereact/button";

// * Models
import { ComponentStyle } from "@models";

export const EditButton : FC<EditButtonProps> = (props) => {

    const {
        onClick,
        className,
        style,
        icon = 'pi-pencil',
    } = props;

    return (
        <Button 
            rounded 
            icon={`pi ${icon}`} 
            severity="info" 
            aria-label="Edit" 
            className={className}
            style={style}
            onClick={onClick}
        />
    )
}

interface EditButtonProps extends ComponentStyle {
    onClick: () => void;
    icon?: string;
}