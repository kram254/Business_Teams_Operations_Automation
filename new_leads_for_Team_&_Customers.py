import smtplib
from socket import gaierror

def send_email(subject, message, recipients):
    """
    Sends an email to the specified recipients.

    Args:
    subject (str): The subject of the email.
    message (str): The body of the email.
    recipients (list): A list of email addresses to send the email to.
    """
    # SMTP server configuration
    smtp_server = "smtp.example.com"
    smtp_port = 587
    smtp_username = "your_email@example.com"
    smtp_password = "your_password"

    # Email configuration
    sender = "markorlando45@gmail.com"

    # Create the email message
    email_message = f"Subject: {subject}\n\n{message}"

    try:
        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)

        # Send the email
        server.sendmail(sender, recipients, email_message)

        print("Email sent successfully!")

    except gaierror as e:
        print("Failed to connect to the SMTP server. Please check the server address and port.")
        print(f"Error details: {e}")

    except smtplib.SMTPAuthenticationError as e:
        print("SMTP authentication failed. Please check the username and password.")
        print(f"Error details: {e}")

    except Exception as e:
        print("An error occurred while sending the email.")
        print(f"Error details: {e}")

    finally:
        # Disconnect from the SMTP server
        server.quit()

# Example usage
subject = "New lead or customer"
message = "A new lead or customer has been added to the system."
recipients = ["e.ndaliro69@gmail.com", "team_member2@example.com"]
send_email(subject, message, recipients)
