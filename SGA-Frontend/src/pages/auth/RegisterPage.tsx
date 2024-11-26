// * Third Party Libraries
import { useFormik } from "formik";

// * Components
import { CardHeader, MInputNumber, MInputText, MPassword, NavigateButton, SubmitButton } from "@components"

// * Forms
import { registerInitialValues, registerValidationSchema } from "@forms";

// * Helpers
import { getProps } from "@helpers";

// * Hooks
import { useAuthStore, useToast } from "@hooks";

// * Models
import { RegisterRequest, Role, User } from "@models";

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

            const newUser : RegisterRequest = {
                first_name: values.firstName,
                last_name: values.lastName,
                email: values.email,
                password: values.password,
                phone_number: values.phoneNumber.toString(),
                role: Role.User
            }

            const response = await user.register(newUser);

            if (response.status === 200) {
                const data = response.data;

                const user : User = {
                    id: data.user_id,
                    firstName: data.first_name,
                    lastName: data.last_name,
                    email: data.email,
                    phoneNumber: data.phone_number,
                    role: data.role
                };

                onLogin(user);

                showSuccess("Registration Successful", `Welcome ${user.firstName} ${user.lastName}`);
                
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
                <MInputText {...getProps(formik, 'firstName', 'First Name')}/>
                <MInputText {...getProps(formik, 'lastName', 'Last Name')}/>
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
                    {...getProps(formik, 'confirmPassword', 'Confirm Password')}
                    toggleMask
                />
                <MInputNumber 
                    {...getProps(formik, 'phoneNumber', 'Phone Number')}
                    useGrouping={false}
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