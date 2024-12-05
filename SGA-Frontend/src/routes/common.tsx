// * React Libraries
import { Navigate, RouteObject } from "react-router-dom";

export const commonRoutes : RouteObject[] = [
    // {
    //     index: true,
    //     loader: () => <Navigate to="/home" />,
    // },
    {
        path: '/home',
        element: <div>Home</div>
    }
]