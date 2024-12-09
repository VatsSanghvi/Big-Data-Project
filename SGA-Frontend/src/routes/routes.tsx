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
import { CategoriesPage, DepartmentsPage, StoresPage, ProfilePage, UserProductsPage, ProductsPage } from "@pages";

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
            {
                path: "/profile",
                element: (
                    <RolesRoute allowedRoles={[Role.User, Role.Admin]}>
                        <ProfilePage />
                    </RolesRoute>
                )
            },
            {
                path: '/departments',
                element: (
                    <RolesRoute allowedRoles={[Role.Admin]}>
                        <DepartmentsPage />
                    </RolesRoute>
                )
            },
            {
                path: '/categories',
                element: (
                    <RolesRoute allowedRoles={[Role.Admin]}>
                        <CategoriesPage />
                    </RolesRoute>
                )
            },
            {
                path: '/products-admin',
                element: (
                    <RolesRoute allowedRoles={[Role.Admin]}>
                        <ProductsPage />
                    </RolesRoute>
                )
            },
            {
                path: "/products",
                element: (
                    <RolesRoute allowedRoles={[Role.User]}>
                        <UserProductsPage />
                    </RolesRoute>
                )
            },
        ]
    }
]