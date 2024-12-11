// * React Libraries
import { FC } from "react";

// * Third Party Components
import { Button } from "primereact/button";
import { classNames } from "primereact/utils";

// * Models
import { Style } from "@models";

// * Button to add new item
export const AddButton : FC<Style<AddButtonProps>> = (props) => {

    const {
        label,
        onClick,
        icon='pi-plus',
        className,
        style,
        wrapperClassName,
        wrapperStyle
    } = props;

    const wrapperClasses = classNames(
        'add-button',
        wrapperClassName
    );

    return (
        <div
            className={wrapperClasses}
            style={wrapperStyle}
        >
            <Button 
                label={label}
                icon={`pi ${icon}`}
                onClick={onClick}
                className={className}
                style={style}
            />
        </div>
    )
}

interface AddButtonProps {
    label: string;
    onClick: () => void;
    icon?: string;
}