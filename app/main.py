import logging
from flask import Flask, render_template
from app import kubernetes_api, security_benchmark, pod_security_policy, network_policy, container_scanning, runtime_security, compliance_reporting, alerting

app = Flask(__name__)

@app.route("/")
def dashboard():
    cluster_info = kubernetes_api.get_cluster_info()
    cis_results = security_benchmark.run_cis_benchmark()
    psp_violations = pod_security_policy.check_psp_violations()
    network_policies = network_policy.get_network_policies()
    image_scan_results = container_scanning.scan_images()
    runtime_security_events = runtime_security.monitor_runtime_security()

    compliance_report = compliance_reporting.generate_report(cis_results, psp_violations, network_policies, image_scan_results, runtime_security_events)

    alerting.send_alerts(compliance_report)

    return render_template("dashboard.html", cluster_info=cluster_info, compliance_report=compliance_report)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app.run(debug=True)
