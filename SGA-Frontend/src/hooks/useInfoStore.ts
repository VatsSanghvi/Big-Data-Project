// * Store
import { setCategories, setDepartments, setGroceryList, setGroceryListItems, setProducts, setStores } from "@store";

// * Hooks
import { useAppDispatch } from "./useStore";

// * Services
import { category, department, product, store, userProduct } from "@services";

// * Models
import { Category, Department, GroceryList, GroceryListItem, Role, User } from "@models";

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

  const getCategories = async (user_id: number, departments: Department[]) => {
    const { data } = await category.get(user_id);

    if (data.ok) {
      const categories: Category[] = [];

      for (const category of data.data) {
        const fk_store_id: number =
          departments.find(
            (department: Department) =>
              category.fk_department_id === department.department_id
          )?.fk_store_id ?? 0;

        categories.push({
          ...category,
          fk_store_id,
        });
      }

      dispatch(setCategories(categories));
    }
  };

  const getProducts = async (user_id: number) => {
    const { data } = await product.get(user_id);

    if (data.ok) dispatch(setProducts(data.data));
  };

  const getAllProducts = async () => {
    const { data } = await product.get_all();

    if (data.ok) dispatch(setProducts(data.data));
  };

  const getGroceryList = async (user_id: number) => {
    const { data } = await userProduct.getGroceryList(user_id);

    if (data.ok) {
      const groceryList : GroceryList = {
        id: data.data.id,
        user_id: data.data.user_id,
        name: data.data.name,
        total_spent: data.data.total_spent,
      }

      const items: GroceryListItem[] = data.data.items;

      dispatch(setGroceryList(groceryList));
      dispatch(setGroceryListItems(items));
    }
  };

  const getInfo = async (user: User) => {
    if (user.role === Role.Admin) {
      // * Fetch Stores
      const storeResponse = await getStores(user.user_id);

      if (storeResponse.ok) {
        // * Fetch Departments
        const departmentResponse = await getDepartments(user.user_id);

        if (departmentResponse.ok) {
          // * Fetch Categories
          await getCategories(user.user_id, departmentResponse.data);
        }

        await getProducts(user.user_id);
      }
    } else if (user.role === Role.User) {
      await getAllProducts();

      await getGroceryList(user.user_id);
    }
  };

  return {
    getInfo,
  };
};
