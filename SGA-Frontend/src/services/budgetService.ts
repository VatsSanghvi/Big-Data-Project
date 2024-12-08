// * Models
import { BudgetRequest } from "@models";

// * Constants
import { endpoints } from "@constants";

// * Services
import { instance } from "./axiosService";

export const budget = {
  get: (budget_id: number) => {
    return instance.get(`${endpoints.budget.get}/${budget_id}`);
  },
  create: (budget: BudgetRequest) => {
    return instance.post(endpoints.budget.create, budget);
  },
  update: (budget: BudgetRequest) => {
    return instance.put(endpoints.budget.update, budget);
  },
  reset: (budget_id: number) => {
    return instance.delete(`${endpoints.budget.reset}/${budget_id}`);
  },
};
