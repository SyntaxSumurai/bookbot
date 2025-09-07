from stats import get_num_words, get_num_characters, sort_dict
import sys

def get_book_text(file_path):
    file_content=""

    with open(file_path) as f:
        file_content = f.read()
    return file_content


def _main_():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    content = get_book_text(sys.argv[1])
    no_of_words = get_num_words(content)
    no_of_characters = get_num_characters(content)
    dict_sorted = sort_dict(no_of_characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {no_of_words} total words")
    print("--------- Character Count -------")
    for i in dict_sorted:
        if not i["char"].isalpha():
            continue
        print(f"{i["char"]}: {i["num"]}")
    
    print("============= END ===============")
_main_()