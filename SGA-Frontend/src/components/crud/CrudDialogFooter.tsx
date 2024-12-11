// * React Libraries
import { FC } from "react";

// * Third Party Libraries
import { Button } from "primereact/button";

// * Models
import { DialogMode, DialogTitle } from "@models";

// * Footer for CRUD Dialog
export const CrudDialogFooter : FC<CrudDialogFooterProps> = (props) => {
    const {
        openMode,
        setOpenMode,
        title,
        onSubmit
    } = props;

    return (
        <div>
            <Button 
                label="Cancel"
                icon="pi pi-times"
                onClick={() => setOpenMode(DialogMode.CLOSE)}
            />
            <Button 
                autoFocus
                label={`${DialogTitle[openMode]} ${title}`}
                icon="pi pi-check"
                onClick={onSubmit}
            />
        </div>
    )
}

interface CrudDialogFooterProps {
    openMode: DialogMode;
    setOpenMode: (mode: DialogMode) => void;
    title: string;
    onSubmit: () => void;
}