// * React Libraries
import { createSlice, PayloadAction } from '@reduxjs/toolkit';

// * Models
import { Department, Store } from '@models';

interface InfoState {
    stores: Store[];
    departments: Department[];
}

const initialState : InfoState = {
    stores: [],
    departments: []
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
        }
    }
});

export const { setStores, addStore, updateStore, deleteStore, setDepartments, addDepartment, updateDepartment, deleteDepartment } = infoSlice.actions;