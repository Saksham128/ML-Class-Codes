# Question-1
#arr = ['Mary', 'had', 'a', 'a', 'little', 'lamb']
# Question-2
arr = [['A', 'Mary'], ['B', 'had'], ['C', 'a']]
for i, j in enumerate(arr):
    print(i, "=", type(i), i,end=" ")
    print(j, "=", type(j), j)
for i, [j, k] in enumerate(arr):
    print(i, "=", type(i), i,end=" ")
    print(j, "=", type(j), j,k)

for i, j in enumerate(arr):
    print(i, j)
