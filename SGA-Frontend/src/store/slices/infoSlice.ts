// * React Libraries
import { createSlice, PayloadAction } from '@reduxjs/toolkit';

// * Models
import { Category, Department, Product, Store } from '@models';

interface InfoState {
    stores: Store[];
    departments: Department[];
    categories: Category[];
    products: Product[];
}

const initialState : InfoState = {
    stores: [],
    departments: [],
    categories: [],
    products: []
};

export const infoSlice = createSlice({
    name: 'info',
    initialState,
    reducers: {
        setStores: (state, { payload } : PayloadAction<Store[]>) => {
            state.stores = payload;
        },
        addStore: (state, { payload } : PayloadAction<Store>) => {
            state.stores.push(payload);
        },
        updateStore: (state, { payload } : PayloadAction<Store>) => {
            const index = state.stores.findIndex(store => store.store_id === payload.store_id);
            state.stores[index] = payload;
        },
        deleteStore: (state, { payload } : PayloadAction<number>) => {
            state.stores = state.stores.filter(store => store.store_id !== payload);
        },
        setDepartments: (state, { payload } : PayloadAction<Department[]>) => {
            state.departments = payload;
        },
        addDepartment: (state, { payload } : PayloadAction<Department>) => {
            state.departments.push(payload);
        },
        updateDepartment: (state, { payload } : PayloadAction<Department>) => {
            const index = state.departments.findIndex(department => department.department_id === payload.department_id);
            state.departments[index] = payload;
        },
        deleteDepartment: (state, { payload } : PayloadAction<number>) => {
            state.departments = state.departments.filter(department => department.department_id !== payload);
        },
        setCategories: (state, { payload } : PayloadAction<Category[]>) => {
            state.categories = payload;
        },
        addCategory: (state, { payload } : PayloadAction<Category>) => {
            state.categories.push(payload);
        },
        updateCategory: (state, { payload } : PayloadAction<Category>) => {
            const index = state.categories.findIndex(category => category.category_id === payload.category_id);
            state.categories[index] = payload;
        },
        deleteCategory: (state, { payload } : PayloadAction<number>) => {
            state.categories = state.categories.filter(category => category.category_id !== payload);
        },
        setProducts: (state, { payload } : PayloadAction<Product[]>) => {
            state.products = payload;
        },
        addProduct: (state, { payload } : PayloadAction<Product>) => {
            state.products.push(payload);
        },
        updateProduct: (state, { payload } : PayloadAction<Product>) => {
            const index = state.products.findIndex(product => product.product_id === payload.product_id);
            state.products[index] = payload;
        },
        deleteProduct: (state, { payload } : PayloadAction<number>) => {
            state.products = state.products.filter(product => product.product_id !== payload);
        }
    }
});

export const {
    // * Store Methods
    setStores,
    addStore,
    updateStore,
    deleteStore,

    // * Department Methods
    setDepartments,
    addDepartment,
    updateDepartment,
    deleteDepartment,

    // * Category Methods
    setCategories,
    addCategory,
    updateCategory,
    deleteCategory,

    // * Product Methods
    setProducts,
    addProduct,
    updateProduct,
    deleteProduct
} = infoSlice.actions;