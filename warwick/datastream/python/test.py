
import twitter, sys, csv

# XXX: Go to http://twitter.com/apps/new to create an app and get values
# for these credentials that you'll need to provide in place of these
# empty string values that are defined as placeholders.
# See https://dev.twitter.com/docs/auth/oauth for more information 
# on Twitter's OAuth implementation.
CONSUMER_KEY = "R7cBscjqkjgloQX2V4NZFO4VE"
CONSUMER_SECRET = "p2j6xH2NjmubGmk0nDuhmrRNQncVIxCsng9dwP4AGiAtX6UXHw"
ACCESS_TOKEN = "417418987-cCK5Wgb4XcjnNce1o9Zp0i7GLkSPSL4INvpmTtA9"
ACCESS_TOKEN_SECRET = "nGwVk9Bm9h8CfaCFFu4Q8YgXxRGRh7UFkuX72vEbFwBoY"

auth = twitter.oauth.OAuth(ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY,
	CONSUMER_SECRET)

# Query terms
q = "Paris, love" # Comma-separated list of terms

print >> sys.stderr, "Filtering the public timeline for track = \"%s\"" % q

# Returns an instance of twitter.Twitter
twitter_api = twitter.Twitter(auth=auth)

# Reference the self.auth parameter
twitter_stream = twitter.TwitterStream(auth=twitter_api.auth)

# See https://dev.twitter.com/docs/streaming-apis
stream = twitter_stream.statuses.filter(track=q)

with open("twitter-hashtag-stream.csv", "a") as csv_file:
	csv.writer(csv_file).writerow(["ID_STR", "CREATED_AT", "SCREEN_NAME",
		"TEXT", "HASHTAGS"])
	
	for tweet in stream:
		print tweet['id_str'],\
		tweet['created_at'],\
		tweet['user']['screen_name'].encode('utf-8'),\
		tweet['text'].encode('utf-8'),\
		[ hashtag['text'].encode('utf-8') for hashtag in tweet['entities']\
		['hashtags'] ]

		for hashtag in tweet['entities']['hashtags']:
			csv.writer(csv_file).writerow([
			tweet['id_str'],
			tweet['created_at'],
			tweet['user']['screen_name'].encode('utf-8'),
			tweet['text'].encode('utf-8'),
			hashtag['text'].encode('utf-8')
			])