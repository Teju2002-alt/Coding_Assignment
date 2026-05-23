text = input("Enter sentence: ")
words = text.lower().split()
count = {}
for word in words:
    if word in count:
        count[word] = count[word] + 1
    else:
        count[word] = 1

max_count = 0
result = ""

for word in count:
    if count[word] > max_count:
        max_count = count[word]
        result = word

    elif count[word] == max_count:
        if word < result:
            result = word

print("Most frequent word:", result)