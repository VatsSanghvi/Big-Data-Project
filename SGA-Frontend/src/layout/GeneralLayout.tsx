// * React Libraries
import { Topbar } from "@components"
import { menuOptions } from "@constants";
import { useAuthStore, useBreakpoints } from "@hooks";
import { Menu } from "primereact/menu";
import { MenuItem } from "primereact/menuitem";
import { useMemo } from "react";
import { Outlet, useNavigate } from "react-router-dom"

export const GeneralLayout = () => {
    
    const { isMobile } = useBreakpoints();

    const { user } = useAuthStore();
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
                    <Outlet />
                </div>
            </div>
        </div>
    )
}