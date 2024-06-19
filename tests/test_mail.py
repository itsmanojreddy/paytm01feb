import pytest
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(subject, message, sender_email, receiver_email, smtp_server, smtp_port, smtp_username, smtp_password):
    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Add message body
    msg.attach(MIMEText(message, 'plain'))

    # Connect to SMTP server and send email
    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
@pytest.mark.test12345
def test_send_email():
    # Test parameters
    subject = "Test Email from pytest"
    message = "This is a test email sent from a pytest script."
    sender_email = "itsmanojreddyy@outlook.com"
    receiver_email = "pmanoj.ece94@gmail.com"
    smtp_server = "smtp.office365.com"
    smtp_port = 465
    smtp_username = "itsmanojreddyy@outlook.com"
    smtp_password = "Manoj@123"

    # Send email
    send_email(subject, message, sender_email, receiver_email, smtp_server, smtp_port, smtp_username, smtp_password)

    # Assert that the email was sent successfully
    assert True

if __name__ == "__main__":
    pytest.main([__file__, "-v"])