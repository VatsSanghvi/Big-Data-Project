import { MenuOptions, Role } from "@models";

export const menuOptions: MenuOptions[] = [
  {
    label: "Stores",
    icon: "shop",
    to: "/stores",
    roles: [Role.Admin],
  },
  {
    label: "User Profile",
    icon: "bars",
    to: "/profile",
    roles: [Role.User],
  },
  {
    label: "Budget",
    icon: "dollar",
    to: "/budget",
    roles: [Role.User],
  },
];
