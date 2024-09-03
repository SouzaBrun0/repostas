def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

string = input("Informe uma Palavra: ")
print(f"Palavra invertida: {reverse_string(string)}")
