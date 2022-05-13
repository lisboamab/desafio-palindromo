

palavra = input("Digite sua palavra ").lower()
print(palavra)
if palavra == palavra[::-1]:
    print("A sua palavra é um palindromo")
else:
    print("A sua palavra não é um palindromo")

print(palavra[::-1])