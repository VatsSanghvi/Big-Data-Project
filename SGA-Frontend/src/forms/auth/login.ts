// * Third Party Libraries
import { object, string } from "yup"

export const loginInitialValues = {
    email: '',
    password: ''
}

export const loginValidationSchema = object({
    email: string()
            .email('It must be a valid email')
            .required('Email is required'),
    password: string()
            .required('Password is required')
            
})