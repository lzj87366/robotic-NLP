'''
This code from kaggle,URL:kaggle.com/code/ahsannawazch/0-84002-baseline-roberta-large/notebook
function of the code is clear the text
'''
import re
import emoji
import contractions
import html

def clean_tweet(text):
        text = text.strip()  # Remove leading/trailing spaces
        
        # Convert HTML entities
        text = html.unescape(text)
        
        # Fix corrupted Unicode artifacts
        text = text.replace("‰ÛÏ", '"').replace("‰Û", '"')  # Fix double quotes
        text = text.replace("‰Û÷", "'").replace("‰Ûª", "'")  # Fix single quotes
        text = text.replace("‰Û¢", "-").replace("‰Û_", "-")  # Fix hyphen issues
        
        # Remove any remaining corrupted symbols
        text = re.sub(r"[^\x00-\x7F]+", "", text)  # Remove remaining non-ASCII characters
        
        # Remove URLs
        text = re.sub(r'http\S+', '', text)
        
        # Remove mentions (@username)
        text = re.sub(r'@\w+', '', text)
        
        # Handle emojis
        text = emoji.demojize(text, delimiters=(" ", " "))  
        
        # Expand contractions
        text = contractions.fix(text)
    
        return text

# Apply to dataset
train_df["text"] = train_df["text"].apply(clean_tweet)
test_df["text"] = test_df["text"].apply(clean_tweet)