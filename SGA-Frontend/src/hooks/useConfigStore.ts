// Local Libraries
import { setIsLoading } from '@store';

// Hooks
import { useAppDispatch, useAppSelector } from './useStore'


export const useConfigStore = () => {
    const { isLoading } = useAppSelector(state => state.config);
    const dispatch = useAppDispatch();

    const updateLoading = (loading: boolean) => {
        dispatch(setIsLoading(loading))
    };
    
    return {
        // Properties
        isLoading,
        
        // Methods
        updateLoading
    };
}