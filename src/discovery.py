from zeroconf import ServiceBrowser, Zeroconf
import time

class DeviceListener:
    def remove_service(self, zeroconf, typ, name):
        return

    def add_service(self, zconf, typ, name):
        service = None
        tries = 0
        while service is None and tries < 4:
            service = zconf.get_service_info(typ, name)
            tries += 1

        if service:
            ips = zconf.cache.entries_with_name(service.server.lower())
            host = repr(ips[0]) if ips else service.server
            name=name.encode("utf-8")
            print("2")
            print("ip="+host)
            print("name="+name[:name.index("._googlecast")])

zeroconf = Zeroconf()
listener = DeviceListener()
browser = ServiceBrowser(zeroconf, "_googlecast._tcp.local.", listener)
time.sleep(5)