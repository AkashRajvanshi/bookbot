def count_words(text):
    return len(text.split())


def char_frequencies(text):
    text = text.lower()
    freq = {}
    for char in text:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq


def sort_char_frequencies(freq_dict):
    char_list = [{"char": char, "num": count} for char, count in freq_dict.items()]
    char_list.sort(key=lambda x: x["num"], reverse=True)
    return char_list
