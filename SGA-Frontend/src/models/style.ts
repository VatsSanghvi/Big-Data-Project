// * React Libraries
import { CSSProperties } from "react";
import { Breakpoints } from "./breakpoints";

export interface ComponentStyle {
    className?: string;
    style?: CSSProperties;
}

export interface WrapperStyle {
    wrapperClassName?: string;
    wrapperStyle?: CSSProperties;
}

export type Style<T> = ComponentStyle & WrapperStyle & T;

export type BreakpointComponentStyle = Breakpoints<ComponentStyle>;

export type BreakpointWrapperStyle = Breakpoints<WrapperStyle>;

export type BreakpointStyle<T> = Breakpoints<Style<T>>;