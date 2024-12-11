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

// * Forms
import { sendEmailFormInitialValues, sendEmailFormValidationSchema } from "@forms";

// * Models
import { SendEmailForm } from "@models";

export const SendEmailPage = () => {
    
    const { showSuccess, showError } = useToast();

    const formik = useFormik<SendEmailForm>({
        initialValues: sendEmailFormInitialValues,
        validationSchema: sendEmailFormValidationSchema,
        onSubmit: async(values) => {
            console.log(values);

            const { data } = await user.sendEmail(values);

            if (data.ok) {
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
                    {...getProps(formik, 'to_email', 'Email')}
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