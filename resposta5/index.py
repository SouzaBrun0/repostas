def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

# Exemplo de uso
string = input("Informe uma string: ")
print(f"String invertida: {reverse_string(string)}")
