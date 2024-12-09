// * Models
import {
  Login,
  RegisterRequest,
  ResetPasswordRequest,
  UpdateProfileRequest,
} from "@models";

// * Constants
import { endpoints } from "@constants";

// * Services
import { instance } from "./axiosService";

export const user = {
  login: (user: Login) => {
    return instance.post(endpoints.auth.login, user);
  },
  register: (values: RegisterRequest) => {
    return instance.post(endpoints.auth.register, values);
  },
  sendEmail: (values: { email: string }) => {
    return instance.post(endpoints.auth.sendEmail, values);
  },
  resetPassword: (email: string, values: ResetPasswordRequest) => {
    return instance.put(`${endpoints.auth.resetPassword}/${email}`, values);
  },
  updateProfile: (user_id: number, values: UpdateProfileRequest) => {
    return instance.put(`${endpoints.auth.updateProfile}/${user_id}`, values);
  },
};
