import twitter
import tweepy
from textblob import TextBlob

class SentimentAnalysis:

    def __init__(self, search, count, result_type, until, lang):
        self.search = search
        self.count = count
        self.result_type = result_type
        self.until = until
        self.lang = lang

    def call_api(self):
        # Enter your Twitter API keys here
        # Consumer API keys:
        consumer_key = "___"
        consumer_key_secret = "___"
        # Access token & access token secret
        access_token = "___"
        access_token_secret = "___"

        # Tweepy library connects to Twitter API authentication
        auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)

        # API Call
        public_tweets = api.search(q = self.search, count = self.count, result_type = self.result_type, until = self.until, lang = self.lang)

        # Values for analysis
        positive_count = 0
        negative_count = 0

        # Textblob NLP Analysis
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

        # Print statements to console
        total_count = positive_count + negative_count
        if positive_count > negative_count:
            print("Sentiment towards %s is positive: %d positive tweets, %d negative tweets" % (self.search, positive_count, negative_count))
        elif positive_count < negative_count:
            print("Sentiment towards %s is negative: %d positive tweets, %d negative tweets" % (self.search, positive_count, negative_count))
        elif positive_count == negative_count:
            print("Sentiment towards %s is indifferent: %d positive tweets, %d negative tweets" % (self.search, positive_count, negative_count))
        else:
            print("Error: Please make sure 'until' parameter is within one week of current date, or regenerate Twitter API keys.")

if __name__ == "__main__":
    # Edit parameters for search here:
    search = input('Search term: ')
    # Number of tweets to pull during API call
    count = 100
    # Result type 'recent' pulls only the most recent tweets, 'popular' pulls only the most popular tweets
    result_type = 'recent'
    # Time horizon to pull data from. MAKE SURE DATE IS WITHIN ONE WEEK OF CURRENT DATE!
    until = '2020-05-02'
    # Language setting to english
    lang = 'en'

    model = SentimentAnalysis(search, count, result_type, until, lang)
    model.call_api()
