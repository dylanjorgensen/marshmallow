
def anti_vowel(text):
    new_word = ''
    for x in text:
        if x not in "aeiouAEIOU":
            new_word += x
    print new_word
    return new_word

anti_vowel("Hey You!")
