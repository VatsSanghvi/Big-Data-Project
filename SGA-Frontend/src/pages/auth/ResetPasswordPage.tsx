// * Third Party Libraries
import { useFormik } from "formik";

// * Components
import { CardHeader, MInputText, SubmitButton } from "@components"

// * Forms
import { recoverPasswordInitialValues, recoverPasswordValidationSchema } from "@forms"

// * Helpers
import { getProps } from "@helpers";

// * Hooks
import { useToast } from "@hooks";

// * Services
import { user } from "@services";

// * React 
import { useParams } from "react-router-dom";
import { ResetPasswordRequest } from "@models";

export const RecoverPasswordPage = () => {

    const { showSuccess, showError } = useToast();
    const { email } = useParams();

    const formik = useFormik({
        initialValues: { ...recoverPasswordInitialValues, email },
        validationSchema: recoverPasswordValidationSchema,
        onSubmit: async (values) => {

            const { currentPassword, newPassword } = values;

            if (!email) {
                showError("Error", "Email is required");
                return;
            }
            const updatePassword: ResetPasswordRequest = { currentPassword, newPassword };

            const response = await user.resetPassword(email, updatePassword);

            console.log(response.data);
            if (response.data.ok) {
                showSuccess("Success", response.data.message);
            } else {
                showError("Error", response.data.message);
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
                    disabled
                />
                <MInputText
                    {...getProps(formik, 'currentPassword', 'Current Password')}
                    type="password"
                    inputMode="text"
                />
                <MInputText
                    {...getProps(formik, 'newPassword', 'New Password')}
                    type="password"
                    inputMode="text"
                />
                <SubmitButton
                    className="submit-button"
                    size="large"
                >
                    Update Password
                </SubmitButton>
            </form>
        </div>
    )
}