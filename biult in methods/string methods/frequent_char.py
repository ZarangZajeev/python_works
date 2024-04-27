def most_frequent(input_str):
    char_count={}
    for char in input_str:
        char_count[char]=char_count.get(char,0)+1
    return max(char_count,key=char_count.get)

print(most_frequent("hellloooo"))