import requests
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download the Vader lexicon for sentiment analysis
import nltk
nltk.download('vader_lexicon')

video_id = 'nirn1jVIi1s'
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

['😮😮😮', '❤❤❤', 'Abakadar is such a gem character..😂', 'Munawar❤', 'Bhai main fan hu tumahara lakin funny nahi hai yeh video kuch bhi dal rahe ho', 'Woooh the wait is over now', 'Bhi last mai to roola he diya tha😢😢😢 but jad usna kaaha pani kisna phaka😅😅😅', '😂😂😂😂😂😂😂', '😂❤😍', 'Manaara ka sat ak pic ❤❤', 'Abba kadar : paani kisne mara tha ☠️ was epic❤😂😂', 'Bhai Bhai asli winner toh bs Babu bhayia  the hai aur rahenge', 'Bhai ho aap❤', 'Bechara Aba kader pani nahi marna tha bechare par 🤣🤣🤣🤣🤣🤣', 'System hang to let all know YouTube views show delay than likes when more people have watched..... After 48 hours views will be exactly updated but likes are accurate  second to second... Hope all doubts are clarified GOAT talent munawar bhai❤', 'Munawar farooqi fan like', 'Kya bolte YouTube hang hoga 😂😂 manowar Bhai🔥', 'Osm ek no ....bhut dino ke baad .... mood fresh ho gya .... wait tha 😂😂😂😂😂😂bhut acha ❤❤❤❤❤❤❤❤❤❤', 'bahot paka raha hai ......very poor jokes maaza nahi aaya....']
😮😮😮 : Neutral
❤❤❤ : Neutral
Abakadar is such a gem character..😂 : Neutral
Munawar❤ : Neutral
Bhai main fan hu tumahara lakin funny nahi hai yeh video kuch bhi dal rahe ho : Positive
Woooh the wait is over now : Neutral
Bhi last mai to roola he diya tha😢😢😢 but jad usna kaaha pani kisna phaka😅😅😅 : Neutral
😂😂😂😂😂😂😂 : Neutral
😂❤😍 : Neutral
Manaara ka sat ak pic ❤❤ : Neutral
Abba kadar : paani kisne mara tha ☠️ was epic❤😂😂 : Neutral
Bhai Bhai asli winner toh bs Babu bhayia  the hai aur rahenge : Positive
Bhai ho aap❤ : Neutral
Bechara Aba kader pani nahi marna tha bechare par 🤣🤣🤣🤣🤣🤣 : Neutral
System hang to let all know YouTube views show delay than likes when more people have watched..... After 48 hours views will be exactly updated but likes are accurate  second to second... Hope all doubts are clarified GOAT talent munawar bhai❤ : Positive
Munawar farooqi fan like : Positive
Kya bolte YouTube hang hoga 😂😂 manowar Bhai🔥 : Neutral
Osm ek no ....bhut dino ke baad .... mood fresh ho gya .... wait tha 😂😂😂😂😂😂bhut acha ❤❤❤❤❤❤❤❤❤❤ : Neutral
bahot paka raha hai ......very poor jokes maaza nahi aaya.... : Negative

'''