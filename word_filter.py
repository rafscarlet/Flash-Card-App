import pandas

data = pandas.read_csv('data/spanish_words.csv')
words = data.to_dict(orient="records")

wordlist=[]
spanish_words_inlist = []

for word in words:
    es_word = word["Spanish"]
    en_word = word["English"]
    if es_word not in spanish_words_inlist and len(es_word) > 2:
        wordlist.append([es_word,en_word])
        spanish_words_inlist.append(es_word)


df = pandas.DataFrame(wordlist, columns=["Spanish", "English"])
# print(df)
df.to_csv('data/spanish_words.csv', index=False)
