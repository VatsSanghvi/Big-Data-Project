import { RegisterForm, Role } from "@models";
import { number, object, ref, string } from "yup";

export const registerInitialValues : RegisterForm = {
    firstName: '',
    lastName: '',
    email: '',
    password: '',
    confirmPassword: '',
    phoneNumber: '',
    role: Role.User,
}

export const registerValidationSchema = object({
    firstName: string()
                .required('First Name is required'),
    lastName: string()
                .required('Last Name is required'),
    email: string()
            .email('It must be a valid email')
            .required('Email is required'),
    password: string()
            .required('Password is required')
            .min(8, 'Password must be at least 8 characters'),
    confirmPassword: string()
            .required('Confirm your password')
            .oneOf([ref('password')], 'Passwords must match'),
    phoneNumber: number()
            .required('Phone Number is required')
            .integer('No decimals are allowed'),
    role: string()
});