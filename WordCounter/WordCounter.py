print("==Word Counter==")

# checking if file is available.
while True:
    file_name = input("Please input a file name (must be inside this program's directory): ")
    try:
        file = open(file_name, "r")
    except (FileNotFoundError, IOError):
        print("There's a problem with opening a file.")
    else:
        break

# list containing every word from the file.
all_words = []

# reading line-by-line, cleaning words from commas etc and populating all_words list.
for line in file:
    words_in_line = line.split()
    for word in words_in_line:

        # clearing word from triple dots.
        if "..." in word:
            index = words_in_line.index(word)
            word = word.replace("...", "")
            words_in_line[index] = word

        # purging word from dots, commas etc.
        if word.endswith('.') or word.endswith(',') or word.endswith(';'):
            index = words_in_line.index(word)
            word = word[:-1]
            words_in_line[index] = word

    # all words to lower case.
    words_in_line = [x.lower() for x in words_in_line]
    all_words.extend(words_in_line)

single_words = []
word_counter = []

# counting words.
for word in all_words:
    if word not in single_words:
        single_words.append(word)
        word_counter.append(1)
    else:
        index = single_words.index(word)
        word_counter[index] = word_counter[index] + 1

# printing the result.
print("Words counted:")
for x in single_words:
    index = single_words.index(x)
    print(x + ": " + str(word_counter[index]))
