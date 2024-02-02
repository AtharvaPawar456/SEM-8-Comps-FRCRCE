# pip install fuzzywuzzy
# pip install python-Levenshtein

# Ref fuzzywuzzy : https://www.geeksforgeeks.org/fuzzywuzzy-python-library/

from fuzzywuzzy import fuzz 
from fuzzywuzzy import process 


textblobOutput = '''
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

vaderOutput = '''
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


print("fuzz.ratio : ", fuzz.ratio(textblobOutput, vaderOutput))
print("fuzz.partial_ratio : ", fuzz.partial_ratio(textblobOutput, vaderOutput))
print("fuzz.token_sort_ratio : ", fuzz.token_sort_ratio(textblobOutput, vaderOutput))
print("fuzz.WRatio : ", fuzz.WRatio(textblobOutput, vaderOutput))


'''
### Terminal Output (vader_lexicon) :


fuzz.ratio :  87
fuzz.partial_ratio :  87
fuzz.token_sort_ratio :  72
fuzz.WRatio :  95



'''

'''
### About fuzzywuzzy Classes:


1. fuzz.ratio:

    This method computes the simple Levenshtein distance ratio between two strings.
    It calculates the similarity by taking the total number of matching characters divided by the length of the longer string.
    A higher ratio indicates a higher similarity.

2. fuzz.partial_ratio:

    This method is similar to fuzz.ratio but allows for partial matching.
    It tries to find the best partial match of the shorter string within the longer string.
    It is useful when comparing strings that may have slight differences or additional characters.

3. fuzz.token_sort_ratio:

    This method tokenizes the input strings, sorts the tokens, and then calculates the similarity ratio based on the sorted tokens.
    It is particularly useful when comparing strings with words in different orders.
    It considers the set of words in each string without considering their original order.

4. fuzz.WRatio:

    This method is similar to fuzz.ratio but considers word-based matching and allows for partial matches.
    It uses a weighted ratio, where word matches are given more importance than character matches.
    It is useful when comparing strings that have word-level variations.

'''





'''
Looking at the comparison between TextBlob and Vader sentiment analysis outputs for the given comments, here are some observations:

1. TextBlob Output:
   - Tends to label more comments as "Neutral."
   - Identifies sentiments based on the overall tone of the text without considering emojis explicitly.
   - Provides more varied sentiment labels, including "Neutral," "Positive," and "Negative."

2. Vader Output:
   - Labels most comments as "Positive."
   - Takes into account the presence of emojis and assigns a positive sentiment if positive emojis are present.
   - Generally provides a more positive-leaning sentiment classification.

Reasons Why Vader Might be Considered Better:
   - Handling Emojis:
     - Vader appears to handle comments with emojis better. It recognizes positive sentiments associated with emojis like ❤ and 💐 and assigns an overall positive sentiment.

   - Subjectivity and Nuances:
     - Vader may better capture the nuances and subjectivity in comments, especially in mixed sentiment expressions. For example, comments like "sir please CSE Gate k liye bhi kuch tips deziye ya phir koi course le aaye" are labeled as "Positive" by Vader, possibly acknowledging the positive intent.

   - Domain-Specific Design:
     - Vader is specifically designed for social media text, where sentiments can be conveyed through unconventional language, emoticons, and slangs. This makes it well-suited for sentiment analysis in platforms like YouTube.

Considerations:
   - The effectiveness of sentiment analysis tools depends on the nature of the dataset and the specific use case.
   - The choice between TextBlob and Vader might depend on the desired outcome, as both tools have their strengths and weaknesses.

Conclusion:
   - Vader might be considered better in this context due to its handling of emojis, recognition of social media language nuances, and the overall positive-leaning sentiment classification.
   - However, the choice between TextBlob and Vader depends on the specific requirements and characteristics of the dataset, and it's recommended to evaluate based on the context of use.

'''


