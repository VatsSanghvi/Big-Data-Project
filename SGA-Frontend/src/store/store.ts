// * React Libraries
import { configureStore } from "@reduxjs/toolkit";

// * Slices
import { authSlice, configSlice, infoSlice, userSlice } from "./slices";

export const store = configureStore({
  reducer: {
    auth: authSlice.reducer,
    config: configSlice.reducer,
    info: infoSlice.reducer,
    user: userSlice.reducer,
  },
});

export type RootState = ReturnType<typeof store.getState>;

export type AppDispatch = typeof store.dispatch;
