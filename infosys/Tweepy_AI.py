import tweepy
from run_promt import execute_gemini
import json

API_KEY ="W8KpHdCdTfNtP5VFbJs21Gecd"
API_SECRET_KEY = "JbX2FPEoJKFFVlG6K6dgtjLimZ04vYb4TiquaITUNIMzZKBopG"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAOWM3gEAAAAAXe93WDtAGGACD5fz%2BfLtngKetnE%3D9U9LKgK4hpeobT8dHRCLGLr2nbpxVsNx8w4GjZhCPeVuQSJ0ZN"
ACCESS_TOKEN = "1590653080848125952-CCdBpL2kS3B2oVc9fi2lrK9eoXlwAl"
ACCESS_TOKEN_SECRET = "KfILyjjctImdGZcqwXoXnsjeEPzeIkS06vlhEaj63bgeJ"

twitterClient = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET_KEY,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET,
    wait_on_rate_limit=True,
)

# user = twitterClient.get_user(username="sonusood")

# print (user.data.id)

# sonusood_id = user.data.id

# # url --> https://x.com/sonusood
# tweets = twitterClient.get_users_tweets(sonusood_id,max_results=5)

# print(tweets.data)


user= twitterClient.get_user(username="Google")
user_id = user.data.id


# Latest_5_tweets = twitterClient.get_users_tweets(user_id, max_results=5)


# for tweet in Latest_5_tweets.data:
#     print(tweet.text)
#     prompt = f"Analyze the following tweet: {tweet.text}"
#     llm_out = execute_gemini(prompt)
#     print(llm_out)


