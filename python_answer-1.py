



             #Python Answer ------ 1



def find_highest_frequency_word_length(string):
    word_frequency = {}
    

    
    words = string.split()
    
    
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    
  
    highest_frequency = 0
    highest_frequency_word = ''
    
    for word, frequency in word_frequency.items():
        if frequency > highest_frequency:
            highest_frequency = frequency
            highest_frequency_word = word
    
    
    return len(highest_frequency_word)



string = "write write write all the number from from from 1 to 100"
print(find_highest_frequency_word_length(string))  # Output: 5














