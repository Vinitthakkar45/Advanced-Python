with open("X.txt", 'r') as src:
    content = src.readlines()
    print(content)
    for line in content:
        words = line.split()
        print(words)

