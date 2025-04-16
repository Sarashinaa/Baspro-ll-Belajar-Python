matriks1 = [
    [5, 1, 4, 2, 3],
    [2, 3, 1, 5, 4],
    [4, 4, 2, 1, 5],
    [1, 5, 3, 2, 2],
    [3, 2, 5, 4, 1]
]

matriks2 = [
    [4, 2, 5, 3, 1],
    [3, 1, 2, 4, 5],
    [2, 5, 3, 1, 4],
    [5, 3, 1, 2, 2],
    [1, 4, 4, 5, 3]
]

hasil = []
for i in range(len(matriks1)):
    row = []
    for j in range(len(matriks2[0])):
        sum = 0
        for k in range(len(matriks2)):
            sum += matriks1[i][k] * matriks2[k][j]
        row.append(sum)
    hasil.append(row)

print("Hasil perkalian matriks:")
for row in hasil:
    print(row)
