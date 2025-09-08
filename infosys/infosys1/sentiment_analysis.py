import tweepy
from run_promt import execute_gemini

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

        user = twitterClient.get_user(username="sundarpichai")

        user_id = user.data.id

        Latest_5_tweets = twitterClient.get_users_tweets(user_id, max_results=30)

        for tweet in Latest_5_tweets.data:
            # print(tweet.text)
            prompt = f"""
            Summarize the twitter tweet attached and give it a sentimental analysis score
            TWEET ==> {tweet.text}
            """
            llm_out = execute_gemini(prompt)
            print(llm_out)