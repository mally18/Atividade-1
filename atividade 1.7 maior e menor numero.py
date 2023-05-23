a = int(input("Digite o 1 valor:"))
b = int(input("Digite o 2 valor:"))
c = int(input("Digite o 3 valor:"))
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
menor = a
if b < c and b < a:
    menor = b
if c < b and c < a:
    menor = c
print(f"O menor número foi {menor}")
print(f"O maior número foi {maior}")