my_string = "python is good language to code"
cleaned_my_string = list(''.join(char for char in my_string if char.isalpha()))
rez_dictionary = {}
for key in cleaned_my_string:
    counter = 0
    for letter in cleaned_my_string:
        if key == letter:
            counter += 1
    rez_dictionary[key] = counter
print(rez_dictionary)
