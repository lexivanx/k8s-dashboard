import unittest
from unittest.mock import patch
from app import network_policy

class MockedMetadata:
    def __init__(self, _continue):
        self._continue = _continue

class MockedNetworkPolicyList:
    def __init__(self, metadata, items):
        self.metadata = metadata
        self.items = items

class TestNetworkPolicy(unittest.TestCase):
    @patch('app.network_policy.config.load_kube_config')
    @patch('app.network_policy.client.NetworkingV1Api')
    def test_get_network_policies(self, mock_networking_v1_api, mock_load_kube_config):
        mock_api_instance = mock_networking_v1_api.return_value
        mock_api_instance.list_network_policy_for_all_namespaces.return_value = MockedNetworkPolicyList(metadata=MockedMetadata(_continue=None), items=['policy1', 'policy2'])

        all_network_policies = network_policy.get_network_policies()

        self.assertEqual(len(all_network_policies), 2)
        self.assertIn('policy1', all_network_policies)
        self.assertIn('policy2', all_network_policies)

if __name__ == '__main__':
    unittest.main()
