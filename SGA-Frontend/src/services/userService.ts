// * Models
import { LoginForm, RegisterForm } from "@models";

// * Constants
import { endpoints } from "@constants";

// * Services
import { instance } from "./axiosService";


export const user = {
    login: (user: LoginForm) => {
        return instance.post(endpoints.auth.login, user);
    },
    register: async (values: RegisterForm) => {
        return await instance.post(endpoints.auth.register, values);
    }
}