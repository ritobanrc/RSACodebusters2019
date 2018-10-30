from quote_file_mod import get_quotes
import Caesar
import random


quotes = get_quotes()

quote = random.choice(quotes)


print(quote)
