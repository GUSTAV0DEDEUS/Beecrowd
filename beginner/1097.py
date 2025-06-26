maxJ = -4
minJ = -7
for i in [1, 3, 5, 7, 9]:
    for j in range(minJ, maxJ):
        print(f"I={i} J={abs(j)}")
    minJ -= 2
    maxJ -= 2