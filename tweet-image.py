import tweepy

user_key = "CU2BjwJU51o8b33Vbbxm7FQJZ"
user_secret = "lU5TaKQJkm5xyVCJiScm8XeyrAy3iZn5ovVBHtsQS9HwOgIm3Q"
author = tweepy.OAuthHandler(user_key, user_secret)

access_token = "1040844695855718402-ZRr1XadcFzdnAYNk9nSPsLPOVjN67h"
access_secret = "usKZqX4lh5rryzUMIsIS7P1VziOtVzctA0gAP2KQY4O3C"
author.set_access_token(access_token, access_secret)

API = tweepy.API(author)
tweet = input("tweet>> ")
print('\naddress example: C:/Users/facadmin1/Downloads/introdev.PNG')
image = input("pic address>> ")
#Enter image location image="C:/Users/facadmin1/Downloads/introdev.PNG"
API.update_with_media(image, tweet)
print ("Done!")