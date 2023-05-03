from jinja2 import Environment, FileSystemLoader

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

    # Set up Jinja2 environment and load the template
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('compliance_report.txt')

    # Render the template with the compliance report data
    rendered_report = template.render(
        summary=compliance_report['summary'],
        details=compliance_report['details']
    )

    return rendered_report
