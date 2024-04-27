def capitalize_first_letter(input_str):
    return " ".join(word.capitalize() for word in input_str.split())

print(capitalize_first_letter("sarang sajeev"))