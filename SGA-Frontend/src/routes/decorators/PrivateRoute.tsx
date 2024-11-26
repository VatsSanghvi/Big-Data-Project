// * React Libraries
import { FC, ReactNode } from "react";
import { Navigate } from "react-router-dom";

// * Hooks
import { useAuthStore } from "@hooks";

// * Models
import { LoginState } from "@models";

// * Constants
import { unLoggedDefaultRoute } from "@constants";

export const PrivateRoute : FC<PublicRouteProps> = ({ children }) => {
    const { authState } = useAuthStore();

    if (authState === LoginState.UnAuthenticated) return <Navigate to={unLoggedDefaultRoute} replace/>
    
    return children;
}

interface PublicRouteProps {
    children: ReactNode;
}