const endpointModules = {
  user: "users",
  store: "store",
  department: "department",
  budget: "budget",
};

export const endpoints = {
  auth: {
    login: `${endpointModules.user}/login`,
    register: `${endpointModules.user}/register`,
    sendEmail: `${endpointModules.user}/send-email`,
    resetPassword: `${endpointModules.user}/reset-password`,
    updateProfile: `${endpointModules.user}/profile`,
  },
  store: {
    get: `${endpointModules.store}`,
    create: `${endpointModules.store}`,
    update: `${endpointModules.store}`,
    delete: `${endpointModules.store}`,
  },
  department: {
    get: `${endpointModules.department}`,
    create: `${endpointModules.department}`,
    update: `${endpointModules.department}`,
    delete: `${endpointModules.department}`,
  },
  budget: {
    get: `${endpointModules.budget}`,
    create: `${endpointModules.budget}`,
    update: `${endpointModules.budget}`,
    reset: `${endpointModules.budget}/reset`,
  },
};
