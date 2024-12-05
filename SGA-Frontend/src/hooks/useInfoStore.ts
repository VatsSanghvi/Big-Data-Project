// * Store
import { setStores } from "@store";

// * Hooks
import { useAppDispatch } from "./useStore"

// * Services
import { store } from "@services";

// * Models
import { Role, User } from "@models";


export const useInfoStore = () => {
    const dispatch = useAppDispatch();

    const getInfo = async (user: User) => {

        if (user.role === Role.Admin) {
            // * Fetch Stores
            const { status, data } = await store.get(user.user_id);
    
            if (status === 200) dispatch(setStores(data));   
            
        }
    };

    return {
        getInfo
    }
}
