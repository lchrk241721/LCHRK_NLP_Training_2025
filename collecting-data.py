import numpy as np
import tweepy
import json
import pandas as pd
from tweepy import OAuthHandler

#credentials
consumer_key = "22IKpBKj1UM8sq76tX5qrU7za"
consumer_secret = "kxdHIZUkCbxGfK8waM6ncW0478nEG0lYhEmcWgogPUCRudi7Cn"
#access_token = "AAAAAAAAAAAAAAAAAAAAAEqi0wEAAAAAuNDfL%2BeHXiq6aRz%2F2J5OS%2FOpxfU%3DOeiehJuofXFCJPX0aTRKsyPZ5HzvVXtptv0xRqonYRL22TFwp9"
access_token = "1746873399266492416-woVDyLBMNVPCLslol5Hh4Vo7XF7Qtx"
access_token_secret = "BcMUmoPqDQ49S4Hmp3jdVPrEoNRUkXG9Hguz8QmJtZQOp"

#calling API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

 # Query you want to pull the data.
query = "failedtechgeek"

# Fetching tweets
Tweets = api.search_tweets(query, count = 10,lang='en', exclude='retweets',tweet_mode='extended')