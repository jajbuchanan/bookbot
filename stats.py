def get_word_count(text):
    word_count = 0
    input_text = text.split()
    for word in input_text:
        word_count += 1
    return word_count


def char_count(text):
    char_counts = {}
    for char in text:
        char = char.lower()
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts


def dictify(char_counts):
    output = []  # Sorted list of dictionaries
    for key in char_counts:
        output_dict = {}
        output_dict["char"] = key
        output_dict["count"] = char_counts[key]
        output.append(output_dict)

    def sort_on(output):
        return output["count"]

    output.sort(reverse=True, key=sort_on)

    return output
