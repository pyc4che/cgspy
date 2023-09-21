from ipaddress import ip_address, ip_network
from configs.networks import EXCLUDED_NETWORKS


def is_excluded(IP):
    for network in EXCLUDED_NETWORKS:
        if ip_address(IP) in ip_network(network):
            return True
        
    return False
