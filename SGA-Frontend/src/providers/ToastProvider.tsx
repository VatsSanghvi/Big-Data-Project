import { Toast } from "primereact/toast"
import { FC, ReactNode, createContext, useMemo, useRef } from "react"


export const ToastContext = createContext<ToastContextProps | null>(null);

export const ToastProvider : FC<ToastProviderProps> = ({ children }) => {

    const toastRef = useRef<Toast>(null);

    const showToast = (severity: ToastSeverity, summary: string, detail: string) => {
        toastRef.current?.show({ severity, summary, detail });
    }

    const showSuccess = (summary: string, detail: string) => {
        showToast("success", summary, detail);
    }

    const showError = (summary: string, detail: string) => {
        showToast("error", summary, detail);
    }

    const value : ToastContextProps = useMemo(() => ({
        showToast,
        showSuccess,
        showError,
    }), []);

    return (
        <ToastContext.Provider value={value}>
            <Toast ref={toastRef} />
            {children}
        </ToastContext.Provider>
    )
}

type ToastSeverity = "success" | "info" | "warn" | "error";

interface ToastProviderProps {
    children: ReactNode;
}

interface ToastContextProps {
    showToast: (severity: ToastSeverity, summary: string, detail: string) => void;
    showSuccess: (summary: string, detail: string) => void;
    showError: (summary: string, detail: string) => void;
}