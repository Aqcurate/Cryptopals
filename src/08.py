
string = "YELLOW SUBMARINE"
padding_size = 20
padding_digit = padding_size - len(string)

print(("{}{}".format(string, chr(padding_digit) * padding_digit)).encode('utf-8'))
