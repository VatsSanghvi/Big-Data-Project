// * React Libraries
import { FC, ReactNode } from "react";
import { Navigate } from "react-router-dom";

// * Hooks
import { useAuthStore } from "@hooks";

// * Models
import { LoginState } from "@models";

// * Constants
import { roleRoutes } from "@constants";

export const PublicRoute: FC<PublicRouteProps> = ({ children }) => {
    const { authState, user } = useAuthStore();

    if (authState === LoginState.Authenticated) return <Navigate to={roleRoutes[user.role]} replace />

    return children;
}

interface PublicRouteProps {
    children: ReactNode;
}