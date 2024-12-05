// * Third Party Libraries
import { useFormik } from "formik"
import { Button } from "primereact/button"

// * Components
import { CardHeader, MInputText, MPassword, NavigateButton, SubmitButton } from "@components"

// * Forms
import { loginInitialValues, loginValidationSchema } from "@forms"

// * Helpers
import { getProps } from "@helpers"

// * Hooks
import { useAuthStore, useInfoStore, useToast } from "@hooks"

// * Services
import { user } from "@services"

export const LoginPage = () => {

    const { onLogin } = useAuthStore();
    const { getInfo } = useInfoStore();

    const { showSuccess, showError } = useToast();

    const formik = useFormik({
        initialValues: loginInitialValues,
        validationSchema: loginValidationSchema,
        onSubmit: async(values) => {
            console.log(values);
            const response = await user.login(values);

            if (response.status === 200) {
                const data = response.data;

                onLogin(data);

                await getInfo(data);

                showSuccess("Login Successful", `Welcome ${data.first_name} ${data.last_name}`);
            }
            else {
                showError("Error", "Login Failed");
            }
        }
    });

    return (
        <div className="login">
            <CardHeader title="Sign In" />
            <form
                onSubmit={formik.handleSubmit}
            >
                <MInputText
                    {...getProps(formik, 'email', 'Email')}
                    type="email"
                    inputMode="email"
                />
                <MPassword 
                    {...getProps(formik, 'password', 'Password')}
                    toggleMask
                />
                <div className="forgot-password">
                    <Button
                        link
                    >
                        Forgot Password?
                    </Button>
                </div>
                <SubmitButton
                    className="submit-button"
                    size="large"
                >
                    Sign In
                </SubmitButton>
                <div
                    className="signup-link"
                >
                    <p>Dont have an account?</p>
                    <NavigateButton
                        link
                        go="/register"
                    >
                        Sign Up Now
                    </NavigateButton>
                </div>
            </form>
        </div>
    )
}