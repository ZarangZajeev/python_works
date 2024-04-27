def count_word(input_str):
    words=input_str.split()
    word_count={}
    for word in words:
        word_count[word]=word_count.get(word,0)+1
    return word_count

print(count_word("hello guys hello"))