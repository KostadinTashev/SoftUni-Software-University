number = int(input())
word = input()

all_words = []
matched_words = []

for _ in range(number):
    string = input()
    all_words.append(string)
    if word in string:
        matched_words.append(string)
print(all_words)
print(matched_words)