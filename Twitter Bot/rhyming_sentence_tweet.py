from authentication import api
import requests

string = input("Insert the sentence to rhyme: ")
sentence = string.split()
new_sentence_tweet = ''
for word in sentence:
    response = requests.get("https://rhymebrain.com/talk?function=getRhymes&word="+word)
    new_word = response.json()
    counter = 0
    for w in new_word:
        if counter < 1:
            new_sentence_tweet += w["word"]+ " "
            counter += 1
print(new_sentence_tweet)

api.update_status(new_sentence_tweet)

print('success!')

    