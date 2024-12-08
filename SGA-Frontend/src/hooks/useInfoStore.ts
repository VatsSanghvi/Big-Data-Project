// * Store
import { setCategories, setDepartments, setProducts, setStores } from "@store";

// * Hooks
import { useAppDispatch } from "./useStore"

// * Services
import { category, department, product, store } from "@services";

// * Models
import { Category, Department, Role, User } from "@models";


export const useInfoStore = () => {
    const dispatch = useAppDispatch();

    const getStores = async (user_id: number) => {
        const { data } = await store.get(user_id);

        if (data.ok) dispatch(setStores(data.data));

        return data;
    };

    const getDepartments = async (user_id: number) => {

        const { data } = await department.get(user_id);

        if (data.ok) dispatch(setDepartments(data.data));

        return data;
    };

    const getCategories = async(user_id: number, departments: Department[]) => {

        const { data } = await category.get(user_id);
        
        if (data.ok) {
            const categories : Category[] = [];

            for (const category of data.data) {
                const fk_store_id : number = departments.find((department: Department) => category.fk_department_id === department.department_id)?.fk_store_id ?? 0

                categories.push({
                    ...category,
                    fk_store_id
                })
            }

            dispatch(setCategories(categories))
        }
    }

    const getProducts = async(user_id: number) => {
        const { data } = await product.get(user_id);

        if (data.ok) dispatch(setProducts(data.data));
    }

    const getInfo = async (user: User) => {

        if (user.role === Role.Admin) {
            // * Fetch Stores
            const storeResponse = await getStores(user.user_id);
    
            if (storeResponse.ok) {
                // * Fetch Departments
                const departmentResponse = await getDepartments(user.user_id);

                if (departmentResponse.ok) {
                    // * Fetch Categories
                    await getCategories(user.user_id, departmentResponse.data)
                }

                await getProducts(user.user_id);
            }
            
        }
    };

    return {
        getInfo
    }
}
