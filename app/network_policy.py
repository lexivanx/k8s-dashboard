from kubernetes import client, config

def get_network_policies(chunk_size=50):
    config.load_kube_config()
    api_instance = client.NetworkingV1Api()

    continue_token = None
    all_network_policies = []

    while True:
        network_policies = api_instance.list_network_policy_for_all_namespaces(limit=chunk_size, _continue=continue_token)
        all_network_policies.extend(network_policies.items)

        if not network_policies.metadata._continue:
            break

        continue_token = network_policies.metadata._continue

    return all_network_policies
