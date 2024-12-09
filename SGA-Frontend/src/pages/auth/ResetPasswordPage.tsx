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
import { useNavigate, useParams } from "react-router-dom";
import { ResetPasswordRequest } from "@models";
import { useEffect } from "react";

export const RecoverPasswordPage = () => {

    const { showSuccess, showError } = useToast();
    const { email } = useParams();

    const navigate = useNavigate();

    const formik = useFormik<ResetPasswordRequest>({
        initialValues: recoverPasswordInitialValues,
        validationSchema: recoverPasswordValidationSchema,
        onSubmit: async (values) => {
            const { data } = await user.resetPassword(values.email, values);
            
            if (data.ok) {
                showSuccess("Success", data.message);
                navigate('/login');
            } else {
                showError("Error", data.message);
            }
        }
    });

    useEffect(() => {
        if (email) {
            formik.setFieldValue('email', email);
        }
    }, []);

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
                    {...getProps(formik, 'current_password', 'New Password')}
                    type="password"
                    inputMode="text"
                />
                <MInputText
                    {...getProps(formik, 'new_password', 'Confirm Password')}
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