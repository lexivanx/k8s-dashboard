import unittest
from unittest.mock import patch
from app import alerting

class TestAlerting(unittest.TestCase):
    @patch('app.alerting.send_email')
    @patch('app.alerting.send_slack_message')
    def test_send_alerts(self, mock_send_slack_message, mock_send_email):
        compliance_report = {
            "summary": "Test summary",
            "details": "Test details"
        }
        alerting.send_alerts(compliance_report)
        mock_send_email.assert_called_once_with("Compliance Alert", "Compliance alert:\n\nTest summary\n\nDetails:\nTest details")
        mock_send_slack_message.assert_called_once_with("Compliance alert:\n\nTest summary")

if __name__ == '__main__':
    unittest.main()
