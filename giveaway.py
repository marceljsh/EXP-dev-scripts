# this script is intended to spam reply on a certain tweet in order to win giveaway

import tweepy
import random
import datetime
import time

def spam(amount: int, status: str, tweetid: str) -> None:
    user_key = "CU2BjwJU51o8b33Vbbxm7FQJZ"
    user_secret = "lU5TaKQJkm5xyVCJiScm8XeyrAy3iZn5ovVBHtsQS9HwOgIm3Q"
    auth = tweepy.OAuthHandler(user_key, user_secret)

    access_token = "1040844695855718402-ZRr1XadcFzdnAYNk9nSPsLPOVjN67h"
    access_key = "usKZqX4lh5rryzUMIsIS7P1VziOtVzctA0gAP2KQY4O3C"
    auth.set_access_token(access_token, access_key)
    
    api = tweepy.API(auth)

    for i in range(amount):
        send = str(status) + " " + str(i+1)
        
        # random pause time (2, 4)
        pause = random.randint(2,4)
        api.update_status(send, in_reply_to_status_id = tweetid , auto_populate_reply_metadata=True)
        print("acel@host $ success-pause", str(pause) + "s\t", datetime.datetime.now())
        time.sleep(pause)

def main() -> None:
    amount = int(input("amount>> "))
    status = input("status>> ")
    tweetid = input("id>> ")
    spam(amount, status, tweetid)

if __name__ == '__main__':
    main()