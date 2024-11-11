// Local Libraries
import { LoginState, Role } from '@models';
import { setAuthState, setRole } from '@store';

// Local Hooks
import { useAppDispatch, useAppSelector } from './useStore'


export const useAuthStore = () => {
    const { authState, role } = useAppSelector(state => state.auth);
    const dispatch = useAppDispatch();
    
    const updateAuthState = (newState: LoginState) => dispatch(setAuthState(newState));
    const updateRole = (newRole: Role) => dispatch(setRole(newRole));

    return {
        // Properties
        authState,
        role,
        
        // Methods
        updateAuthState,
        updateRole
        
    };
}