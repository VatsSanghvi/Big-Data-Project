import { User } from "./user";

export interface RegisterForm extends Omit<User, 'user_id'> {
    password: string;
    confirm_password: string;
}

export type RegisterRequest = Omit<RegisterForm, 'confirm_password'>;