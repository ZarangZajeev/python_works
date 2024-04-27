def first_non_repeating_char(input_str):
    char_count={}
    for char in input_str:
        char_count[char]=char_count.get(char,0)+1
    print(char_count)
    for char in input_str:
        if char_count[char]==1:
            return char
    return None
    
print(first_non_repeating_char("sssfjhby"))