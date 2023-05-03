import json
import subprocess
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def read_images_from_file(filename):
    with open(filename, "r") as file:
        images = [line.strip() for line in file.readlines()]
    return images

def scan_images():
    images = read_images_from_file("images.txt")
    if not images:
        logger.error("No images found to scan.")
        return []

    image_scan_results = []

    for image in images:
        cmd = f"trivy image --format json {image}"
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        
        if process.returncode != 0:
            logger.error(f"Trivy scan failed for image {image}: {stderr.decode('utf-8')}")
            continue
        
        result = json.loads(stdout)
        image_scan_results.append(result)

    logger.info(f"{len(image_scan_results)} image(s) scanned successfully")
    return image_scan_results
