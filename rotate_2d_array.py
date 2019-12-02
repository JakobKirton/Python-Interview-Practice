#input: First line is amount of rotations. Remaining lines contain array in format- 11 2 4 6 7

n = int(input())
s = 4 #Fixed array length

def build_aray(size):
    array = []
    for i in range(size):
        sub_array = input().strip().split(' ')
        array.append(sub_array)
    return array


def rotate_array(rotations, array):
    if rotations < 0:
        return []
    if rotations == 0:
        for row in array:
            for col in row:
                print(col, end= ' ')
            print()

    rotated_array = list(zip(*array[::-1]))
    rotate_array(rotations-1, rotated_array)


array = build_aray(s)
print("\n")
rotate_array(n,array)
