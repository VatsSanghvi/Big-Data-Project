// * React Libraries
import { Topbar } from "@components"
import { useBreakpoints } from "@hooks";
import { Outlet } from "react-router-dom"

export const GeneralLayout = () => {
    
    const { isMobile } = useBreakpoints();

    return (
        <div className="general-layout">
            <Topbar />
            <div className="general-layout-area">
                {
                    !isMobile && (
                        <div className="general-layout-menu">
                            
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