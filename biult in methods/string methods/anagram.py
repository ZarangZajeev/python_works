def anagram(input_str1,input_str2):
    return "Anagram" if sorted(input_str1)==sorted(input_str2) else "Not anagram"
         
print(anagram("sarang","aasrng"))