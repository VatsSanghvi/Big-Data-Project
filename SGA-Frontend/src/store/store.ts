import { configureStore } from "@reduxjs/toolkit";
import { authSlice, configSlice } from "./slices";


export const store = configureStore({
    reducer: {
        auth: authSlice.reducer,
        config: configSlice.reducer
    }
});

export type RootState = ReturnType<typeof store.getState>;

export type AppDispatch = typeof store.dispatch;