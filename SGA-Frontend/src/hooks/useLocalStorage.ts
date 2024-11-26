import { AuthState } from "@store";
import { useState } from "react";

export const useLocalStorage = ( key : string, defaultValue : unknown ) => {

    const [value, setValue] = useState(() => {
        try {
            const item = window.localStorage.getItem(key);
            if (item) {
                return JSON.parse(item);
            } else {
                window.localStorage.setItem(key, JSON.stringify(defaultValue));
                return defaultValue;
            }
        } catch {
            return defaultValue;
        }
    });

    const updateValue = (newValue: AuthState) => {
        const newValueToStore = {
            ...value,
            ...newValue
        }

        try {

            window.localStorage.setItem(key, JSON.stringify(newValueToStore));
        } catch (error) {
            console.log(error);
        }

        setValue(newValueToStore);
    }

    return {
        value,
        updateValue
    }
}