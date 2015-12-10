from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener


#consumer key, consumer secret, access token, access secret.
ckey="R7cBscjqkjgloQX2V4NZFO4VE"
csecret="p2j6xH2NjmubGmk0nDuhmrRNQncVIxCsng9dwP4AGiAtX6UXHw"
atoken="417418987-cCK5Wgb4XcjnNce1o9Zp0i7GLkSPSL4INvpmTtA9"
asecret="nGwVk9Bm9h8CfaCFFu4Q8YgXxRGRh7UFkuX72vEbFwBoY"

class listener(StreamListener):

    def on_data(self, data):
        print(data)
        return(True)

    def on_error(self, status):
        print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["car"])

