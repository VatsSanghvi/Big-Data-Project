// * React Libraries
import { Navigate, RouteObject } from "react-router-dom";

// * Layouts
import { AuthLayout } from "@layout";

// * Pages
import { LoginPage, /*RecoverPasswordPage,*/ RegisterPage, SendEmailPage } from "@pages";
import { PublicRoute } from "./decorators";

export const authRoutes: RouteObject[] = [
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
                path: '/send-email',
                element: <SendEmailPage />
            },
            // {
            //     path: '/reset-password/:email',
            //     element: <RecoverPasswordPage />
            // },
            {
                path: '*',
                element: <Navigate to="/login" />
            }
        ]
    }
]