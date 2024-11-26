import { MenuOptions, Role } from "@models";


export const menuOptions: MenuOptions[] = [
    {
        label: 'Stores',
        icon: 'shop',
        to: '/stores',
        roles: [Role.Admin]
    }
] 