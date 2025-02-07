"""
 Author: Varsha Rana
 Date: February 7, 2025
 Description: This script counts the number of words and characters in a text file (Frankenstein).
              It generates a report of the word count and character frequencies, displaying the
              results in a sorted manner.
"""


def count_words(text):
    """
    Count the number of words in a given text.

    Args:
        text (str): The input text to count words in.

    Returns:
        int: The number of words in the text.
    """
    words = text.split()
    return len(words)


def count_characters(text):
    """
    Count the frequency of each alphabetic character in a given text.

    Args:
        text (str): The input text to count characters in.

    Returns:
        dict: A dictionary where keys are characters and values are their frequencies.
    """
    text = text.lower()
    char_count = {}

    for char in text:
        if char.isalpha():  # Only count alphabetic characters
            char_count[char] = char_count.get(char, 0) + 1

    return char_count


def print_report(word_count, char_count):
    """
    Print a report showing the word count and character frequencies.

    Args:
        word_count (int): The total word count in the document.
        char_count (dict): The character frequencies to display.
    """
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")

    sorted_char_count = sorted(char_count.items(), key=lambda item: item[1], reverse=True)

    for char, count in sorted_char_count:
        print(f"The '{char}' character was found {count} times")

    print("--- End report ---")


def main():
    """
    Main function to execute the script. It reads the text from the file,
    counts words and characters,
    and prints the report.
    """
    path_to_file = 'books/frankenstein.txt'

    with open(path_to_file, 'r') as f:
        file_contents = f.read()

    word_count = count_words(file_contents)
    char_count = count_characters(file_contents)

    print_report(word_count, char_count)


if __name__ == "__main__":
    main()
