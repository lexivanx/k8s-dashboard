import unittest
from app import kubernetes_api

class TestKubernetesAPI(unittest.TestCase):

    def test_get_cluster_info(self):
        cluster_info = kubernetes_api.get_cluster_info()
        self.assertIsNotNone(cluster_info)
        self.assertTrue('cluster_name' in cluster_info)
        self.assertTrue('nodes' in cluster_info)
        self.assertTrue('namespaces' in cluster_info)

if __name__ == '__main__':
    unittest.main()
