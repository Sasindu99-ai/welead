from os import environ

from django.core.mail import EmailMultiAlternatives
from icecream import ic

__all__ = ["EmailService"]


class EmailService:
    @classmethod
    async def sendEmailOTP(cls, email: str, otp: str):
        ic("Sending OTP Email")
        subject = f"VIP Travels - OTP Verification: {otp}"
        from_email = environ.get("EMAIL_HOST_USER")
        to = [email]
        text_content = (
            f"Your OTP is: {otp}.\n\nPlease do not share this OTP with anyone!"
        )
        html_content = f"""
		<!DOCTYPE html>
		<html lang="en">
		<head>
			<meta charset="UTF-8">
			<meta http-equiv="X-UA-Compatible" content="IE=edge">
			<meta name="viewport" content="width=device-width, initial-scale=1.0">
			<title>VIP Travels - OTP Verification</title>
		</head>
		<body>
			<h1>VIP Travels - OTP Verification</h1>
			<p>Your OTP is: <strong>{otp}</strong>.</p>
			<p>Please do not share this OTP with anyone!</p>
		</body>
		</html>
		"""

        msg = EmailMultiAlternatives(subject, text_content, from_email, to)
        msg.attach_alternative(html_content, "text/html")
        msg.send()

    @classmethod
    def sendEmailOTPDefault(cls, email: str, otp: str):
        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText

        # Email configuration
        SMTP_SERVER = "smtp.gmail.com"
        SMTP_PORT = 587
        EMAIL_ADDRESS = environ.get("EMAIL_HOST_USER", "")
        EMAIL_PASSWORD = environ.get("EMAIL_HOST_PASSWORD", "")

        subject = f"VIP Travels - OTP Verification: {otp}"
        html_content = f"""
		<!DOCTYPE html>
		<html lang="en">
		<head>
			<meta charset="UTF-8">
			<meta http-equiv="X-UA-Compatible" content="IE=edge">
			<meta name="viewport" content="width=device-width, initial-scale=1.0">
			<title>VIP Travels - OTP Verification</title>
		</head>
		<body>
			<h1>VIP Travels - OTP Verification</h1>
			<p>Your OTP is: <strong>{otp}</strong>.</p>
			<p>Please do not share this OTP with anyone!</p>
		</body>
		</html>
		"""

        try:
            msg = MIMEMultipart()
            msg["From"] = EMAIL_ADDRESS
            msg["To"] = email
            msg["Subject"] = subject
            msg.attach(MIMEText(html_content, "html"))
            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
            server.quit()
        except Exception as e:
            print(e)
