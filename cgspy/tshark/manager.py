from os import popen


from pyshark import LiveCapture

from cgspy.network.get import ip
from cgspy.network.exclude import is_excluded



class TShark:
    def __init__(self):
        self.ip_address = ip()
        self.path = popen('which tshark').read().strip()
        

    def is_available(self):
        if not self.path:
            return False
        else:
            return True

    
    def xor_map(self, iface):
        capture = LiveCapture(
            interface=iface,
            display_filter='stun'
        )

        for packet in capture.sniff_continuously(
            packet_count=250
        ):
            if hasattr(packet, 'ip'):
                src = packet.ip.src
                dst = packet.ip.dst

                if is_excluded(src) or is_excluded(dst):
                    continue

                if packet.stun:
                    xor_mapped_address = packet.stun.get_field_value(
                        'stun.att.ipv4'
                    )

                    if xor_mapped_address:
                        if xor_mapped_address != self.ip_address:
                            return xor_mapped_address

        return None
