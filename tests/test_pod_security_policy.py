import unittest
from unittest.mock import patch
from app import pod_security_policy

class TestPodSecurityPolicy(unittest.TestCase):
    @patch('app.pod_security_policy.subprocess.Popen')
    def test_check_psp_violations(self, mock_popen):
        mock_popen_instance = mock_popen.return_value
        mock_popen_instance.communicate.return_value = ('{"psp_violations": "violations_data"}', '')
        mock_popen_instance.returncode = 0

        psp_violations = pod_security_policy.check_psp_violations()

        self.assertIsNotNone(psp_violations)
        self.assertEqual(psp_violations["psp_violations"], "violations_data")

if __name__ == '__main__':
    unittest.main()