'''
Sentiment Analysis (SA) Process Pipeline:

Sentiment Analysis involves several steps in its pipeline:

1. Data Collection:
   - Gather textual data from various sources, such as social media posts, comments, reviews, or other text-based content.

2. Text Preprocessing:
   - Clean and preprocess the text data by removing noise, stopwords, and irrelevant information. Tokenization and stemming may also be applied.

3. Feature Extraction:
   - Convert the processed text into numerical features using techniques like TF-IDF (Term Frequency-Inverse Document Frequency) or word embeddings.

4. Sentiment Classification:
   - Utilize machine learning or natural language processing models to classify the sentiment of each piece of text into categories like positive, negative, or neutral.

5. Post-Processing:
   - Evaluate the results, fine-tune the model, and handle any misclassifications. Post-processing may include adjusting for context or considering sentiment intensity.

6. Analysis and Visualization:
   - Analyze the overall sentiment trends, create visualizations, and extract meaningful insights from the sentiment-labeled data.

List of Generic and Social Network Sentiment Analysis Tools (Free to Use):
1. NLTK (Natural Language Toolkit):
   - Generic tool with modules for natural language processing and sentiment analysis.

2. TextBlob:
   - Simplified and easy-to-use tool for sentiment analysis, based on NLTK and Pattern libraries.

3. VADER (Valence Aware Dictionary and sEntiment Reasoner):
   - Specifically designed for social media sentiment analysis, part of the NLTK library.

4. IBM Watson Natural Language Understanding:
   - Offers sentiment analysis capabilities with a limited free tier.

Tools Performing Emotion Recognition (ER) along with Sentiment Analysis in English:
1. IBM Watson Natural Language Understanding:
   - Provides both sentiment analysis and emotion recognition features.

2. Microsoft Azure Text Analytics:
   - Offers sentiment analysis and recognizes key emotions.

3. TextBlob:
   - Besides sentiment analysis, it also provides a basic emotion analysis.

Tools Allowing URLs/Keywords/Text for Data Input and JSON/CSV for Data Export:
1. IBM Watson Natural Language Understanding:
   - Accepts text, URLs, or HTML as input and provides JSON as output.

2. Microsoft Azure Text Analytics:
   - Supports plain text or URLs as input and provides JSON output.

3. TextBlob:
   - Accepts text input and allows exporting results in various formats, including JSON.

4. VADER (NLTK Library):
   - Handles text input and can be integrated with Python for further data processing.

Human-like Response:
Sure, here's a more human-like response:

"Hey there! So, when we talk about Sentiment Analysis, it's like diving into a series of steps. First, we scoop up text data from different places. Then, we clean it up, kind of like tidying up a room. Next, we turn words into numbers, using some cool techniques. After that, it's time to decide if the text is positive, negative, or just hanging out in neutral land. But wait, we're not done! We take a second look, make adjustments, and try to really understand the vibe of the text.

Now, for the tools – there are some cool ones out there that won't cost you a dime. NLTK, TextBlob, and VADER are like the rockstars of generic and social media sentiment analysis. But if you're into emotions too, check out IBM Watson and Microsoft Azure – they're like the emotion wizards of the tech world.

And hey, if you want to toss in some URLs, keywords, or plain text for analysis, these tools got you covered. IBM Watson, Microsoft Azure, TextBlob, and even VADER can handle that. Plus, they're cool with giving you the results in JSON or CSV format. So, it's like they speak your language, whether you're a data geek or just someone curious about what the words are saying. Hope this helps you navigate the sentiment analysis playground!"









5. Tools Supporting More Than 5 Text Languages:
1. IBM Watson Natural Language Understanding:

2. Microsoft Azure Text Analytics:

3. Google Cloud Natural Language API:

4. TextBlob:

6. Tools Supporting Both APIs and Client for Popular Programming Languages:
1. IBM Watson Natural Language Understanding

2. Microsoft Azure Text Analytics

3. Google Cloud Natural Language API

4. TextBlob


7. Concluding Remark on Best Recommended Tool for Business Analysis:

IBM Watson Natural Language Understanding:
Among the 24 tools, IBM Watson Natural Language Understanding stands out as the top recommendation for business analysis. The reasons are quite compelling:

1. Multilingual Support:
   - IBM Watson NLU excels in supporting sentiment analysis for a diverse range of languages. This is crucial for businesses operating globally, ensuring a comprehensive understanding of customer sentiments across different regions.

2. Robust API and Client Support:
   - The tool offers both APIs and client libraries for popular programming languages, making it highly versatile and easily integrable into existing business applications. This flexibility caters to diverse development environments and the preferences of developers.

3. Advanced Features:
   - IBM Watson NLU goes beyond basic sentiment analysis. It provides additional features like emotion recognition, entity recognition, and concept tagging, offering a more nuanced understanding of textual data.

4. Proven Business Integration:
   - IBM Watson has a strong reputation for business applications and has been successfully integrated into various industries, including finance, healthcare, and customer service. This track record makes it a reliable choice for businesses seeking actionable insights from textual data.

5. Scalability and Reliability:
   - With IBM's robust infrastructure, Watson NLU ensures scalability and reliability, crucial factors for businesses dealing with large volumes of textual data.

In conclusion, IBM Watson Natural Language Understanding emerges as the best-recommended tool for business analysis, combining language diversity, developer-friendly features, advanced capabilities, and a proven track record in real-world business applications.






'''