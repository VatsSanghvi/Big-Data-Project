// * React Libraries
import { FC, ReactNode } from "react";

// * Third Party Libraries
import { Dialog } from "primereact/dialog";

// * Models
import { DialogMode, DialogTitle } from "@models";

// * Components
import { CrudDialogFooter } from "./CrudDialogFooter";

// * Dialog for CRUD operations
export const CrudDialog : FC<CrudDialogProps> = (props) => {
    const {
        openMode,
        setOpenMode,
        title,
        children,
        onSubmit
    } = props;

    return (
        <Dialog
            className="crud-dialog"
            header={`${DialogTitle[openMode]} ${title}`}
            visible={openMode !== DialogMode.CLOSE}
            onHide={() => setOpenMode(DialogMode.CLOSE)}
            footer={
                <CrudDialogFooter 
                    openMode={openMode} 
                    setOpenMode={setOpenMode} 
                    onSubmit={onSubmit}
                    title={title}
                />
            }
        >
            {children}
        </Dialog>
    )
}

interface CrudDialogProps {
    openMode: DialogMode;
    setOpenMode: (mode: DialogMode) => void;
    title: string;
    children: ReactNode;
    onSubmit: () => void;
}