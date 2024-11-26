const endpointModules = {
    user: 'users'
}

export const endpoints = {
    auth: {
        login: `${endpointModules.user}/login`,
        register: `${endpointModules.user}/register`,
    }
}