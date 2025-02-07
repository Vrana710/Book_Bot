def count_words(text):
    # Split the text into words based on whitespace and return the number of words
    words = text.split()
    return len(words)


def main():
    # Path to the Frankenstein text file
    path_to_file = 'books/frankenstein.txt'

    # Open the file and read its contents
    with open(path_to_file, 'r') as f:
        file_contents = f.read()

    # Print the contents of the file (optional)
    print(file_contents)

    # Count the words in the file and print the result
    word_count = count_words(file_contents)
    print(f"The book contains {word_count} words.")


if __name__ == "__main__":
    main()
