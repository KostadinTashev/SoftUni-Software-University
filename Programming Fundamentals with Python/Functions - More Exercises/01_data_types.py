def data_tp(first_string, second_string):
    if first_string == "int":
        return 2 * int(second_string)
    if first_string == "real":
        return f"{1.50 * float(second_string):.2f}"
    if first_string == "string":
        return "$" + second_string + "$"


data_type = input()
string = input()
print(data_tp(data_type, string))