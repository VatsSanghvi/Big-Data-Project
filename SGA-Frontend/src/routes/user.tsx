// * React Libraries
import { Navigate, RouteObject } from "react-router-dom";

export const userRoutes: RouteObject[] = [
    {
        path: "/",
        element: <div> Layout </div>,
        errorElement: <Navigate to="/" />,
        children: [
            {
                path: 'profile',
                element: <div>Profile</div>
            },
            {
                path: 'products',
                element: <div>Products</div>
            }

        ]
    }
]