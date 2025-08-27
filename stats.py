
def get_num_words( text):
    return len(text.split())


def get_char_count( text):
    text = text.lower()
    counts = {}

    for char in text:
        if char in counts:
            counts[char] = counts[char] + 1
        else:
            counts[char] = 1
    
    return counts


def sort_chars( char_counts: dict):
    chars = sorted(char_counts)

    return_chars = []
    for char in chars:
        return_chars.append((char,char_counts[char]))


    return return_chars