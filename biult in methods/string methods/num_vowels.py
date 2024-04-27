def count_vowels(input_str):
    vowels="aeiouAEIOU"
    return sum(1 for char in input_str if char in vowels)

print(count_vowels("sajeev"))