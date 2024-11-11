// * React Libraries
import { Navigate, RouteObject } from "react-router-dom";

export const adminRoutes : RouteObject[] = [
    {
        path: "/",
        element: <div> Layout </div>,
        errorElement: <Navigate to="/" />,
        children: [
            {
                path: 'store',
                element: <div>store</div>
            }
        ]
    }
]