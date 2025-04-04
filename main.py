from stats import get_word_count, char_count, dictify
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def print_report(output_dictionary):
    for character in output_dictionary:
        if character["char"].isalpha():
            print(f"{character['char']}: {character['count']}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = get_word_count(text)

    # print(char_count(text))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    output_dictionary = dictify(char_count(text))
    print_report(output_dictionary)
    print("============= END ===============")


main()
