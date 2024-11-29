#from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from app.settings import Settings

# mail_config = ConnectionConfig(
#    MAIL_USERNAME=Settings.mail_username,
#    MAIL_PASSWORD=Settings.mail_password,
#    MAIL_FROM=Settings.mail_from,
#    MAIL_PORT=Settings.mail_port,
#    MAIL_SERVER=Settings.mail_server,
#    MAIL_SSL_TLS=True
#)

# fastmail = FastMail(mail_config)

# async def send_password_reset_email(email: str):
#     reset_url = f"{Settings.frontend_url}/reset-password"
#
#     message = MessageSchema(
#         subject="Password Reset Request",
#         recipients=[email],
#         body=f"""
#         You have requested to reset your password.
#         Please click the following link to reset your password:
#         {reset_url}
#
#         If you did not request this, please ignore this email.
#         The link will expire in 1 hour.
#         """
#     )
#
#     await fastmail.send_message(message)