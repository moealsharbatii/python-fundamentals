# split up the sentence into a list of words
# once words are split, traverse the list and start comparing the lengths of each word
# whichever one is the longest, return that word
def longest_word(sentence):
    words = sentence.split()
    # longest = 0
    best = ""
    for word in words:
        if((len(word) > len(best))):
            best = word
            
    return best

print(longest_word("hi hi there yes lol"))