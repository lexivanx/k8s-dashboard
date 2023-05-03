import unittest
from app import compliance_reporting

class TestComplianceReporting(unittest.TestCase):
    def test_generate_report(self):
        cis_results = "CIS Results"
        psp_violations = "PSP Violations"
        network_policies = "Network Policies"
        image_scan_results = "Image Scan Results"
        runtime_security_events = "Runtime Security Events"

        report = compliance_reporting.generate_report(cis_results, psp_violations, network_policies, image_scan_results, runtime_security_events)
        self.assertIn(cis_results, report)
        self.assertIn(psp_violations, report)
        self.assertIn(network_policies, report)
        self.assertIn(image_scan_results, report)
        self.assertIn(runtime_security_events, report)

if __name__ == '__main__':
    unittest.main()
