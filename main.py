def list_insert(start, num, rep):
    ref_list = [0, 1, 2, 3, 4, 5]
    return ref_list[:start] + [num] * rep + ref_list[start:]
print(list_insert(int(input()),int(input()),int(input())))
