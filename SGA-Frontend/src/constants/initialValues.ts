// * Models
import { LoginState, Role } from "@models";

export const initialAuthValues = {
    authState: LoginState.UnAuthenticated,
    user: {
        id: 0,
        firstName: '',
        lastName: '',
        email: '',
        phoneNumber: '',
        role: Role.User
    }
}