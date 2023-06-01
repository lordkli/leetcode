class Codec:
    
    def __init__(self):
        self.encodingMap = {}
        self.decodingMap = {}
        self.baseUrl = "http://tinyurl.com/" 
        

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl not in self.encodingMap:
            shortUrl = self.baseUrl + str(len(self.encodingMap) + 1)
            self.encodingMap[longUrl] = shortUrl
            self.decodingMap[shortUrl] = longUrl
        return self.encodingMap[longUrl]

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.decodingMap[shortUrl]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

codec = Codec()
print(codec.encode("https://leetcode.com/problems/design-tinyurl"))
print(codec.decode("http://tinyurl.com/1"))