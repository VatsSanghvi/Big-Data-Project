import { initialAuthValues } from '@constants';
import { LoginState, User } from '@models';
import { createSlice, PayloadAction } from '@reduxjs/toolkit';

export interface AuthState {
    authState: LoginState;
    user: User;
}

const initialState : AuthState = initialAuthValues;

export const authSlice = createSlice({
    name: 'auth',
    initialState,
    reducers: {
        setAuthState: (state, { payload } : PayloadAction<LoginState>) => {
            state.authState = payload;
        },
        setUser: (state, { payload } : PayloadAction<User>) => {
            state.user = payload;
        }
    }
});

export const { setAuthState, setUser } = authSlice.actions;