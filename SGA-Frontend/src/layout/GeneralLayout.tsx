// * React Libraries
import { Topbar } from "@components"
import { menuOptions } from "@constants";
import { useAuthStore, useBreakpoints, useInfoStore } from "@hooks";
import { LoginState } from "@models";
import { Menu } from "primereact/menu";
import { MenuItem } from "primereact/menuitem";
import { useEffect, useMemo } from "react";
import { Outlet, useNavigate } from "react-router-dom"

export const GeneralLayout = () => {
    
    const { isMobile } = useBreakpoints();

    const { user, authState } = useAuthStore();
    const { getInfo } = useInfoStore();
    const navigate = useNavigate();

    const menuItems : MenuItem[] = useMemo(() => {
        const items = user.role ? menuOptions.filter(option => option.roles.includes(user.role)) : [];

        return items.map(item => {
            return {
                label: item.label,
                icon: `pi pi-${item.icon}`,
                command: () => navigate(item.to)
            }
        });
    }, [user.role]);

    useEffect(() => {
        if (authState === LoginState.Authenticated && user.user_id) {
            getInfo(user);
        }
    }, [authState]);

    return (
        <div className="general-layout">
            <Topbar />
            <div className="general-layout-area">
                {
                    !isMobile && (
                        <div className="general-layout-menu">
                            <Menu 
                                model={menuItems} 
                                className="menu-container"
                            />
                        </div>
                    )
                }
                <div className="general-layout-outlet">
                    <div className="general-layout-outlet-card">
                        <Outlet />
                    </div>
                </div>
            </div>
        </div>
    )
}