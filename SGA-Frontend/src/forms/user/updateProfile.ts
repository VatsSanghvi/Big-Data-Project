// * Third Party Libraries
import { object, string } from "yup";

// * Models
import { UpdateProfileRequest } from "@models";

export const updateProfileInitialValues: UpdateProfileRequest = {
  first_name: "",
  last_name: "",
  email: "",
  phone_number: "",
};

export const updateProfileValidationSchema = object({
  first_name: string().required("First name is required"),
  last_name: string().required("Last name is required"),
  email: string()
    .email("It must be a valid email")
    .required("Email is required"),
  phone_number: string().required("Phone number is required"),
});
