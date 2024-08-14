def count(a, b):
    n = len(a)
    nums_earlier_in_a = []

    pos_dict_a = { a[i]:i for i in range(n) }
    pos_dict_b = { b[i]:i for i in range(n)}

    for x in a:
        if pos_dict_a[x] < pos_dict_b[x]:
            nums_earlier_in_a.append(x)

    return len(nums_earlier_in_a)




    

if __name__ == "__main__":
    print(count([2,3,4,1], [1,2,3,4])) # 3
    print(count([1,2,3,4], [1,2,3,4])) # 0
    print(count([4,7,3,1,6,2,5], [5,6,1,2,4,3,7])) # 3
    print(count([5,4,9,1,8,3,2,6,7], [6,2,8,4,9,1,5,7,3])) # 5