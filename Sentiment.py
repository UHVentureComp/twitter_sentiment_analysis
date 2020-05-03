import twitter
import tweepy
from textblob import TextBlob
import matplotlib as mpl

#Standard Twitter API Keys
consumer_key = "sTHGIyqNhYPyDTxr4UlBf77Vk"
consumer_key_secret = "cN1NQTLA69Y8khRSX90FKCYJLcv6SdRCwDrN0SAynMeEAvSfMF"
access_token = "1236369835384168448-nRxodOp86kDjkU29Vlh9rj3ESMKE3j"
access_token_secret = "ATbfpnRpxjYLQWclOqsRfHPIXzYRjs0ZPKwRcmcQp3Juk"

#Tweepy library connects to Twitter API authentification
auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#SEARCH CRITERIA (Change accordingly):
#Seach term input (leave alone)
val = input('Search term: ')
#Number of tweets
count = 100
#Result_type can be:
###'recent': return only the most recent results in the response
###'popular': return only the most popular results in the response
###'mixed':Include both popular and real time results in the response.
result_type = 'recent'
#Change to whatever date you want algo to start pulling data from
until = '2020-03-13'
#Lanuage Filter: uses ISO 639-1 lanuage names
lang = 'en'

#API Call
public_tweets = api.search(q = val, count = count, result_type = result_type, until = until, lang = lang)

#Values for analysis
positive_count = 0
negative_count = 0

#Textblob NLP Analysis
for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    if analysis.sentiment[0]>0:
        print('Positive')
        positive_count += 1
    else:
        print('Negative')
        negative_count += 1
    print("")

#Print statements to console
total_count = positive_count + negative_count
if positive_count > negative_count:
    print("Sentiment towards %s is positive: %d positive tweets, %d negative tweets" % (val, positive_count, negative_count))
elif positive_count < negative_count:
    print("Sentiment towards %s is negative: %d positive tweets, %d negative tweets" % (val, positive_count, negative_count))
else:
    print("Sentiment towards %s is indifferent" % (val))
