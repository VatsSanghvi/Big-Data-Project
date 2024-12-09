// * Third Party Libraries
import { object, string } from "yup";

// * Models
import { ResetPasswordRequest } from "@models";

export const recoverPasswordInitialValues: ResetPasswordRequest = {
  email: "",
  current_password: "",
  new_password: "",
};

export const recoverPasswordValidationSchema = object({
  email: string(),
  current_password: string().required("Current password is required"),
  new_password: string().required("New password is required"),
});
