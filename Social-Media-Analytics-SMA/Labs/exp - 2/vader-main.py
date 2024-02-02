import requests
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download the Vader lexicon for sentiment analysis
import nltk
nltk.download('vader_lexicon')

video_id = '9NQSnAOtrbw'
api_key = "apikey"

# Retrieve video comments
comments_url = f"https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId={video_id}&key={api_key}"
comments_response = requests.get(comments_url)
comments_data = comments_response.json()

# Extract the comments
comments = [item["snippet"]["topLevelComment"]["snippet"]["textOriginal"] for item in comments_data['items']]
print(comments)

# Sentiment analysis using Vader
analyzer = SentimentIntensityAnalyzer()

comment_list = []
compound_scores = []

for comment in comments:
    sentiment_scores = analyzer.polarity_scores(comment)
    compound_score = sentiment_scores['compound']

    comment_list.append(comment)
    compound_scores.append(compound_score)

    sentiment = 'Positive' if compound_score >= 0.05 else ('Neutral' if -0.05 < compound_score < 0.05 else 'Negative')
    print(f"{comment} : {sentiment}")

sentiment_df = pd.DataFrame({"Comments": comment_list, "Compound Score": compound_scores})
sentiment_df.head() 
sentiment_df.to_csv("YouTube_Comments_Sentiment_Vader.csv")


'''
### Terminal Output (vader_lexicon) :


vadar-main.py"
[nltk_data] Downloading package vader_lexicon to C:\Users\Atharva
[nltk_data]     Pawar\AppData\Roaming\nltk_data...
[nltk_data]   Package vader_lexicon is already up-to-date!
['ALL THE BEST ALL GATE ASPIRANTS...KEEP YOUR NEGATIVE THOUGHTS ASIDE & GIVE YOUR BEST...', 'Thank You Sir🙏', 'thanks a lot sir your playlist give me a great hope to crack the gate exam❤', 'Sir rpsc programmer ki preparation start krwao🙏', 'Thank you for giving this instruction.', 'Thank you so much Sir ❤', 'love you so much sir ❤❤❤❤❤❤❤❤❤❤❤❤', 'Thanks for your wishes ❤💐🙏', 'Bhaiya paper solve kijiyega live exam hone ke baad ds and ai ka❤\nAur 2025 ke liye batch kab start hoga bata dijiye', 'Thank you so much sir for motivation just before exam approaching. And also thank you so much for guiding the correct way to solve and attempt.', 'Thank you sir🙏', 'Thanku sir❤❤', 'sir please CSE Gate k liye bhi kuch tips deziye ya phir koi course le aaye', 'ThankU Bhayya...❤', 'Thank you so much sir 🙏', 'Thanku sir', 'Thank you sir ❤', 'Nice topic']
ALL THE BEST ALL GATE ASPIRANTS...KEEP YOUR NEGATIVE THOUGHTS ASIDE & GIVE YOUR BEST... : Positive
Thank You Sir🙏 : Positive
thanks a lot sir your playlist give me a great hope to crack the gate exam❤ : Positive
Sir rpsc programmer ki preparation start krwao🙏 : Neutral
Thank you for giving this instruction. : Positive
Thank you so much Sir ❤ : Positive
love you so much sir ❤❤❤❤❤❤❤❤❤❤❤❤ : Positive
Thanks for your wishes ❤💐🙏 : Positive
Bhaiya paper solve kijiyega live exam hone ke baad ds and ai ka❤
Aur 2025 ke liye batch kab start hoga bata dijiye : Positive
Thank you so much sir for motivation just before exam approaching. And also thank you so much for guiding the correct way to solve and attempt. : Positive
Thank you sir🙏 : Positive
Thanku sir❤❤ : Neutral
sir please CSE Gate k liye bhi kuch tips deziye ya phir koi course le aaye : Positive
ThankU Bhayya...❤ : Neutral
Thank you so much sir 🙏 : Positive
Thanku sir : Neutral
Thank you sir ❤ : Positive
Nice topic : Positive
'''