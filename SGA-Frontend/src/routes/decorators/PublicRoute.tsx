// * React Libraries
import { FC, ReactNode } from "react";
import { Navigate } from "react-router-dom";

// * Hooks
import { useAuthStore } from "@hooks";

// * Models
import { LoginState } from "@models";

// * Constants
import { loggedDefaultRoute } from "@constants";

export const PublicRoute : FC<PublicRouteProps> = ({ children }) => {
    const { authState } = useAuthStore();

    if (authState === LoginState.Authenticated) return <Navigate to={loggedDefaultRoute} replace/>
    
    return children;
}

interface PublicRouteProps {
    children: ReactNode;
}