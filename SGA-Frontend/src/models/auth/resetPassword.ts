export interface ResetPasswordRequest {
  email: string;
  current_password: string;
  new_password: string;
}
