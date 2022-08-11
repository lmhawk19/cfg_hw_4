
matrix = [
[1,4,7,12,15,1000],
[2,5,19,31,32,1001],
[3,8,24,33,35,1002],
[40,41,42,44,45,1003],
[99,100,103,106,128,1004]
]

target = 7


def search_in_matrix(matrix, target):
    for i, value in enumerate(matrix):
        for k, value in enumerate(value):
            if value == target:
                return([i, k])
    return [-1,-1]
