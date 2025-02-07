def count_words(text):
    # Split the text into words based on whitespace and return the number of words
    words = text.split()
    return len(words)


def count_characters(text):
    # Convert text to lowercase
    text = text.lower()

    # Initialize an empty dictionary to store character counts
    char_count = {}

    # Loop through each character in the text
    for char in text:
        if char.isalpha():  # Only count alphabetic characters
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    return char_count


def print_report(word_count, char_count):
    # Print the report
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")

    # Sort the character counts by frequency in descending order
    sorted_char_count = sorted(char_count.items(), key=lambda item: item[1], reverse=True)

    # Print each character and its count
    for char, count in sorted_char_count:
        print(f"The '{char}' character was found {count} times")

    print("--- End report ---")


def main():
    # Path to the Frankenstein text file
    path_to_file = 'books/frankenstein.txt'

    # Open the file and read its contents
    with open(path_to_file, 'r') as f:
        file_contents = f.read()

    # Count the words and characters in the file
    word_count = count_words(file_contents)
    char_count = count_characters(file_contents)

    # Print the report
    print_report(word_count, char_count)


if __name__ == "__main__":
    main()
