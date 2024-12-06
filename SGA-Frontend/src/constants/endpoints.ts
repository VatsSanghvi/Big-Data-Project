const endpointModules = {
    user: 'users',
    store: 'store'
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
    }
}