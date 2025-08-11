def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_chars(text):
    lowered = text.lower()
    frequency = {}
    for char in lowered:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency


