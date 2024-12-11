// * React Libraries
import { Navigate, RouteObject } from "react-router-dom";

// * Layouts
import { GeneralLayout } from "@layout";

// * Pages
import { PublicRoute } from "./decorators";

export const commonRoutes: RouteObject[] = [
    {
        element: (
            <PublicRoute>
                <GeneralLayout />
            </PublicRoute>
        ),
        children: [
            {
                index: true,
                loader: () => <Navigate to="/home" />,
            },
            {
                path: '/home',
                element: <div>Home</div>
            }
        ]
    },
]