import smtplib
import yaml
from email.mime.text import MIMEText
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

def load_config():
    with open("config/default.yaml", "r") as f:
        return yaml.safe_load(f)

def send_email(subject, body):
    config = load_config()
    email_config = config["email"]

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = email_config["sender"]
    msg["To"] = ", ".join(email_config["recipients"])

    try:
        server = smtplib.SMTP(email_config["smtp_server"], email_config["smtp_port"])
        server.ehlo()
        server.starttls()
        server.login(email_config["username"], email_config["password"])
        server.sendmail(email_config["sender"], email_config["recipients"], msg.as_string())
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")

def send_slack_message(text):
    config = load_config()
    slack_config = config["slack"]

    client = WebClient(token=slack_config["bot_token"])

    try:
        response = client.chat_postMessage(
            channel=slack_config["channel"],
            text=text
        )
        print("Slack message sent successfully")
    except SlackApiError as e:
        print(f"Failed to send Slack message: {e}")

def send_alerts(compliance_report):
    summary = compliance_report["summary"]
    details = compliance_report["details"]

    email_subject = "Compliance Alert"
    email_body = f"Compliance alert:\n\n{summary}\n\nDetails:\n{details}"
    send_email(email_subject, email_body)

    slack_message = f"Compliance alert:\n\n{summary}"
    send_slack_message(slack_message)
