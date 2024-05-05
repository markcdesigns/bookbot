def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    letter_dict = count_letters(text)
    converted = dict_to_list(letter_dict)
    print("Analyzing Text...")
    print("----- Book Report -----\n")
    print(f"{book_path} contains {word_count} words.\n")
    for x in converted:
        print(f"The letter '{x[0]}' appears {x[1]} times.")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    count = text.split()
    return len(count)

def count_letters(text):
    letter_dict = {}
    lowered_text = text.lower()
    filtered_text = ""
    for letter in lowered_text:
        if letter.isalpha() == True:
            filtered_text += letter
    for letter in filtered_text:
        if letter not in letter_dict:
            letter_dict[letter] = 1
        elif letter in letter_dict:
            letter_dict[letter] += 1
    return letter_dict

def dict_to_list(dict):
    sort_list = dict
    sort_list = sorted(sort_list.items(), reverse=True, key=lambda x: x[1])
    return sort_list


main()