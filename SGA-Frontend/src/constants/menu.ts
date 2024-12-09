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
        icon: "user",
        to: "/profile",
        roles: [Role.User, Role.Admin],
    },
    {
        label: "Grocery List",
        icon: "list",
        to: "/grocery-list",
        roles: [Role.User],
    },
    {
        label: 'Departments',
        icon: 'building',
        to: '/departments',
        roles: [Role.Admin]
    },
    {
        label: 'Categories',
        icon: 'sitemap',
        to: '/categories',
        roles: [Role.Admin]
    },
    {
        label: 'Products',
        icon: 'headphones',
        to: '/products-admin',
        roles: [Role.Admin]
    },
    {
        label: "Products",
        icon: "shopping-cart",
        to: "/products",
        roles: [Role.User],
    },
];
