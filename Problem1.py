class URL_Splitting():
    def __init__(self, url):
        self.url = url

    def getProtocol(self):
        """
        assuming that anything before "://" in a url should be the protocol
        """
        return self.url.split('://')[0]

    def getDomain(self):
        """
        assuming that "anything.anything.anything" can be a domain
        eg: docs.python.org
        """
        return self.url.split('/')[2]

    def getPath(self):
        """
        assuming that the path has no sub-paths
        i.e. the path has no '/' in it
        """
        return self.url.split('/')[3]