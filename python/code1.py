#sec_no = 3
#guess = int(input("guess the secret number")
#while guess != sec_no:
#  guess = int(input("Wrong!!! \n choose another number")
#print ("Congratulations! you guessed it right)
#a = []
#for i in range(5):
#    a.append([])
#    for j in range(5):
#        a[i].append(j)
#
#print(a)
#print(a[3][3])
matrix = [[[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]]]

matrix2 = []

for submatrix in matrix:
  for val in submatrix:
    matrix2.append(val)

print(matrix2)
print(matrix2[2])
print(matrix2[2][2])







