import unittest
from app import kubernetes_api

class TestKubernetesAPI(unittest.TestCase):
    def test_get_cluster_info(self):
        cluster_info = kubernetes_api.get_cluster_info()
        self.assertIsNotNone(cluster_info)
        self.assertIsInstance(cluster_info, dict)

if __name__ == '__main__':
    unittest.main()
