const endpointModules = {
    user: 'users',
    store: 'store',
    department: 'department'
}

export const endpoints = {
    auth: {
        login: `${endpointModules.user}/login`,
        register: `${endpointModules.user}/register`,
    },
    store: {
        get: `${endpointModules.store}`,
        create: `${endpointModules.store}`,
        update: `${endpointModules.store}`,
        delete: `${endpointModules.store}`
    },
    department: {
        get: `${endpointModules.department}`,
        create: `${endpointModules.department}`,
        update: `${endpointModules.department}`,
        delete: `${endpointModules.department}`
    }
}