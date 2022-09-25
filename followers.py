import tweepy
 
user_key = 'CU2BjwJU51o8b33Vbbxm7FQJZ'
user_secret = 'lU5TaKQJkm5xyVCJiScm8XeyrAy3iZn5ovVBHtsQS9HwOgIm3Q'
access_token = '11040844695855718402-ZRr1XadcFzdnAYNk9nSPsLPOVjN67h'
access_secret = 'usKZqX4lh5rryzUMIsIS7P1VziOtVzctA0gAP2KQY4O3C'
 
author = tweepy.OAuthHandler(user_key, user_secret)
author.set_access_token(access_token, access_secret)
 
API = tweepy.API(author)
 
followers = API.followers()
for follower in followers:
    print(follower.screen_name)