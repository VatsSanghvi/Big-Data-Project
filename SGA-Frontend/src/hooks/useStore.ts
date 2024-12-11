// React Libraries
import { TypedUseSelectorHook, useDispatch, useSelector } from "react-redux";

// Local Libraries
import { AppDispatch, RootState } from "@store";

export const useAppDispatch: () => AppDispatch = useDispatch;
export const useAppSelector: TypedUseSelectorHook<RootState> = useSelector;