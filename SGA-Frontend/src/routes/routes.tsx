// * React Libraries
import { RouteObject } from "react-router-dom";

// * Layout
import { GeneralLayout } from "@layout";

// * Models
import { Role } from "@models";

// * Routes
import { authRoutes } from "./auth";
import { commonRoutes } from "./common";

// * Components
import { PrivateRoute, RolesRoute } from "./decorators";

// * Pages
import { DepartmentsPage, StoresPage, /*ProfilePage*/ } from "@pages";

export const routes: RouteObject[] = [
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
                        <StoresPage />
                    </RolesRoute>
                )
            },
            // {
            //     path: "/profile",
            //     element: (
            //         <RolesRoute allowedRoles={[Role.User]}>
            //             <ProfilePage />
            //         </RolesRoute>
            //     )
            // },
            {
                path: '/departments',
                element: (
                    <RolesRoute allowedRoles={[Role.Admin]}>
                        <DepartmentsPage />
                    </RolesRoute>
                )
            }
        ]
    }
]