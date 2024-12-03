// * React Libraries
import { FC } from "react";

// * Third Party Libraries
import { Button } from "primereact/button";

// * Models
import { DialogMode, DialogTitle } from "@models";

export const CrudDialogFooter : FC<CrudDialogFooterProps> = (props) => {
    const {
        mode,
        setMode,
        title,
        onSubmit
    } = props;

    return (
        <div>
            <Button 
                label="Cancel"
                icon="pi pi-times"
                onClick={() => setMode(DialogMode.CLOSE)}
            />
            <Button 
                autoFocus
                label={`${DialogTitle[mode]} ${title}`}
                icon="pi pi-check"
                onClick={onSubmit}
            />
        </div>
    )
}

interface CrudDialogFooterProps {
    mode: DialogMode;
    setMode: (mode: DialogMode) => void;
    title: string;
    onSubmit: () => void;
}