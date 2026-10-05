# Split up the sentence using .split()
# array of words is now made, so now traverse the array
# make a count for each word. If you see a word again then add to that count
# I'll need to return an array of counts
def count_words(sentence):
    words = sentence.split()
    counts = {}
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
            

    return counts

print(count_words("hi hi there lol yes"))

# def count_words(sentence):
#     counts = []
#     for word in sentence:
#         words = word.split()
#         print(words)
#         for words in sentence:
#             if(word in counts[word]):
#                 counts[word] += 1
#                 print(counts)
#     return counts


