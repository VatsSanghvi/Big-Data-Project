// * React Libraries
import { Navigate, RouteObject } from "react-router-dom";

export const authRoutes : RouteObject[] = [
    {
        path: '/',
        element: <div> Layout </div>,
        errorElement: <Navigate to="/" />,
        children: [
            {
                index: true,
                path: '/',
                element: <div>Home</div>
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