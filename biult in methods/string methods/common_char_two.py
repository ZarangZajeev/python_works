def common_char(input_str1,input_str2):
    return " ".join(char for char in set(input_str1) if char in set(input_str2))

print(common_char("sarang","sajegev"))