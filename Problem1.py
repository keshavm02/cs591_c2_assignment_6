class URL_Splitting():
    def __init__(self, url):
        self.url = url

    def getProtocol(self):
        return self.url.split('://')[0]

    def getDomain(self):
        return self.url.split('/')[2]