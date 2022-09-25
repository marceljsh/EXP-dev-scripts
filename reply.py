import tweepy

# ("CONSUMER KEY", "CONSUMER KEY SECRET")
auth = tweepy.OAuthHandler("CU2BjwJU51o8b33Vbbxm7FQJZ", "lU5TaKQJkm5xyVCJiScm8XeyrAy3iZn5ovVBHtsQS9HwOgIm3Q")
# ("ACCESS TOKEN", "ACCESS TOKEN SECRET")
auth.set_access_token("1040844695855718402-ZRr1XadcFzdnAYNk9nSPsLPOVjN67h", "usKZqX4lh5rryzUMIsIS7P1VziOtVzctA0gAP2KQY4O3C")
api = tweepy.API(auth)
status = input("status>> ")
tweetid = input("id>> ")
api.update_status(status, in_reply_to_status_id = tweetid , auto_populate_reply_metadata=True)