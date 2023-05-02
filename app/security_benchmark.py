import json
import subprocess

def run_cis_benchmark():
    cmd = "kube-bench --json"
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        raise Exception(f"kube-bench failed: {stderr.decode('utf-8')}")
    
    cis_results = json.loads(stdout)
    return cis_results
