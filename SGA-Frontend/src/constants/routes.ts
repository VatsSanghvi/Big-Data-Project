// * Routes
import { adminRoutes, managerRoutes, userRoutes } from "@routes";

// * Models
import { Role } from "@models";

export const roleRoutes = {
    [Role.User]: userRoutes,
    [Role.Manager]: managerRoutes,
    [Role.Admin]: adminRoutes
}