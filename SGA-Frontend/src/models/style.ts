// * React Libraries
import { CSSProperties } from "react";

export interface ComponentStyle {
    className?: string;
    style?: CSSProperties;
}

export interface WrapperStyle {
    wrapperClassName?: string;
    wrapperStyle?: CSSProperties;
}

export type Style<T> = ComponentStyle & WrapperStyle & T;