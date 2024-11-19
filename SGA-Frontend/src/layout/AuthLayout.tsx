// * React Libraries
import { Outlet } from "react-router-dom"

export const AuthLayout = () => {
    return (
        <div className="auth-layout">
            <div className="auth-layout-card">
                <Outlet />
            </div>
        </div>
    )
}