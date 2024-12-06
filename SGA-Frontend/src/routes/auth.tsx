// * React Libraries
import { Navigate, RouteObject } from "react-router-dom";

// * Layouts
import { AuthLayout } from "@layout";

// * Pages
import { LoginPage, RegisterPage } from "@pages";
import { PublicRoute } from "./decorators";

export const authRoutes : RouteObject[] = [
    {
        element: (
            <PublicRoute>
                <AuthLayout />
            </PublicRoute>
        ),
        children: [
            {
                index: true,
                loader: () => <Navigate to="/login" />,
            },
            {
                path: '/login',
                element: <LoginPage />
            },
            {
                path: '/register',
                element: <RegisterPage />
            },
            {
                path: '*',
                element: <Navigate to="/login" />
            }
        ]
    }
]