def longest_words():
    with open('article.txt', 'r') as file:
        text = file.read()
        a = text.replace("\n", " ")
        text = a.split(" ")
        g = dict(map(lambda x: (x, len(x)), text))
        f = []
        max = 0
        for i in g.items():
            if i[1] > max:
                f = []
                max = i[1]
                f.append(i)
            elif i[1] == max:
                f.append(i)
        print(f)
        file.close()

longest_words()