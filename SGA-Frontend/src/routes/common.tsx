// * React Libraries
import { Navigate, RouteObject } from "react-router-dom";

export const commonRoutes : RouteObject[] = [
    {
        path: "/",
        element: <div> Layout </div>,
        errorElement: <Navigate to="/" />,
        children: [
            {
                index: true,
                loader: () => <Navigate to="/home" />
            },
            {
                path: 'home',
                element: <div>Home</div>
            },
            {
                path: 'products',
                element: <div>Products</div>
            }
        ]
    }
]