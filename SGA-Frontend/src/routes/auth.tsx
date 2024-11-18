// * React Libraries
import { Navigate, redirect, RouteObject } from "react-router-dom";

// * Layouts
import { AuthLayout } from "@layout";

// * Pages
import { LoginPage } from "@pages";

export const authRoutes : RouteObject[] = [
    {
        path: '/',
        element: <AuthLayout />,
        errorElement: <Navigate to="/" />,
        children: [
            {
                index: true,
                loader: () => redirect('/login') 
            },
            {
                path: 'login',
                element: <LoginPage />
            },
            {
                path: 'register',
                element: <div>Register</div>
            },
            {
                path: 'reset',
                element: <div>Reset</div>
            },
            {
                path: 'reset-sent',
                element: <div>Reset Sent</div>
            },
            {
                path: 'new-password',
                element: <div>New Password</div>
            },
            {
                path: 'resseted',
                element: <div>Resetted</div>
            },
            {
                path: 'confirm',
                element: <div>Confirm</div>
            }
        ]
    }
]