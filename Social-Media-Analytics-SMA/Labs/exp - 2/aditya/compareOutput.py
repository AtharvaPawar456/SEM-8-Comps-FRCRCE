# pip install fuzzywuzzy
# pip install python-Levenshtein

# Ref fuzzywuzzy : https://www.geeksforgeeks.org/fuzzywuzzy-python-library/

from fuzzywuzzy import fuzz 
from fuzzywuzzy import process 


textblobOutput = '''

['Subscribe to Android Developers → https://goo.gle/AndroidDevs', 'ياخي هذا اكثر من صنع مصنعي لي كإنسان.', 'الكلام كثير وبدون توضيح 😁', 'sar please helps❤❤', "It's just me, or did someone understand something more than Gemini?", 'his name is Murat, not Murant :)', "Let's be clear, you mean gambling apps.", 'Can you please share info on Jetpack compose carousel', 'Compose 1.6 was also released today', "I've watched this video with my family, and it brought us all together. Thank you!", 'When Google AI Studio will be available in UK?', 'Why is my Android system not updating?']
Subscribe to Android Developers → https://goo.gle/AndroidDevs : Neutral
ياخي هذا اكثر من صنع مصنعي لي كإنسان. : Neutral
الكلام كثير وبدون توضيح 😁 : Neutral
sar please helps❤❤ : Neutral
It's just me, or did someone understand something more than Gemini? : Positive
his name is Murat, not Murant :) : Positive
Let's be clear, you mean gambling apps. : Negative
Can you please share info on Jetpack compose carousel : Neutral
Compose 1.6 was also released today : Neutral
I've watched this video with my family, and it brought us all together. Thank you! : Neutral
When Google AI Studio will be available in UK? : Positive
Why is my Android system not updating? : Neutral

'''

vaderOutput = '''

['Subscribe to Android Developers → https://goo.gle/AndroidDevs', 'ياخي هذا اكثر من صنع مصنعي لي كإنسان.', 'الكلام كثير وبدون توضيح 😁', 'sar please helps❤❤', "It's just me, or did someone understand something more than Gemini?", 'his name is Murat, not Murant :)', "Let's be clear, you mean gambling apps.", 'Can you please share info on Jetpack compose carousel', 'Compose 1.6 was also released today', "I've watched this video with my family, and it brought us all together. Thank you!", 'When Google AI Studio will be available in UK?', 'Why is my Android system not updating?']
Subscribe to Android Developers → https://goo.gle/AndroidDevs : Neutral
ياخي هذا اكثر من صنع مصنعي لي كإنسان. : Neutral
الكلام كثير وبدون توضيح 😁 : Neutral
sar please helps❤❤ : Positive
It's just me, or did someone understand something more than Gemini? : Neutral
his name is Murat, not Murant :) : Negative
Let's be clear, you mean gambling apps. : Positive
Can you please share info on Jetpack compose carousel : Positive
Compose 1.6 was also released today : Neutral
I've watched this video with my family, and it brought us all together. Thank you! : Positive
When Google AI Studio will be available in UK? : Neutral
Why is my Android system not updating? : Neutral

'''


print("fuzz.ratio : ", fuzz.ratio(textblobOutput, vaderOutput))
print("fuzz.partial_ratio : ", fuzz.partial_ratio(textblobOutput, vaderOutput))
print("fuzz.token_sort_ratio : ", fuzz.token_sort_ratio(textblobOutput, vaderOutput))
print("fuzz.WRatio : ", fuzz.WRatio(textblobOutput, vaderOutput))


'''
### Terminal Output (vader_lexicon) :

fuzz.ratio :  85
fuzz.partial_ratio :  85
fuzz.token_sort_ratio :  95
fuzz.WRatio :  95


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