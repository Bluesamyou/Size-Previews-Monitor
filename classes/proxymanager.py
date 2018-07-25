#TODO: Fix this up to take multiple proxies, and format copped proxies to user:pass@ip:port
from random import randint

class ProxyManager:
    def __init__(self):
        self.formattedProxies  = []
        with open('proxies.txt') as proxy_file:
            self.proxies = proxy_file.readlines()
            for proxies in range(len(self.proxies)):
                formatProxy = "{}:{}@{}:{}".format(self.proxies[proxies].rstrip().split(":")[2],self.proxies[proxies].rstrip().split(":")[3],self.proxies[proxies].rstrip().split(":")[0],self.proxies[proxies].rstrip().split(":")[1] )
                self.formattedProxies.append(formatProxy)

        self.index = 0

    def get_next_proxy(self,randomProxy):
        if self.index == len(self.formattedProxies):
            return ""
        if randomProxy:
            return self.formattedProxies[randint(0,len(self.formattedProxies))]
        else:
            return self.formattedProxies[0]



