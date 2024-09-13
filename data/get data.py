from datasets import load_dataset

# Load the dataset from Hugging Face
ds = load_dataset("mjw/stock_market_tweets")

# Save the dataset locally in CSV format
ds['train'].to_csv("stock_market_tweets.csv", index=False)


