import unittest
from unittest.mock import patch
from app import security_benchmark

class TestSecurityBenchmark(unittest.TestCase):
    @patch('app.security_benchmark.subprocess.Popen')
    def test_run_cis_benchmark(self, mock_popen):
        mock_popen_instance = mock_popen.return_value
        mock_popen_instance.communicate.return_value = ('{"cis_results": "cis_data"}', '')
        mock_popen_instance.returncode = 0

        cis_results = security_benchmark.run_cis_benchmark()

        self.assertIsNotNone(cis_results)
        self.assertEqual(cis_results["cis_results"], "cis_data")

if __name__ == '__main__':
    unittest.main()
