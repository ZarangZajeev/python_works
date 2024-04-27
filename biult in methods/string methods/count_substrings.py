def count_substring_occurances(input_str,substring):
    count=0
    index=0
    while True:
        index=input_str.find(substring,index)
        if index==-1:
            break
        count+=1
        index+=1
    return count

print(count_substring_occurances("sarang","a"))