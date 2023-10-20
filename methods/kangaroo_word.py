# source_word="chicken"
# target_word="hen"
# s_count=len(source_word)
# t_count=len(target_word)
# for i in range(0,3):
#     if(target_word[i]==source_word[i]):
#         print("Given words ara kangaroo words")






source_word = "chicken"
target_word = "hen"
s_count = len(source_word)
t_count = len(target_word)


# if t_count < 3:
#     print("Target word is too short to be a kangaroo word.")
# else:
#     is_kangaroo = True

#     for i in range(3):
#         if target_word[i] != source_word[i]:
#             is_kangaroo = False
#             break
    
#     if is_kangaroo:
#         print("Given words are kangaroo words")
#     else:
#         print("Given words are not kangaroo words")

for i in range(0, t_count):
    if target_word[i] == source_word[i]:
        print("Given words are kangaroo words")
        break
    else:
        print("Given words are not kangaroo words")
else:
    print("Given words are not kangaroo words")