import requests
from textblob import TextBlob
import pandas as pd

video_id = 'nirn1jVIi1s'
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

['😂😂😂😂😂😂😂', '😂❤😍', 'Manaara ka sat ak pic ❤❤', 'Abba kadar : paani kisne mara tha ☠️ was epic❤😂😂', 'Bhai Bhai asli winner toh bs Babu bhayia  the hai aur rahenge', 'Bhai ho aap❤', 'Bechara Aba kader pani nahi marna tha bechare par 🤣🤣🤣🤣🤣🤣', 'System hang to let all know YouTube views show delay than likes when more people have watched..... After 48 hours views will be exactly updated but likes are accurate  second to second... Hope all doubts are clarified GOAT talent munawar bhai❤', 'Munawar farooqi fan like', 'Kya bolte YouTube hang hoga 😂😂 manowar Bhai🔥', 'Osm ek no ....bhut dino ke baad .... mood fresh ho gya .... wait tha 😂😂😂😂😂😂bhut acha ❤❤❤❤❤❤❤❤❤❤', 'bahot paka raha hai ......very poor jokes maaza nahi aaya....', 'hats off bhai.......love ur videos😍😍', 'Abba kadar😂😂 idol hai Apna😂', 'Ghost story 2 kab Aayegi😢', 'Super Brotherrr', 'The Legend of Abba Qader\n😂', 'Mjy smj ni aye y😅😅']
😂😂😂😂😂😂😂 : Neutral
😂❤😍 : Neutral
Manaara ka sat ak pic ❤❤ : Neutral
Abba kadar : paani kisne mara tha ☠️ was epic❤😂😂 : Neutral
Bhai Bhai asli winner toh bs Babu bhayia  the hai aur rahenge : Neutral
Bhai ho aap❤ : Neutral
Bechara Aba kader pani nahi marna tha bechare par 🤣🤣🤣🤣🤣🤣 : Neutral
System hang to let all know YouTube views show delay than likes when more people have watched..... After 48 hours views will be exactly updated but likes are accurate  second to second... Hope all doubts are clarified GOAT talent munawar bhai❤ : Positive
Munawar farooqi fan like : Neutral
Kya bolte YouTube hang hoga 😂😂 manowar Bhai🔥 : Neutral
Osm ek no ....bhut dino ke baad .... mood fresh ho gya .... wait tha 😂😂😂😂😂😂bhut acha ❤❤❤❤❤❤❤❤❤❤ : Positive
bahot paka raha hai ......very poor jokes maaza nahi aaya.... : Negative
hats off bhai.......love ur videos😍😍 : Neutral
Abba kadar😂😂 idol hai Apna😂 : Neutral
Ghost story 2 kab Aayegi😢 : Neutral
Super Brotherrr : Positive
The Legend of Abba Qader
😂 : Neutral
Mjy smj ni aye y😅😅 : Neutral

'''