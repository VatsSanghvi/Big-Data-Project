import { LoginState, Role } from '@models';
import { createSlice, PayloadAction } from '@reduxjs/toolkit';

interface AuthState {
   authState: LoginState;
   role: Role;
}

const initialState : AuthState = {
   authState: LoginState.UnAuthenticated,
   role: Role.User
};

export const authSlice = createSlice({
   name: 'auth',
   initialState,
   reducers: {
       setAuthState: (state, { payload } : PayloadAction<LoginState>) => {
           state.authState = payload;
       },
       setRole: (state, { payload } : PayloadAction<Role>) => {
           state.role = payload;
       }
   }
});

export const { setAuthState, setRole } = authSlice.actions;