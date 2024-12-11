// * React Libraries
import { Navigate, RouteObject } from "react-router-dom";

export const managerRoutes : RouteObject[] = [
    {
        path: "/",
        element: <div> Layout </div>,
        errorElement: <Navigate to="/" />,
        children: [
            {
                path: 'inventory',
                element: <div>Inventory</div>
            }
        ]
    }
]