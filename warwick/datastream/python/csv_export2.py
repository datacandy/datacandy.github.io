import tweepy, itertools, csv, sys
from datetime import datetime



auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# Definite a pagination function (necessary to submit the maximum 100 screen
# names per request):
def paginate(iterable, page_size):
    while True:
		i1, i2 = itertools.tee(iterable)
		iterable, page = (itertools.islice(i1, page_size, None),
			list(itertools.islice(i2, page_size)))
		
		if len(page) == 0:
			break
		
		yield page

# Count the input screen names:
with open("screen-names.txt") as screen_names:
	input_count = sum(1 for line in screen_names)

# Open a CSV file to append:
csv_file = open("nodes.csv", "a")
csv.writer(csv_file).writerow(["USER_ID", "SCREEN_NAME", "ATTRIBUTE"])

# Use the Twitter REST API GET users/lookup method to get the user IDs for each
# of the input screen names:
with open("screen-names.txt") as screen_names:
	print "Getting user IDs for input screen names on " + \
	datetime.now().strftime("%Y-%m-%d") + " at " + \
	datetime.now().strftime("%H:%M") + "..."
	got_ids = []
	for page in paginate(screen_names, 100):
		users = api.lookup_users(screen_names=page)
		# Append the returned screen names to the CSV:
		for user in users:
			csv.writer(csv_file).writerow([user.id, user.screen_name, 1])
			got_ids.append(user.id)

		print "Got %i of %i user IDs..." % (len(got_ids), input_count)

	print "Finished getting user IDs on " + \
	datetime.now().strftime("%Y-%m-%d") + " at " + \
	datetime.now().strftime("%H:%M") + ". Getting friends..."

# Use the Twitter REST API GET friends/ids method to get the user IDs for each
# of the input users' friends:
with open("screen-names.txt") as screen_names:
	total_friends = []
	for line in screen_names:
		try:
			friends_ids = tweepy.Cursor(api.friends_ids, screen_name=
				line.rstrip())

			got_friends = []
			# Append the returned user IDs to the CSV:
			for friend_id in friends_ids.items():
				csv.writer(csv_file).writerow([friend_id, "", 0])
				got_friends.append(friend_id)
				total_friends.append(friend_id)

			# for page in paginate(friends_ids.items(), 100):
			# 	users = api.lookup_users(user_ids=page)
			# 	for user in users:
			# 		csv.writer(csv_file).writerow([user.id, user.screen_name, 0])
			# 		got_friends.append(user.id)
			# 		total_friends.append(friend_id)

			# 	print "Got %i of %i friends..." % (len(got_friends), len(total_friends)

		except tweepy.TweepError as error:
			if error.reason == "Not authorized.":
				print "@%s account protected." % line.rstrip()

			else:
				pass

		print "Got %i friends of @%s on " % (len(got_friends), line.rstrip()) \
		+ datetime.now().strftime("%Y-%m-%d") + " at " + \
		datetime.now().strftime("%H:%M") + "..."

	print "Finished getting %i friends on " % len(total_friends) + \
	datetime.now().strftime("%Y-%m-%d") + " at " + \
	datetime.now().strftime("%H:%M") + ". Done."

sys.exit
