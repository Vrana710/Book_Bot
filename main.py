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
        # If the character is already in the dictionary, increment its count
        if char in char_count:
            char_count[char] += 1
        else:
            # If it's the first occurrence, set its count to 1
            char_count[char] = 1

    return char_count


def main():
    # Path to the Frankenstein text file
    path_to_file = 'books/frankenstein.txt'

    # Open the file and read its contents
    with open(path_to_file, 'r') as f:
        file_contents = f.read()

    # Count the words in the file and print the result
    word_count = count_words(file_contents)
    print(f"The book contains {word_count} words.")

    # Count the characters in the file and print the result
    char_count = count_characters(file_contents)
    print("Character frequencies:")
    print(char_count)


if __name__ == "__main__":
    main()
