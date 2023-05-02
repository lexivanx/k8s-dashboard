import json
import subprocess

def scan_images():
    # Replace this with actual image names and tags
    images = ["your-image-name:your-image-tag"]

    image_scan_results = []

    for image in images:
        cmd = f"trivy image --format json {image}"
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        if process.returncode != 0:
            raise Exception(f"Trivy scan failed: {stderr.decode('utf-8')}")
        
        result = json.loads(stdout)
        image_scan_results.append(result)

    return image_scan_results
