from kubernetes import client, config

def get_network_policies():
    config.load_kube_config()
    api_instance = client.NetworkingV1Api()

    network_policies = api_instance.list_network_policy_for_all_namespaces()
    return network_policies
