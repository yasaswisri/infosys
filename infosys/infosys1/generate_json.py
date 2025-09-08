import tweepy
from run_promt import execute_gemini
import json

API_KEY = "4uVOD6ewnumaiFhJKfriL0D9j"
API_SECRET_KEY = "kzF6bXAAIq4d1NmgChmh1Wa3rJNDqFQd9tZXXtsE9TO87O0htg"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAFKM3gEAAAAA7ycPRfAI5oCsFCwYKK1ut2U0%2Bgs%3DpdlEFu4YsGjibEOjbjx0CNI0UrOfpC1oIBoVDzM7ZiwxHyqjfz"
ACCESS_TOKEN = "1957415390625292288-Ies0v7ZThcgYsvTXFEeG1xhzbYnVHE"
ACCESS_TOKEN_SECRET = "HWCeOENdWlgS1xsdAEq2DYNs93MCzVkEs8rMld5GK1XUz"

if __name__ == "__main__":
        twitterClient = tweepy.Client(
            bearer_token=BEARER_TOKEN,
            access_token_secret=ACCESS_TOKEN_SECRET,
            consumer_key=API_KEY,
            consumer_secret=API_SECRET_KEY,
            access_token=ACCESS_TOKEN,
            wait_on_rate_limit=True,
        )

        user = twitterClient.get_user(username="vickykaushal09")

        user_id = user.data.id
        tweets = twitterClient.get_users_tweets(user_id, max_results=50, tweet_fields=['created_at', 'text', 'public_metrics'])

        # with open("extracted_tweets.json", "w") as json_file:
        #     json.dump(tweets.data, json_file, indent=4)

        tweet_list = []
if tweets.data:
    for tweet in tweets.data:
        tweet_dict = {
            "id": tweet.id,
            "text": tweet.text,
            "created_at": str(tweet.created_at),
            "metrics": tweet.public_metrics
        }
        tweet_list.append(tweet_dict)

# Save to JSON
with open("extracted_tweets.json", "w", encoding="utf-8") as json_file:
    json.dump(tweet_list, json_file, ensure_ascii=False, indent=4)

print("Tweets saved to extracted_tweets.json")