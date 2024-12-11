// * Third Party Components
import { useFormik } from "formik";

// * Components
import { CardHeader, MInputMask, MInputText, SubmitButton } from "@components"

// * Forms
import { updateProfileInitialValues, updateProfileValidationSchema } from "@forms";

// * Helpers
import { getProps } from "@helpers";

// * Hooks
import { useAuthStore, useToast } from "@hooks";

// * Models
import { UpdateProfileRequest } from "@models";

// * Services
import { user as userService } from "@services";

// * Local Components
import { useEffect } from "react";

export const ProfilePage = () => {

    const { user, updateUser } = useAuthStore();
    const { showSuccess, showError } = useToast();

    const formik = useFormik({
        initialValues: updateProfileInitialValues,
        validationSchema: updateProfileValidationSchema,
        onSubmit: async (values) => {
            console.log(values);

            const updateProfile: UpdateProfileRequest = values

            const response = await userService.updateProfile(user.user_id, updateProfile);

            if (response.data.ok) {
                const data = response.data.data;
                updateUser(data);

                showSuccess('Profile Updated Successfully', `Profile has been updated successfully ${data.first_name} ${data.last_name}`);

            } else {
                showError("Error", response.data.message);
            }
        }
    });

    useEffect(() => {
        if (user && user.user_id) {
            formik.setValues({
                ...user
            })
        }
    }, []);

    return (
        <div className="register">
            <CardHeader title="Update User" />
            <form
                onSubmit={formik.handleSubmit}
            >
                <MInputText {...getProps(formik, 'first_name', 'First Name')} />
                <MInputText {...getProps(formik, 'last_name', 'Last Name')} />
                <MInputText
                    {...getProps(formik, 'email', 'Email')}
                    type="email"
                    inputMode="email"
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
                    Save
                </SubmitButton>

            </form>
        </div>
    )
}