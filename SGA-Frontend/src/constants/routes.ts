import { Role } from "@models";

export const unLoggedDefaultRoute = "/login";
export const loggedDefaultRoute = "/stores";

export const roleRoutes: Record<Role, string> = {
  [Role.Admin]: "/stores",
  [Role.User]: "/profile",
  [Role.Manager]: "/stores",
};
