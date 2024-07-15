def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    dictionary_list = letter_dictionary(text)
    dictionary_list.sort(reverse=True, key=sort_on)
    out(dictionary_list, num_words, book_path)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def letter_dictionary(text):
    input_text = text.lower()
    letter_dict = {}
    for letter in input_text:
        if letter.isalpha():
            if letter in letter_dict:
                letter_dict[letter] += 1
            else: 
                letter_dict[letter] = 1

    output_list = [{"char": k, "num": v} for k, v in letter_dict.items()] # This seems to be creating a list that converts the key/value pairs in the letter_dict dictionary, and making a new list that add items, adding the "char" and "num" key and value for each dictionary in the list, iterating through the items in each of the dictionary entries. 

    print(output_list)
    return(output_list)

def sort_on(dict):
    return dict["num"]

def out(sorted_dictionary, num_words, book_path):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    for item in sorted_dictionary:
        print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")

main()
