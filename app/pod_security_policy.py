import json
import subprocess
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def check_psp_violations():
    cmd = "kube-psp-advisor --namespace=default --output=json"
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        logger.error(f"kube-psp-advisor failed: {stderr.decode('utf-8')}")
        return None
    
    psp_violations = json.loads(stdout)
    logger.info("Checked PSP violations successfully")
    return psp_violations
