import twitter
import tweepy
from textblob import TextBlob
import matplotlib as mpl

consumer_key = "OTKkOwGPqIJBpbF5hKMHjs3Lc"
consumer_key_secret = "z0Qiop3xjEFqoL6J3zc4JIMBjX569AlNL9hNKU8r7TvDtvNK2I"
access_token = "1236369835384168448-FzfW5YftxcMJbeFHU2ldkri7bZl8Lm"
access_token_secret = "1Snd5zhk3u7jiVRdf6FpCrXoxFjlhfkcpqB1RaIhZ7uof"

auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

val = input('Search term: ')
count = 100
result_type = 'popular'
until = '2020-03-01'
lang = 'en'

public_tweets = api.search(q = val, count = count, result_type = result_type, until = until)

positive_count = 0
negative_count = 0

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

total_count = positive_count + negative_count
if positive_count > negative_count:
    print("Sentiment towards %s is positive: %d positive tweets, %d negative tweets" % (val, positive_count, negative_count))
elif positive_count < negative_count:
    print("Sentiment towards %s is negative: %d positive tweets, %d negative tweets" % (val, positive_count, negative_count))
else:
    print("Sentiment towards %s is indifferent" % (val))
