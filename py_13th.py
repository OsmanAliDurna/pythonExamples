sentence = "i try So hard!"

sentenceUpper = sentence.upper()            # Make all characters to uppercase
sentenceLower = sentence.lower()            # Make all characters to lowercase
sentenceTitle = sentence.title()            # Make all words' first characters to uppercase and rest of them to lowercase
senteceCapitalize = sentence.capitalize()   # Make first characters of all string to uppercase and rest of them to lowercase

print(sentence, sentenceUpper, sentenceLower, sentenceTitle, senteceCapitalize, sep="\n")

sentence2 = "    " + sentence + "    "

print(sentence2)

sentenceStrip = sentence2.strip()
sentenceSplit = sentence2.split()
sentenceSplit2 = sentence2.split(" ")
sentenceJoin = " ~ ".join(sentenceSplit)

print(sentenceStrip)

print(sentenceSplit)

print(sentenceSplit[2]) # 3rd word

print(sentenceSplit2)

print(sentenceJoin)