current_symbol = input()
saved_text = ""
counter_c = 0
counter_o = 0
counter_n = 0

while current_symbol != "End":

    if current_symbol == "c":
        counter_c += 1
        if counter_c > 1:
            saved_text += current_symbol

    elif current_symbol == "o":
        counter_o += 1
        if counter_o > 1:
            saved_text += current_symbol

    elif current_symbol == "n":
        counter_n += 1
        if counter_n > 1:
            saved_text += current_symbol

    elif not current_symbol.isalpha():
        pass

    else:
        saved_text += current_symbol

    if counter_c >= 1 and counter_o >= 1 and counter_n:
        print(saved_text, end=' ')
        counter_c = 0
        counter_o = 0
        counter_n = 0
        saved_text = ""

    current_symbol = input()