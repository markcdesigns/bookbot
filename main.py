def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    letter_dict = count_letters(text)
    print(text)
    print(f"{book_path} contains {word_count} words.")
    print(letter_dict)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    count = text.split()
    return len(count)

def count_letters(text):
    letter_dict = {}
    lowered_text = text.lower()
    for letter in lowered_text:
        if letter not in letter_dict:
            letter_dict[letter] = 1
        elif letter in letter_dict:
            letter_dict[letter] += 1
    return letter_dict


main()