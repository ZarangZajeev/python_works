def remove_duplicate(input_str):
    return "".join(sorted(set(input_str),key=input_str.index))

print(remove_duplicate("hello"))