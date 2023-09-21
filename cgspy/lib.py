from sys import exit

from cgspy.argparser.parser import Arguments

from cgspy.network.iface import choose

from cgspy.tshark.manager import TShark
from cgspy.whois.manager import Whois


def init():
    parser = Arguments()
    parser.make_args()
    
    args = parser.parse_args()


    if args.iface:
        iface = args.iface
    else:
        iface = choose()

    tshark = TShark()
    if tshark.is_available():
        address = tshark.xor_map(iface)

        if address:
            print(f"IP ADDRESS SUCCESSFULLY TRACKED: {address}")

            whois = Whois(address)
            whois.display_info(whois.get_info(), address)

        else:
            print("TRACKING FAILED ! :(")

    else:
        print("[!] Install Wireshark!")
        exit(1)