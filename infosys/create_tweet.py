import pandas as pd
import json
from run_promt import execute_gemini_for_tweet_creation

def get_top_5_tweets(engagement_type, analyzed_tweets):
    if not analyzed_tweets:
        return []
    df = pd.DataFrame(analyzed_tweets)
    if 'engagement_type' not in df.columns or 'engagement_score' not in df.columns:
        raise ValueError("Input data must contain 'engagement_type' and 'engagement_score'")
    filtered_df = df[df['engagement_type'] == engagement_type]
    return filtered_df.nlargest(5, columns=['engagement_score']).to_dict(orient="records")

def generate_tweet(analyzed_tweets):
    top_tweets = get_top_5_tweets("like", analyzed_tweets)

    user_prompt = """
    Write a tweet for the newly releasing
    iPhone 17 Pro Max with A18 Pro SoC launching
    with physically moving camera zoom.
    Make this tweet more appealing for camera enthusiasts.
    """

    system_prompt = f"""
    Create an engaging Twitter tweet for my tech company.

    PROMPT: {user_prompt}

    Here are some example tweets and their sentiment
    analysis with very high user engagements from other similar companies.

    Example Tweets:
    {top_tweets}

    Create the tweet, compare it with the example tweets,
    and predict and explain why and how this tweet will
    perform well compared to the given examples.
    """

    output = execute_gemini_for_tweet_creation(system_prompt)
    result = json.loads(output)

    tweet = result.get('tweet')
    prediction = result.get('prediction')
    explanation = result.get('explanation')

    print("Generated Tweet:", tweet)
    print("Prediction:", prediction)
    print("Explanation:", explanation)

    return result

# Load tweets from file
with open("analyzed_tweets.json") as f:
    data = json.load(f)
    print("Tweets loaded:", len(data))
    generate_tweet(data)
