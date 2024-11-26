import { loggedDefaultRoute } from "@constants";
import { useAuthStore } from "@hooks";
import { Role } from "@models"
import { FC, ReactNode } from "react";
import { Navigate } from "react-router-dom";

export const RolesRoute : FC<RolesRouteProps> = ({ allowedRoles, children }) => {

    const { user } = useAuthStore();

    if (!allowedRoles.includes(user.role)) return <Navigate to={loggedDefaultRoute} replace/>

    return children;
}

interface RolesRouteProps {
    allowedRoles: Role[];
    children: ReactNode;
}