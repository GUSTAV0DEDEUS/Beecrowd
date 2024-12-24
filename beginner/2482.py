n = int(input())
linguagem = []
felizNatal = []

for _ in range(n):
    linguagem.append(input().strip())
    felizNatal.append(input().strip())

m = int(input())

for _ in range(m):
    a = input().strip()
    b = input().strip()
    print(a)
    pos = linguagem.index(b)
    print(felizNatal[pos], end='\n\n')

linguagem.clear()
felizNatal.clear()
