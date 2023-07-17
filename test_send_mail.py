import pytest
from unittest.mock import patch
from smtplib import SMTPAuthenticationError
from new_leads_for_Team_&_Customers import send_email

@pytest.fixture
def mock_smtp_server():
    with patch("smtplib.SMTP") as mock_smtp:
        yield mock_smtp.return_value

def test_send_email(mock_smtp_server):
    subject = "Test Subject"
    message = "Test Message"
    recipients = ["recipient1@example.com", "recipient2@example.com"]

    send_email(subject, message, recipients)

    # Check if SMTP server is called with the correct arguments
    mock_smtp_server.assert_called_once_with("smtp.example.com", 587)
    mock_smtp_server.return_value.starttls.assert_called_once()
    mock_smtp_server.return_value.login.assert_called_once_with("your_email@example.com", "your_password")
    mock_smtp_server.return_value.sendmail.assert_called_once_with("markorlando45@gmail.com", recipients, f"Subject: {subject}\n\n{message}")
    mock_smtp_server.return_value.quit.assert_called_once()

def test_send_email_authentication_error(mock_smtp_server):
    # Raise an SMTPAuthenticationError to simulate authentication failure
    mock_smtp_server.return_value.login.side_effect = SMTPAuthenticationError(535, "Authentication failed")

    subject = "Test Subject"
    message = "Test Message"
    recipients = ["recipient1@example.com", "recipient2@example.com"]

    with pytest.raises(SMTPAuthenticationError):
        send_email(subject, message, recipients)

    mock_smtp_server.return_value.quit.assert_called_once()
