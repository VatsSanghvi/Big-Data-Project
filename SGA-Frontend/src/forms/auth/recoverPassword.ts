// * Third Party Libraries
import { object, string } from "yup";

// * Models
import { RecoverPassword } from "@models";

export const recoverPasswordInitialValues: RecoverPassword = {
  currentPassword: "",
  newPassword: "",
};

export const recoverPasswordValidationSchema = object({
  email: string()
    .email("It must be a valid email")
    .required("Email is required"),
  currentPassword: string().required("Current password is required"),
  newPassword: string().required("New password is required"),
});
