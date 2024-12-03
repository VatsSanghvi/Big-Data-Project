import { DialogMode, DialogTitle } from "@models";
import { Dialog } from "primereact/dialog";
import { FC, ReactNode } from "react";
import { CrudDialogFooter } from "./CrudDialogFooter";

export const CrudDialog : FC<CrudDialogProps> = (props) => {
    const {
        mode,
        setMode,
        title,
        children,
        onSubmit
    } = props;

    return (
        <Dialog
            className="crud-dialog"
            header={`${DialogTitle[mode]} ${title}`}
            visible={mode !== DialogMode.CLOSE}
            onHide={() => setMode(DialogMode.CLOSE)}
            footer={
                <CrudDialogFooter 
                    mode={mode} 
                    setMode={setMode} 
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
    mode: DialogMode;
    setMode: (mode: DialogMode) => void;
    title: string;
    children: ReactNode;
    onSubmit: () => void;
}