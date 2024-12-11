import { RegisterForm, Role } from "@models";
import { object, ref, string } from "yup";

export const registerInitialValues : RegisterForm = {
    first_name: '',
    last_name: '',
    email: '',
    password: '',
    confirm_password: '',
    phone_number: '',
    role: Role.User,
}

export const registerValidationSchema = object({
    first_name: string()
                .required('First Name is required'),
    last_name: string()
                .required('Last Name is required'),
    email: string()
            .email('It must be a valid email')
            .required('Email is required'),
    password: string()
            .required('Password is required')
            .min(8, 'Password must be at least 8 characters'),
    confirm_password: string()
            .required('Confirm your password')
            .oneOf([ref('password')], 'Passwords must match'),
    phone_number: string()
            .required('Phone Number is required')
            .length(10, 'Phone Number must be 10 digits'),
    role: string()
});