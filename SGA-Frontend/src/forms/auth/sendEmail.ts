import { SendEmailForm } from "@models";
import { object, string } from "yup";

export const sendEmailFormInitialValues: SendEmailForm = {
    sender_email: 'adminSGA@test.com',
    to_email: '',
};

export const sendEmailFormValidationSchema = object<SendEmailForm>({
    sender_email: string(),
    to_email: string()
        .email('It must be a valid email')
        .required('Email is required'),
})