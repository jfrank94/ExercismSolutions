def is_pangram(sentence):

    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
             'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    sentence = sentence.lower()
    letter_map = {}
    count = 0
    for element in sentence:
        if element not in letter_map and element in alpha:
            letter_map[element] = 1
        elif element in alpha:
            letter_map[element] += 1
    return len(letter_map) == 26
