import requests
from textblob import TextBlob
import pandas as pd

video_id = '9NQSnAOtrbw'
api_key = "apikey"

# Retrieve video information
video_info_url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={api_key}"
video_info_response = requests.get(video_info_url)
video_info_data = video_info_response.json()
video_info_data

# Retrieve video comments
comments_url = f"https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId={video_id}&key={api_key}"
comments_response = requests.get(comments_url)
comments_data = comments_response.json()

# Extract the comments
comments = [item["snippet"]["topLevelComment"]["snippet"]["textOriginal"] for item in comments_data['items']]
print(comments)

def get_comment_sentiment(comment):
    analysis = TextBlob(comment)
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity == 0:
        return "Neutral"
    else:
        return "Negative"

comment_list = []
sentiment_list = []

for comment in comments:
    sentiment = get_comment_sentiment(comment)
    comment_list.append(comment)
    sentiment_list.append(sentiment)
    print(f"{comment} : {sentiment}")

sentiment_df = pd.DataFrame({"Comments": comment_list, "Sentiment": sentiment_list})
sentiment_df.head() 
sentiment_df.to_csv("YouTube_Comments_Sentiment.csv")


'''
### Terminal Output:

['ALL THE BEST ALL GATE ASPIRANTS...KEEP YOUR NEGATIVE THOUGHTS ASIDE & GIVE YOUR BEST...', 'thanks a lot sir your playlist give me a great hope to crack the gate exam❤', 'Sir rpsc programmer ki preparation start krwao🙏', 'Thank you for giving this instruction.', 'Thank you so much Sir ❤', 'love you so much sir ❤❤❤❤❤❤❤❤❤❤❤❤', 'Thanks for your wishes ❤💐🙏', 'Bhaiya paper solve kijiyega live exam hone ke baad ds and ai ka❤\nAur 2025 ke liye batch kab start hoga bata dijiye', 'Thank you so much sir for motivation just before exam approaching. And also thank you so much for guiding the correct way to solve and attempt.', 'Thank you sir🙏', 'Thanku sir❤❤', 'sir please CSE Gate k liye bhi kuch tips deziye ya phir koi course le aaye', 'ThankU Bhayya...❤', 'Thank you so much sir 🙏', 'Thanku sir', 'Thank you sir ❤', 'Nice topic']
ALL THE BEST ALL GATE ASPIRANTS...KEEP YOUR NEGATIVE THOUGHTS ASIDE & GIVE YOUR BEST... : Positive
thanks a lot sir your playlist give me a great hope to crack the gate exam❤ : Positive
Sir rpsc programmer ki preparation start krwao🙏 : Neutral
Thank you for giving this instruction. : Neutral
Thank you so much Sir ❤ : Positive
love you so much sir ❤❤❤❤❤❤❤❤❤❤❤❤ : Positive
Thanks for your wishes ❤💐🙏 : Positive
Bhaiya paper solve kijiyega live exam hone ke baad ds and ai ka❤
Aur 2025 ke liye batch kab start hoga bata dijiye : Positive
Thank you so much sir for motivation just before exam approaching. And also thank you so much for guiding the correct way to solve and attempt. : Positive
Thank you sir🙏 : Neutral
Thanku sir❤❤ : Neutral
sir please CSE Gate k liye bhi kuch tips deziye ya phir koi course le aaye : Neutral
ThankU Bhayya...❤ : Neutral
Thank you so much sir 🙏 : Positive
Thanku sir : Neutral
Thank you sir ❤ : Neutral
Nice topic : Positive

'''