import { endpoints } from "@constants";
import { instance } from "./axiosService";


export const user = {
    login: async (email: string, password: string) => {
        return await instance.post(endpoints.auth.login, {
            email,
            password
        });
    }
}