


            #python answer ------- 10



import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

def count_pos_tags(text):
    words = word_tokenize(text)

    tagged_words = pos_tag(words)

    pos_counts = {'Noun': 0, 'Verb': 0, 'Pronoun': 0, 'Adjective': 0}

    for word, tag in tagged_words:
        if tag.startswith('NN'):  # Noun
            pos_counts['Noun'] += 1
        elif tag.startswith('VB'):  # Verb
            pos_counts['Verb'] += 1
        elif tag.startswith('PRP'):  # Pronoun
            pos_counts['Pronoun'] += 1
        elif tag.startswith('JJ'):  # Adjective
            pos_counts['Adjective'] += 1

    return pos_counts

if __name__ == '__main__':
    # Test case 1: Count POS tags in a phrase
    phrase = "The quick brown fox jumps over the lazy dog"
    print("Test Case 1:")
    print("Input Phrase:", phrase)
    pos_counts = count_pos_tags(phrase)
    print("POS Counts:", pos_counts)

    # Test case 2: Count POS tags in a paragraph
    paragraph = "I love to travel and explore new places. The majestic mountains and serene beaches always leave me in awe. I enjoy capturing beautiful moments with my camera."
    print("\nTest Case 2:")
    print("Input Paragraph:", paragraph)
    pos_counts = count_pos_tags(paragraph)
    print("POS Counts:", pos_counts)

    # Test case 3: Count POS tags in a longer paragraph
    paragraph = "The quick brown fox jumps over the lazy dog. The dog barks loudly. The fox runs away. I see the fox in the distance. It is a beautiful sight."
    print("\nTest Case 3:")
    print("Input Paragraph:", paragraph)
    pos_counts = count_pos_tags(paragraph)
    print("POS Counts:", pos_counts)

