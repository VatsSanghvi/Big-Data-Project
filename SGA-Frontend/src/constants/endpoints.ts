const endpointModules = {
  user: "users",
  store: "store",
  department: "department",
  budget: "budget",
  category: "category",
  products: "products",
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
    get: `${endpointModules.department}/owner`,
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
  category: {
    get: `${endpointModules.category}/owner`,
    create: `${endpointModules.category}`,
    update: `${endpointModules.category}`,
    delete: `${endpointModules.category}`,
  },
  product: {
    get: `${endpointModules.products}/owner`,
    create: `${endpointModules.products}`,
    update: `${endpointModules.products}`,
    delete: `${endpointModules.products}`,
  }
};
