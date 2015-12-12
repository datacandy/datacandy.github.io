import twitter, sys, csv

CONSUMER_KEY = "BfWhILEiLISWkNRIxIZMcfWIl"
CONSUMER_SECRET = "gYB5gsMP9CJYxQp4FDhcJ1l6fEh75MzY2jfarJPhYXYqoyW1IF"
ACCESS_TOKEN = "417418987-BURt6knbA65EQouhaI56rp25sjUyJOoRz7Va15XS"
ACCESS_TOKEN_SECRET = "kgYThQYtOyYft66XpnZ3Kdr3vjWN7lEvqFirDLJGvaJhH"

auth = twitter.oauth.OAuth(ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY,
	CONSUMER_SECRET)

q = "refugees" 

print >> sys.stderr, "Filtering the public timeline for track = \"%s\"" % q

twitter_api = twitter.Twitter(auth=auth)

twitter_stream = twitter.TwitterStream(auth=twitter_api.auth)

stream = twitter_stream.statuses.filter(track=q)

with open("output.csv", "a") as csv_file:
	csv.writer(csv_file).writerow(["ID_STR", "CREATED_AT", "SCREEN_NAME",
		"TEXT", "HASHTAGS"])
	
	for tweet in stream:
		print (tweet)['id_str'],\
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
