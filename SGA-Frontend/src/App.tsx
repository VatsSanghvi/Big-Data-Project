import { roleRoutes } from "@constants";
import { useAuthStore } from "@hooks";
import { LoginState } from "@models";
import { authRoutes, commonRoutes } from "@routes";
import { useMemo } from "react";
import { createBrowserRouter, RouterProvider } from "react-router-dom";

const authRouteStates = [LoginState.UnAuthenticated, LoginState.Checking];

export const App = () => {

    const { authState, role } = useAuthStore();

    const routes = useMemo(() => {
        if (authRouteStates.includes(authState)) return authRoutes;

        return [...commonRoutes, ...roleRoutes[role]];

        
    }, [authState, role]);

    return (
        <RouterProvider router={createBrowserRouter(routes)}/>
    )
}
