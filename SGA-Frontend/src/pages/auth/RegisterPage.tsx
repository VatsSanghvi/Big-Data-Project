// * Third Party Libraries
import { useFormik } from "formik";

// * Components
import { CardHeader, MInputMask, MInputText, MPassword, NavigateButton, SubmitButton } from "@components"

// * Forms
import { registerInitialValues, registerValidationSchema } from "@forms";

// * Helpers
import { getProps } from "@helpers";

// * Hooks
import { useAuthStore, useToast } from "@hooks";

// * Models
import { RegisterRequest } from "@models";

// * Services
import { user } from "@services";

export const RegisterPage = () => {

    const { onLogin } = useAuthStore();
    const { showSuccess, showError } = useToast();

    const formik = useFormik({
        initialValues: registerInitialValues,
        validationSchema: registerValidationSchema,
        onSubmit: async(values) => {
            console.log(values);

            const { confirm_password, ...rest } = values;

            const newUser : RegisterRequest = rest

            const response = await user.register(newUser);

            if (response.status === 200) {
                const data = response.data;

                onLogin(data);

                showSuccess("Registration Successful", `Welcome ${data.first_name} ${data.last_name}`);
                
            } else {
                showError("Error", "Registration Failed");
            }
        }
    });

    return (
        <div className="register">
            <CardHeader title="Sign Up" />
            <form
                onSubmit={formik.handleSubmit}
            >
                <MInputText {...getProps(formik, 'first_name', 'First Name')}/>
                <MInputText {...getProps(formik, 'last_name', 'Last Name')}/>
                <MInputText 
                    {...getProps(formik, 'email', 'Email')}
                    type="email"
                    inputMode="email"
                />
                <MPassword 
                    {...getProps(formik, 'password', 'Password')}
                    toggleMask
                />
                <MPassword 
                    {...getProps(formik, 'confirm_password', 'Confirm Password')}
                    toggleMask
                />
                <MInputMask
                    {...getProps(formik, 'phone_number', 'Phone Number')}
                    unmask
                    mask="(999) 999-9999"
                />
                <SubmitButton
                    className="submit-button"
                    size="large"
                >
                    Sign In
                </SubmitButton>

                <div
                    className="signin-link"
                >
                    <p>Already registered?</p>
                    <NavigateButton
                        link
                        go="/login"
                    >
                        Sign Up Now
                    </NavigateButton>
                </div>
            </form>
        </div>
    )
}