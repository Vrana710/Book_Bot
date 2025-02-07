def main():
    # Path to the Frankenstein text file
    path_to_file = 'books/frankenstein.txt'

    # Open the file and read its contents
    with open(path_to_file, 'r') as f:
        file_contents = f.read()

    # Print the contents of the file
    print(file_contents)


if __name__ == "__main__":
    main()
