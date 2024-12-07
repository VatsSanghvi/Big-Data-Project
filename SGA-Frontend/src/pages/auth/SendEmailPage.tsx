// * Third Party Libraries
import { useFormik } from "formik";

// * Components
import { CardHeader, MInputText, NavigateButton, SubmitButton } from "@components"

// * Helpers
import { getProps } from "@helpers";

// * Hooks
import { useToast } from "@hooks";

// * Services
import { user } from "@services";
import {string} from "yup";

export const SendEmailPage = () => {
    
    const { showSuccess, showError } = useToast();

    const formik = useFormik({
        initialValues: {email: ''},
        validationSchema: {
            email: string()
            .email('It must be a valid email')
            .required('Email is required'),
        },
        onSubmit: async(values) => {
            console.log(values);

            const { email } = values;

            const sendEmail = { email }

            const response = await user.sendEmail(sendEmail);

            if (response.status === 200) {
                showSuccess("Email Sent", `Check your email for reset link`);
                
            } else {
                showError("Error", "Error sending email");
            }
        }
    });

    return (
        <div className="login">
            <CardHeader title="Password Recovery" />
            <form
                onSubmit={formik.handleSubmit}
            >
                <MInputText 
                    {...getProps(formik, 'email', 'Email')}
                    type="email"
                    inputMode="email"
                />
                <SubmitButton
                    className="submit-button"
                    size="large"
                >
                    Send email
                </SubmitButton>

                <div
                    className="signin-link"
                >
                    <NavigateButton
                        link
                        go="/login"
                    >
                        Back to Login
                    </NavigateButton>
                </div>
            </form>
        </div>
    )
}