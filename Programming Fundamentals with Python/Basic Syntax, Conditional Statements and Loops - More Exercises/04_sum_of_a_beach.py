string = input()
lower_string = string.lower()
n = 0
string_names = ["Water", "Sun", "Fish", "Sand"]
string_list = [i.lower() for i in string_names]
for i in range(len(string_list)):
    new_string = string_list[i]
    n += lower_string.count(new_string)
print(n)
