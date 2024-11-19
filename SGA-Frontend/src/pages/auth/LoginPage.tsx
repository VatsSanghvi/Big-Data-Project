// * Third Party Libraries
import { useFormik } from "formik"
import { Button } from "primereact/button"

// * Components
import { CardHeader, MInputText, MPassword } from "@components"

// * Forms
import { loginInitialValues, loginValidationSchema } from "@forms"
import { user } from "@services"

export const LoginPage = () => {

    const formik = useFormik({
        initialValues: loginInitialValues,
        validationSchema: loginValidationSchema,
        onSubmit: async({email, password}) => {
            const response = await user.login(email, password);

            console.log(response.data);
        }
    })

    return (
        <div className="w-full login">
            <CardHeader title="Sign In" />
            <form
                onSubmit={formik.handleSubmit}
            >
                <MInputText 
                    formik={formik}
                    name="email"
                    label="Username"
                    type="email"
                    inputMode="email"
                    variant="filled"
                />
                <MPassword 
                    formik={formik}
                    name="password"
                    label="Password"
                    variant="filled"
                />
                <div className="forgot-password">
                    <Button
                        link
                    >
                        Forgot Password?
                    </Button>
                </div>
                <Button
                    type="submit"
                    className="submit-button"
                    size="large"
                >
                    Sign In
                </Button>
                <div
                    className="signup-link"
                >
                    <p>Dont have an account?</p>
                    <Button
                        link
                    >
                        Sign Up Now
                    </Button>
                </div>
            </form>
        </div>
    )
}