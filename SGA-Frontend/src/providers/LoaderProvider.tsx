
// * React Libraries
import { FC, ReactNode, useEffect } from "react";

// * Components
import { Loader } from "@components";

// * Hooks
import { useConfigStore } from "@hooks";

// * Services
import { instance } from "@services";



export const LoaderProvider : FC<LoaderProviderProps> = ({ children }) => {

    const { isLoading, updateLoading } = useConfigStore();

    useEffect(() => {
        instance.interceptors.request.use(config => {
            updateLoading(true);

            return config;
        });

        instance.interceptors.response.use(response => {
            updateLoading(false);

            return response;
        },
        error => {
            updateLoading(false);

            return Promise.reject(new Error(error));
        });
    }, []);

    

    return (
        <>
            {isLoading && <Loader />}
            {children}
        </>
    )
}

interface LoaderProviderProps {
    children: ReactNode;
}
