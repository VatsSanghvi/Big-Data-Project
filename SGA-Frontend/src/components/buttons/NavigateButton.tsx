// * React Libraries
import { FC } from "react";
import { useNavigate } from "react-router-dom";

// * Third Party Libraries
import { Button, ButtonProps } from "primereact/button"

export const NavigateButton : FC<NavigateButtonProps> = (props) => {
    const {
        children,
        go
    } = props;

    const navigate = useNavigate();

    const goTo = () => navigate(go);

    return (
        <Button
            {...props}
            onClick={goTo}
        >
            {children}
        </Button>
    )
}

interface NavigateButtonProps extends Omit<ButtonProps, 'onClick'> {
    go: string;
}