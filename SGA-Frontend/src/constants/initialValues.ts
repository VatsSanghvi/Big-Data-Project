// * Models
import { LoginState, Role } from "@models";

export const initialAuthValues = {
    authState: LoginState.UnAuthenticated,
    user: {
        user_id: 0,
        first_name: '',
        last_name: '',
        email: '',
        phone_number: '',
        role: Role.User
    }
}