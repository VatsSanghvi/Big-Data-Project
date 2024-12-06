// * Models
import { Login, RegisterRequest } from "@models";

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
    }
}