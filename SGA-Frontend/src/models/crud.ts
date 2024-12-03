export enum DialogMode {
    CREATE,
    EDIT,
    CLOSE,
}

export const DialogTitle : Record<DialogMode, string> = {
    [DialogMode.CREATE]: 'Create New',
    [DialogMode.EDIT]: 'Edit',
    [DialogMode.CLOSE]: ''
}