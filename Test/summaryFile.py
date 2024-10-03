def file_summary(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    word_count = len(content.split())

    char_count_including_spaces = len(content)
    char_count_excluding_spaces = len(content.replace(' ', ''))
    char_frequency = {}
    for char in content:
        char_frequency[char] = char_frequency.get(char, 0) + 1

    paragraph_count = len(content.split('\n\n'))

    summary = {
        'Word Count': word_count,
        'Character Count (Including Spaces)': char_count_including_spaces,
        'Character Count (Excluding Spaces)': char_count_excluding_spaces,
        'Character Frequency': char_frequency,
        'Paragraph Count': paragraph_count
    }
    with open("Y.txt", 'w') as file:
        print(summary, file=file)

file_path = 'X.txt'
file_summary(file_path)
