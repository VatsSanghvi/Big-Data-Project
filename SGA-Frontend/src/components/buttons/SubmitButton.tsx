// * React Libraries
import { FC } from "react"

// * Third Party Libraries
import { Button, ButtonProps } from "primereact/button"

// * Submit Button for forms
export const SubmitButton : FC<Omit<ButtonProps, 'type'>> = (props) => {

    const { children } = props;

    return (
        <Button
            {...props}
            type="submit"
        >
            {children}
        </Button>
    )
}
