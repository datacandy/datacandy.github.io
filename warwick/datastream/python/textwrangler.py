#1. Initialize your private stuff 
consumer_key = 'R7cBscjqkjgloQX2V4NZFO4VE' 
consumer_secret = 'p2j6xH2NjmubGmk0nDuhmrRNQncVIxCsng9dwP4AGiAtX6UXHw' 
access_token = '417418987-cCK5Wgb4XcjnNce1o9Zp0i7GLkSPSL4INvpmTtA9' 
access_token_secret = 'nGwVk9Bm9h8CfaCFFu4Q8YgXxRGRh7UFkuX72vEbFwBoY'

#2. Authenticate 
auth=tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret)

#3. Get a reference 
api = tweepy.API(auth)

#4. Get those details!!! 
print api.me()

















