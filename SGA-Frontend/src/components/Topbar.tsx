import Logo from '@assets/virtual-assistant.png';
import { useAuthStore, useBreakpoints } from '@hooks';
import { Button } from 'primereact/button';
import { Image } from 'primereact/image';
import { Sidebar } from 'primereact/sidebar';
import { useState } from 'react';

export const Topbar = () => {
    const { isMobile } = useBreakpoints();
    const { onLogout } = useAuthStore();

    const [visible, setVisible] = useState<boolean>(false);

    return (
        <div className="topbar">
            <div className="left-side">
                {
                    isMobile 
                    ? (
                        <Button 
                            link
                            icon="pi pi-bars"
                            className='menu-button'
                            onClick={() => setVisible(true)}
                        />
                    )
                    : (
                        <Image src={Logo} alt="Logo" width='50'/>
                    )
                }
                <h1>Smart Grocery Assitant</h1>
            </div>
            <Button
                label={isMobile ? '' : 'Sign Out'}
                icon='pi pi-sign-out'
                className='sign-out-button'
                onClick={onLogout}
            />
            <Sidebar visible={visible} onHide={() => setVisible(false)}>
                <h2>Sidebar</h2>
                {/* <p>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
                    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
                </p> */}
            </Sidebar>
        </div>
    )
}