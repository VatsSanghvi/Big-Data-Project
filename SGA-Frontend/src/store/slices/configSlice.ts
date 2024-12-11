

import { PayloadAction, createSlice } from '@reduxjs/toolkit';

interface ConfigState {
    isLoading: boolean;
}

const initialState : ConfigState = {
    isLoading: false,
};

export const configSlice = createSlice({
    name: 'config',
    initialState: initialState,
    reducers: {
        setIsLoading: (state, { payload } : PayloadAction<boolean>) => {
            state.isLoading = payload;
        }
    }
});
export const { setIsLoading } = configSlice.actions;