def logest_word(input_str):
    words=input_str.split()
    return max(words,key=len)

print(logest_word("ggvcibyuuybyubyu uirhubuchbhb"))