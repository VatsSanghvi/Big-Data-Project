// * Store
import { setDepartments, setStores } from "@store";

// * Hooks
import { useAppDispatch } from "./useStore"

// * Services
import { department, store } from "@services";

// * Models
import { Department, Role, Store, User } from "@models";


export const useInfoStore = () => {
    const dispatch = useAppDispatch();

    const getStores = async (user_id: number) => {
        const { data } = await store.get(user_id);

        if (data.ok) dispatch(setStores(data.data));

        return data;
    };

    const getDepartments = async (stores: Store[]) => {

        let departaments : Department[] = [];

        for (const store of stores) {
            const { data } = await department.get(store.store_id);

            if (data.ok) {
                departaments = [
                    ...departaments,
                    ...data.data.map((department : Department) => {
                        return {
                            ...department,
                            fk_store_id: store.store_id
                        }
                    })
                ];
            }
        }

        console.log(departaments);

        dispatch(setDepartments(departaments));

        return {
            ok: true,
            data: departaments
        };

    };

    const getCategories = async(departments: Department[]) => {}

    const getInfo = async (user: User) => {

        if (user.role === Role.Admin) {
            // * Fetch Stores
            const storeResponse = await getStores(user.user_id);
    
            if (storeResponse.ok) {
                // * Fetch Departments
                await getDepartments(storeResponse.data);
            }
            
        }
    };

    return {
        getInfo
    }
}
