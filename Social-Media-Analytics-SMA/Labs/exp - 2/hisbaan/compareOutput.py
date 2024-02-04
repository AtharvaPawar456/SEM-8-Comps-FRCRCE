# pip install fuzzywuzzy
# pip install python-Levenshtein

# Ref fuzzywuzzy : https://www.geeksforgeeks.org/fuzzywuzzy-python-library/

from fuzzywuzzy import fuzz 
from fuzzywuzzy import process 


textblobOutput = '''
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

vaderOutput = '''

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


print("fuzz.ratio : ", fuzz.ratio(textblobOutput, vaderOutput))
print("fuzz.partial_ratio : ", fuzz.partial_ratio(textblobOutput, vaderOutput))
print("fuzz.token_sort_ratio : ", fuzz.token_sort_ratio(textblobOutput, vaderOutput))
print("fuzz.WRatio : ", fuzz.WRatio(textblobOutput, vaderOutput))


'''
### Terminal Output (vader_lexicon) :


fuzz.ratio :  72
fuzz.partial_ratio :  77
fuzz.token_sort_ratio :  3
fuzz.WRatio :  86


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