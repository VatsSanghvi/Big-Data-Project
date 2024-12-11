// * React Libraries
import { RouteObject } from "react-router-dom";

// * Pages
import { StoresPage } from "@pages";

export const adminRoutes : RouteObject[] = [
    {
        path: "/stores",
        element: <StoresPage />,
    }
]