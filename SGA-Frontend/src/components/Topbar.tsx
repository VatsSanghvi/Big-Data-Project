// * React Libraries
import { useState } from 'react';

// * Third Party Libraries
import { Button } from 'primereact/button';
import { Image } from 'primereact/image';
import { Sidebar } from 'primereact/sidebar';

// * Hooks
import { useAuthStore, useBreakpoints } from '@hooks';

// * Constants
import { menuOptions } from '@constants';

// * Components
import { MenuItem } from './MenuItem';

// * Assets
import Logo from '@assets/virtual-assistant.png';

// * Topbar of the application
export const Topbar = () => {
    const { isMobile } = useBreakpoints();
    const { onLogout, user } = useAuthStore();

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
                <h1>Smart Grocery Assistant</h1>
            </div>
            <Button
                label={isMobile ? '' : 'Sign Out'}
                icon='pi pi-sign-out'
                className='sign-out-button'
                onClick={onLogout}
            />
            <Sidebar visible={visible} onHide={() => setVisible(false)}>
                <h2>Menu</h2>
                {
                    menuOptions
                        .filter(option => option.roles.includes(user.role))
                        .map(item => (
                            <MenuItem 
                                {...item}
                                close={() => setVisible(false)}
                                key={item.to}
                            />
                        ))
                }
            </Sidebar>
        </div>
    )
}