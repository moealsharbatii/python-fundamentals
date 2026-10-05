# will need to use a dictionary (and this helped me because of the short explanation you mentioned in that example of 'hello')
# need to loop over the string, one letter at a time
# add to the dictionary for every new letter encountered, increase the count for every letter ran into again
# return the dictionary
def count_letters(word):
    count = {} # empty dictionary
    for letter in word:
        if(letter not in count):
            count[letter] = 1                
        else:
            count[letter] += 1

    return count

print(count_letters("hello"))