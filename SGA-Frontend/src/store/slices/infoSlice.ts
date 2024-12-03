// * React Libraries
import { createSlice, PayloadAction } from '@reduxjs/toolkit';

// * Models
import { Store } from '@models';

interface InfoState {
   stores: Store[];
}

const initialState : InfoState = {
   stores: []
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
        }
    }
});

export const { setStores, addStore, updateStore, deleteStore } = infoSlice.actions;