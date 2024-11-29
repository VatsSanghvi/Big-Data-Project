import { FC } from "react";
import { useNavigate } from "react-router-dom";

export const MenuItem : FC<MenuItemProps> = (props) => {

    const {
        label,
        icon,
        to,
        close
    } = props;

    const navigate = useNavigate();

    const onClick = () => {
        navigate(to);
        close();
    }

    return (
        <div
            className="menu-item"
            onClick={onClick}
            role="button"
        >
            <i className={`pi pi-${icon}`}></i>
            <p>{label}</p>
        </div>
    )
}

interface MenuItemProps {
    label: string;
    icon: string;
    to: string;
    close: () => void;
}