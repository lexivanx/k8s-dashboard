def generate_report(cis_results, psp_violations, network_policies, image_scan_results, runtime_security_events):
    # Combine the input data into a compliance report dictionary
    compliance_report = {
        'summary': 'Compliance summary based on the input data...',
        'details': {
            'cis_results': cis_results,
            'psp_violations': psp_violations,
            'network_policies': network_policies,
            'image_scan_results': image_scan_results,
            'runtime_security_events': runtime_security_events
        }
    }
    return compliance_report
