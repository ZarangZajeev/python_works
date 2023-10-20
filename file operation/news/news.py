news_read=open("D:\\MY PC\\july_python_works\\file operation\\news\\news.txt")
stop_words_read=open("D:\\MY PC\\july_python_works\\file operation\\news\\stopwords.txt")

news_words=set()
stop_words=set()

for nw in news_read:
    n_words=nw.split()
    for w in n_words:
        news_words.add(w)


stop_words={sw.rstrip("\n") for sw in stop_words_read }

words=news_words.difference(stop_words)
print(words)