// Local Libraries
import { LoginState, User } from '@models';
import { setAuthState, setUser } from '@store';

// Local Hooks
import { useAppDispatch, useAppSelector } from './useStore'
import { useLocalStorage } from './useLocalStorage';
import { initialAuthValues } from '@constants';
import { useEffect } from 'react';


export const useAuthStore = () => {
    const { authState, user } = useAppSelector(state => state.auth);
    const dispatch = useAppDispatch();

    const { value, updateValue } = useLocalStorage('auth', initialAuthValues);

    
    const updateAuthState = (newState: LoginState) => dispatch(setAuthState(newState));
    const updateUser = (newUser: User) => {
        dispatch(setUser(newUser));
    };

    const onLogin = (newUser: User) => {
        updateAuthState(LoginState.Authenticated);
        updateUser(newUser);        
        updateValue({
            authState: LoginState.Authenticated,
            user: newUser
        });
    };

    const onLogout = () => {
        updateAuthState(LoginState.UnAuthenticated);
        updateUser(initialAuthValues.user);
        updateValue(initialAuthValues);
    };

    useEffect(() => {
        updateAuthState(value.authState);
        updateUser(value.user);
    }, []);

    return {
        // Properties
        authState,
        user,
        
        // Methods
        updateAuthState,
        updateUser,
        onLogin,
        onLogout
        
    };
}