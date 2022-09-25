import tweepy

user_key = "bD0QTg6fmP0en4yBBZEFMDFO2"
user_secret = "7dnhxG9AmMZBJTVSmVDSx1Myf4EL6wI32NZLSXoqgraUh6fYj3"
auth = tweepy.OAuthHandler(user_key, user_secret)

access_token = "1458965264020557824-Bc87KEmcsqMFQyfa0WkL6SfqaJJp5n"
access_key = "qKsxk8hqc0aetknnDI1RduT0FdrlMhLSqQCCbuh6DDfAL"
auth.set_access_token(access_token, access_key)

API = tweepy.API(auth)
tweet = input("Conjure Up A Tweet: ")
API.update_status(status =(tweet))
print ("Done!")