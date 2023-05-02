import json
import subprocess

def check_psp_violations():
    cmd = "kube-psp-advisor --namespace=default --output=json"
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        raise Exception(f"kube-psp-advisor failed: {stderr.decode('utf-8')}")
    
    psp_violations = json.loads(stdout)
    return psp_violations
