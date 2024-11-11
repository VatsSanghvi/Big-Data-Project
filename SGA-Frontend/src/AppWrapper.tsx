// * Third Party Libraries
import { PrimeReactProvider } from "primereact/api";

// * Components
import { App } from "./App";

// * Providers
import { LoaderProvider, ToastProvider } from "@providers";

// * Styles
import  'primeflex/primeflex.css';
import 'primeicons/primeicons.css';
import '@styles/index.scss';
import "primereact/resources/themes/md-light-indigo/theme.css";

export const AppWrapper = () => {
    return (
        <PrimeReactProvider>
            <LoaderProvider>
                <ToastProvider>
                    <App />
                </ToastProvider>
            </LoaderProvider>
        </PrimeReactProvider>
    )
}