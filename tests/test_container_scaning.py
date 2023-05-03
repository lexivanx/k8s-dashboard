import unittest
from unittest.mock import patch
from app import container_scanning

class TestContainerScanning(unittest.TestCase):
    @patch('app.container_scanning.read_images_from_file')
    @patch('app.container_scanning.subprocess.Popen')
    def test_scan_images(self, mock_popen, mock_read_images_from_file):
        mock_read_images_from_file.return_value = ['image1', 'image2']
        mock_popen_instance = mock_popen.return_value
        mock_popen_instance.communicate.return_value = ('{"image": "image1"}', '')
        mock_popen_instance.returncode = 0
        
        scan_results = container_scanning.scan_images()

        self.assertEqual(len(scan_results), 2)
        self.assertIn('image1', [result['image'] for result in scan_results])

if __name__ == '__main__':
    unittest.main()
