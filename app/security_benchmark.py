import json
import subprocess
import logging
from flask_caching import Cache

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

cache = Cache(config={'CACHE_TYPE': 'simple'})

def init_app(app):
    cache.init_app(app)

@cache.cached(timeout=300)
def run_cis_benchmark():
    cmd = "kube-bench --json"
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        logger.error(f"kube-bench failed: {stderr.decode('utf-8')}")
        return None

    cis_results = json.loads(stdout)
    logger.info("CIS benchmark check completed successfully")
    return cis_results
