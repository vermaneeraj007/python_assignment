
                #Python Answer -------- 2



def is_valid_string(s):
    
    char_frequency = {}
    for char in s:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1
    
    
    frequency_count = {}
    for frequency in char_frequency.values():
        if frequency in frequency_count:
            frequency_count[frequency] += 1
        else:
            frequency_count[frequency] = 1
    
   
    if len(frequency_count) == 1:
        return "YES"
    
    
    if len(frequency_count) == 2:
        freq1, count1 = frequency_count.popitem()
        freq2, count2 = frequency_count.popitem()
        if (count1 == 1 and freq1 == 1) or (count2 == 1 and freq2 == 1):
            return "YES"
    
    return "NO"


s1 = "abc"
print(is_valid_string(s1))  # Output: YES

s2 = "abcc"
print(is_valid_string(s2))  # Output: NO


