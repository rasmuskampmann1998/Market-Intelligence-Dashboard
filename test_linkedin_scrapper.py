from apify_client import ApifyClient
import json

# Initialize the ApifyClient with your API token
client = ApifyClient("apify_api_pcGK8MnzZ36IXKAUNvKNLwwahzUrpf0B8JUq") 

# Prepare the Actor input to fetch agriculture-related content
run_input = {
    "keyword": "tomato innovation, tomato farming, tomato technology, tomato patents, tomato research, tomato crop, tomato trends, heirloom tomatoes, tomato disease, tomato pests, tomato care",
    "sort_type": "relevance",      # Sort by relevance (you can change to 'date' or 'hot' based on preference)
    "page_number": 1,              # Start from page 1 (you can change this based on the page you need)
    "date_filter": "",             # Empty string for no date filter (you can specify date ranges if required)
    "limit": 50,                   # Limit to 50 items (adjust as needed)
}
# Run the Actor and wait for it to finish
run = client.actor("apimaestro/linkedin-posts-search-scraper-no-cookies").call(run_input=run_input)

# Fetch results and save them to a JSON file
results = [item for item in client.dataset(run["defaultDatasetId"]).iterate_items()]

# Save results to JSON file named 'agriculture_linkedin.json'
with open("agriculture_linkedin.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print("✅ Data saved to agriculture_linkedin.json")
