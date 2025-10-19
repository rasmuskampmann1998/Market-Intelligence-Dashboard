from apify_client import ApifyClient
import json


# Initialize the ApifyClient with your API token
client = ApifyClient("apify_api_pcGK8MnzZ36IXKAUNvKNLwwahzUrpf0B8JUq") 

# Prepare the Actor input
run_input = {
    "searchTerms": [
        "tomato agriculture news",
        "farming technology",
        "climate and agriculture",
        "crop yields",
        "global agriculture trends",
        "sustainable farming"
    ],
    "tweetLanguage": "en",  # English language
    "sort": "Latest",  # Latest tweets
    "maxItems": 10,  # Limit to 100 tweets
    "minimumRetweets": 2,  # Filter for meaningful tweets
    "minimumFavorites": 2,
    "minimumReplies": 1,
    "customMapFunction": "(object) => { return {...object} }"
}

try:
    # Run the Actor and wait for it to finish
    run = client.actor("CJdippxWmn9uRfooo").call(run_input=run_input)
    print(f"Run started with ID: {run['id']}")

    # Fetch and store results
    results = [item for item in client.dataset(run["defaultDatasetId"]).iterate_items()]
    print(f"Fetched {len(results)} results")

    # Save to JSON
    with open("global_agriculture_tweets.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print("✅ Data saved to global_agriculture_tweets.json")

except Exception as e:
    print(f"Error during the Apify run: {e}")