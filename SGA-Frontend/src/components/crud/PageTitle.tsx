// * React Libraries
import { FC } from "react";

// * Third Party Libraries
import { classNames } from "primereact/utils";

// * Models
import { Style } from "@models";

// * Page Title Component
export const PageTitle : FC<Style<PageTitleProps>> = (props) => {
    const {
        title,
        className,
        style,
        wrapperClassName,
        wrapperStyle
    } = props;

    const wrapperClasses = classNames(
        'page-title',
        wrapperClassName
    )

    return (
        <div 
            className={wrapperClasses}
            style={wrapperStyle}
        >
            <h1
                className={className}
                style={style}
            >
                {title}
            </h1>
        </div>
    )
}

interface PageTitleProps {
    title: string;
}