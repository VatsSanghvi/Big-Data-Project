import { RouteObject } from "react-router-dom";
import { PrivateRoute } from "./decorators";
import { GeneralLayout } from "@layout";
import { authRoutes } from "./auth";
import { commonRoutes } from "./common";
import { RolesRoute } from "./decorators/RolesRoute";
import { Role } from "@models";

export const routes : RouteObject[] = [
    ...authRoutes,
    {
        element: (
            <PrivateRoute>
                <GeneralLayout />
            </PrivateRoute>
        ),
        children: [
            ...commonRoutes,
            {
                path: "/stores",
                element: (
                    <RolesRoute allowedRoles={[Role.Admin]}>
                        <div>Store</div>
                    </RolesRoute>
                )
            }
        ]
    }
]