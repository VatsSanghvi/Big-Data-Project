// * React Libraries
import { createSlice, PayloadAction } from "@reduxjs/toolkit";

// * Models
import { GroceryList, GroceryListItem } from "@models";

interface UserState {
    groceryList?: GroceryList;
    groceryListItems: GroceryListItem[];
}

const initialState: UserState = {
    groceryList: undefined,
    groceryListItems: [],
};

export const userSlice = createSlice({
    name: "user",
    initialState,
    reducers: {
        setGroceryList: (state, { payload }: PayloadAction<GroceryList | undefined>) => {
            state.groceryList = payload;
        },
        deleteGroceryList: (state) => {
            state.groceryList = undefined;
        },
        setGroceryListItems: (state, { payload }: PayloadAction<GroceryListItem[]>) => {
            state.groceryListItems = payload;
        },
        addGroceryListItem: (state, { payload }: PayloadAction<GroceryListItem>) => {
            state.groceryListItems.push(payload);
        },
        removeGroceryListItem: (state, { payload }: PayloadAction<number>) => {
            state.groceryListItems = state.groceryListItems.filter((item) => item.id !== payload);
        },
        updateGroceryListItem: (state, { payload }: PayloadAction<GroceryListItem>) => {
            const index = state.groceryListItems.findIndex((item) => item.id === payload.id);
            state.groceryListItems[index] = payload;
        },
        deleteGroceryListItems: (state) => {
            state.groceryListItems = [];
        }
    },
});

export const { setGroceryList, setGroceryListItems, addGroceryListItem, removeGroceryListItem, deleteGroceryList, updateGroceryListItem, deleteGroceryListItems } = userSlice.actions;
