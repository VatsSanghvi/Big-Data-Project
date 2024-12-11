// * Third Party Libraries
import { object, string } from "yup";

// * Models
import { BudgetRequest } from "@models";

export const budgetInitialValues: BudgetRequest = {
  amount: 0,
  total_spent: 0,
  user_id: 0,
};

export const budgetValidationSchema = object({
  amount: string().required("Amount is required"),
  user_id: string().required("User ID is required"),
});
