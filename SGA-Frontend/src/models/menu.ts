import { Role } from "./auth";

export interface MenuOptions {
    label: string;
    icon: string;
    to: string;
    roles: Role[];
}