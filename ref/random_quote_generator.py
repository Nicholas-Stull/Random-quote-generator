import random
import json


def get_random_quote(wordcount=None):
    # Load quotes from JSON file
    filename = "ref\src\quotes.json"
    with open(filename, "r", encoding="utf-8") as f:
        quotes = json.load(f)

    # Set the wordcount limit
    if wordcount is not None and isinstance(wordcount, int) and wordcount > 0:
        limit = wordcount
    else:
        limit = 10

    # Generate and return a random quote string
    quote = random.choice(quotes)
    quote_words = quote["quote"].split()
    if len(quote_words) > limit:
        quote_words = quote_words[:limit] + ["..."]
    quote_text = f'"{ " ".join(quote_words) }"\n- {quote["author"]}'
    return quote_text

