from cgspy.network.get import hostname

from requests import ConnectionError, get


class Whois:
    def __init__(self, IP):
        self.ip_address = IP


    def get_info(self):
        try:
            response = get(
                f'http://ip-api.com/json/{self.ip_address}'
            )

            return response.json()
        
        except ConnectionError:
            return None
        
    def display_info(self, info, IP):
        print(f"[*] HOSTNAME: {hostname(IP)}")

        print(
            f'''
    [+] STATUS : {info.get('status', 'N/A')}
    [+] COUNTRY : {info.get('country', 'N/A')}
    [+] COUNTRY CODE : {info.get('coutryCode', 'N/A')}
    [+] REGION: {info.get('region', 'N/A')}
    [+] REGION NAME: {info.get('regionName', 'N/A')}
    [+] CITY: {info.get('city', 'N/A')}
    [+] ZIP: {info.get('zip', 'N/A')}
    [+] LAT: {info.get('lat', 'N/A')}
    [+] LON: {info.get('lon', 'N/A')}
    [+] TIMEZONE: {info.get('timezone', 'N/A')}
    [+] ISP: {info.get('isp', 'N/A')}:
        [+] ORG: {info.get('org', 'N/A')}
        [+] AS: {info.get('as', 'N/A')}
    [+] QUERY: {info.get('query', 'N/A')}
'''
)