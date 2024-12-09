// * React Libraries
import { createSlice, PayloadAction } from "@reduxjs/toolkit";

// * Models
import { GroceryList, Product } from "@models";

interface UserState {
  groceryList: GroceryList[];
}

const initialState: UserState = {
  groceryList: [],
};

export const userSlice = createSlice({
  name: "user",
  initialState,
  reducers: {
    createGroceryList: (state, { payload }: PayloadAction<GroceryList>) => {
      state.groceryList.push(payload);
    },
    addItem: (state, { payload }: PayloadAction<Product>) => {
      state.products.push(payload);
    },
  },
});

export const { createGroceryList, addItem } = userSlice.actions;
